import subprocess

def summarize(text):
    result = subprocess.run(
        ["ollama", "run", "phi"],
        input=f"Summarize:\n{text}",
        capture_output=True,
        text=True
    )
    return result.stdout.strip()