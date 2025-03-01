from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('api-key')

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Set it in your environment.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

def get_gemini_response(text: str) -> str:
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate", response_model=QueryResponse)

def generate_response(request: QueryRequest):
    return QueryResponse(response=get_gemini_response(request.query))
