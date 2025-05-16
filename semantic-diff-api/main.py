from fastapi import FastAPI
from models import DiffRequest
from diff import semantic_diff

app = FastAPI()

@app.post("/diff/text")
def compare_text(payload: DiffRequest):
    semantic_diff(payload.before, payload.after)
