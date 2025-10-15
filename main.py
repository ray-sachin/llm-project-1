import code
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from pydantic import BaseModel
from llm_utils import generate_code_from_brief, save_code_to_file

app = FastAPI()

class Attachment(BaseModel):
    name: str
    url: str

# Define what the incoming JSON should look like
class AppRequest(BaseModel):
    email: str
    secret: str
    task: str
    round: int
    nonce: str
    brief: str
    evaluation_url: str
    attachments: Optional[List[Attachment]] = None

# Your chosen secret (change this to your own!)
YOUR_SECRET = "sachin"

@app.post("/generate-app")
async def generate_app(request: AppRequest):
    if request.secret != YOUR_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")
    app_code = generate_code_from_brief(request.brief)
    save_code_to_file(app_code, "index.html")
    return {"status": "received", "generated_code": code[:500]}