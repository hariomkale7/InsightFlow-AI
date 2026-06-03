import os
import shutil

from fastapi import FastAPI, UploadFile, File

from src.pipeline import run_insightflow_pipeline

from fastapi.staticfiles import StaticFiles


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

    report["cleaned_df"] = report["cleaned_df"].to_dict(orient="records")

    report = convert_numpy_types(report)

    return report


