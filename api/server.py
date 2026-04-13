from fastapi import FastAPI, UploadFile, File
from core.orchestrator import run_pipeline, execute_tasks_after_confirm

app = FastAPI()

@app.post("/process")
async def process(file: UploadFile = File(...)):
    return run_pipeline(file.file)

@app.post("/execute")
async def execute(data: dict):
    return execute_tasks_after_confirm(data)