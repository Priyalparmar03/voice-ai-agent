# from stt.whisper_local import transcribe_audio
# from core.planner import plan_tasks
# from safety.validator import validate
# from tools.executor import execute

# def run_pipeline(file):
#     print("🔥 Step 1: Starting pipeline")

#     text = transcribe_audio(file)
#     print("📝 Transcribed:", text)

#     tasks = plan_tasks(text)
#     print("📋 Tasks:", tasks)

#     safe, msg = validate(tasks)
#     print("🔐 Safety:", safe)

#     if not safe:
#         return {"text": text, "tasks": tasks, "output": msg}

#     return {
#         "text": text,
#         "tasks": tasks,
#         "confirm": True
#     }

from stt.whisper_local import transcribe_audio
from core.planner import plan_tasks
from safety.validator import validate
from tools.executor import execute

def run_pipeline(file):
    print("🔥 Pipeline started")

    text = transcribe_audio(file)
    print("📝 Text:", text)

    tasks = plan_tasks(text)
    print("📋 Tasks:", tasks)

    safe, msg = validate(tasks)

    if not safe:
        return {
            "text": text,
            "tasks": tasks,
            "output": msg
        }

    return {
        "text": text,
        "tasks": tasks,
        "confirm": True
    }


def execute_tasks_after_confirm(data):
    print("⚙️ Executing:", data["tasks"])

    result = execute(data["tasks"])

    return {"output": result}