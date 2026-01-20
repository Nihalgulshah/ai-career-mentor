from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from agents.career_agent import analyze_with_ai

app = FastAPI()

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze_resume(
    resume_text: str = Form(...),
    interest: str = Form(None)
):
    try:
        result = await analyze_with_ai(resume_text, interest)
        return {"result": result}
    except Exception:
        return {
            "result": """
AI Career Analysis (Demo Mode)

Skill Gaps:
- Advanced Machine Learning
- Deep Learning fundamentals
- Model deployment (MLOps)

Suggested Career Paths:
- AI Engineer
- Machine Learning Engineer
- Data Scientist

Learning Roadmap:
- Strengthen Python for ML
- Learn PyTorch or TensorFlow
- Study deep learning concepts
- Build end-to-end AI projects

Project Ideas:
- Resume Analyzer using NLP
- AI Job Recommendation System
- Career Guidance Chatbot
"""
        }

