# import subprocess
# import json

# def plan_tasks(text):
#     prompt = f"""
#     Convert user input into structured JSON tasks.

#     Input: {text}

#     Allowed actions:
#     - create_file
#     - write_code
#     - summarize
#     - chat

#     Output format:
#     {{
#       "tasks": [
#         {{"action": "create_file", "filename": "file.txt"}}
#       ]
#     }}
#     """

#     try:
#         result = subprocess.run(
#           ["ollama", "run", "phi"],
#           input=prompt,
#           capture_output=True,
#           text=True,
#           encoding="utf-8",     # ✅ FIX
#           errors="ignore"       # ✅ PREVENT CRASH
#         )

#         output = result.stdout.strip()

#         # extract JSON safely
#         start = output.find("{")
#         end = output.rfind("}") + 1
#         json_str = output[start:end]

#         return json.loads(json_str)["tasks"]

#     except Exception as e:
#         return [{"action": "chat", "input": text}]


import subprocess
import json

def plan_tasks(text):
    text_lower = text.lower()

    # ✅ RULE-BASED INTENT (STRONG + RELIABLE)
    if "create" in text_lower and "file" in text_lower:
        return [{
            "action": "create_file",
            "filename": "test.txt"
        }]

    if "write code" in text_lower or "python" in text_lower:
        return [{
            "action": "write_code",
            "filename": "code.py",
            "content": "print('Hello World')"
        }]

    if "summarize" in text_lower:
        return [{
            "action": "summarize",
            "input": text
        }]

    # 🔥 FALLBACK → LLM (phi)
    try:
        result = subprocess.run(
            ["ollama", "run", "phi"],
            input=text,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        return [{
            "action": "chat",
            "input": result.stdout.strip()
        }]

    except:
        return [{
            "action": "chat",
            "input": text
        }]