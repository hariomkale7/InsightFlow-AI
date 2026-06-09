import os
import json


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


def save_report(report, output_folder="reports"):
    os.makedirs(output_folder, exist_ok=True)

    report_count = len(os.listdir(output_folder)) + 1

    report_id = f"report_{report_count:03d}"
    file_name = report_id + ".json"

    report_path = os.path.join(output_folder, file_name)

    report = convert_numpy_types(report)

    with open(report_path, "w") as file:
        json.dump(report, file, indent=4)

    return {
        "report_id": report_id,
        "report_path": report_path.replace("\\", "/")
    }

def load_report(report_id, reports_folder="reports"):
    file_path = f"{reports_folder}/{report_id}.json"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:
        report = json.load(file)

    return report


def save_chat_message(report_id, role, message):
    chat_file = f"reports/{report_id}_chat.json"

    chat_history = []

    if os.path.exists(chat_file):
        with open(chat_file, "r") as file:
            chat_history = json.load(file)

    chat_history.append(
        {
            "role": role,
            "message": message
        }
    )

    with open(chat_file, "w") as file:
        json.dump(
            chat_history,
            file,
            indent=4
        )


def load_chat_history(report_id):
    chat_file = f"reports/{report_id}_chat.json"

    if not os.path.exists(chat_file):
        return []

    with open(chat_file, "r") as file:
        return json.load(file)

