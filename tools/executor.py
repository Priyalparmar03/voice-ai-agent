from tools.file_manager import create_file, write_file
from nlp.summarizer import summarize

def execute(tasks):
    results = []

    for t in tasks:
        try:
            if t["action"] == "create_file":
                results.append(create_file(t["filename"]))

            elif t["action"] == "write_code":
                results.append(write_file(t["filename"], t["content"]))

            elif t["action"] == "summarize":
                results.append(summarize(t["input"]))

            else:
                results.append("Chat response")

        except Exception as e:
            results.append(f"Error: {str(e)}")

    return results