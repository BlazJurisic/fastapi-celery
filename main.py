from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
import celery_worker as worker

app = FastAPI()

@app.post("/ex1")
def run_task(data=Body(...)):
    s3_path = int(data["s3_path"])
    task = worker.get_transcript(s3_path, 1, 2, 3)
    return JSONResponse({"Result": task.get()})
