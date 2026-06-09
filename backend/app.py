import os
import shutil
import json

from fastapi import FastAPI, UploadFile, File
from src.pipeline import run_insightflow_pipeline
from fastapi.staticfiles import StaticFiles
from src.storage import load_report, save_chat_message, load_chat_history, save_report
from pydantic import BaseModel
from src.report_generator import build_report_prompt
from src.gemini_service import call_gemini
from src.qa import build_qa_prompt



app = FastAPI()

app.mount(
    "/charts",
    StaticFiles(directory="charts"),
    name="charts"
)

UPLOAD_FOLDER = "uploads"


@app.get("/")
def home():
    return {
        "message": "InsightFlow API is running"
    }



def convert_numpy_types(obj):
    if hasattr(obj, "item"):
        return obj.item()

    if isinstance(obj, dict):
        return {
            key: convert_numpy_types(value)
            for key, value in obj.items()
        }

    if isinstance(obj, list):
        return [
            convert_numpy_types(item)
            for item in obj
        ]

    return obj


@app.post("/analyze")
def analyze_dataset(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    report = run_insightflow_pipeline(file_path)

    report["cleaned_df"] = report["cleaned_df"].to_dict(
        orient="records"
    )

    report = convert_numpy_types(report)

    saved_report = save_report(report)

    report["saved_report"] = saved_report

    return report


@app.get("/reports")
def get_reports():
    reports_folder = "reports"

    reports = []

    if not os.path.exists(reports_folder):
        return reports

    for file_name in os.listdir(reports_folder):
        if file_name.endswith(".json"):
            report_id = file_name.replace(".json", "")

            reports.append(
                {
                    "report_id": report_id,
                    "report_path": f"reports/{file_name}"
                }
            )

    return reports


@app.get("/reports/{report_id}")
def get_report_by_id(report_id: str):
    file_path = f"reports/{report_id}.json"

    if not os.path.exists(file_path):
        return {
            "error": f"Report '{report_id}' not found."
        }

    with open(file_path, "r") as file:
        report = json.load(file)

    return report


class QuestionRequest(BaseModel):
    report_id: str
    question: str


@app.post("/ask")
def ask_question(request: QuestionRequest):
    report = load_report(request.report_id)

    if report is None:
        return {
            "error": f"Report '{request.report_id}' not found."
        }

    chat_history = load_chat_history(request.report_id)

    prompt = build_qa_prompt(
        report,
        request.question,
        chat_history
    )

    ai_answer = call_gemini(prompt)

    answer_text = ai_answer.get("response", "")

    save_chat_message(
        request.report_id,
        "user",
        request.question
    )

    save_chat_message(
        request.report_id,
        "assistant",
        answer_text
    )

    return {
        "report_id": request.report_id,
        "question": request.question,
        "answer": answer_text
    }


@app.get("/reports/{report_id}/chat")
def get_chat_history(report_id: str):

    report = load_report(report_id)

    if report is None:
        return {
            "error": f"Report '{report_id}' not found."
        }

    chat_history = load_chat_history(report_id)

    return {
        "report_id": report_id,
        "chat_history": chat_history
    }



@app.post("/reports/{report_id}/generate-ai-report")
def generate_ai_report(report_id: str):
    report = load_report(report_id)

    if report is None:
        return {
            "error": f"Report '{report_id}' not found."
        }

    prompt = build_report_prompt(report)

    ai_report = call_gemini(prompt)

    return {
        "report_id": report_id,
        "ai_report": ai_report
    }
