from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS configuration (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-career-mentor-frontend.vercel.app",
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
        # 🔹 Demo / fallback AI response
        return {
            "result": f"""
AI Career Analysis (Demo Mode)

Resume Summary:
{resume_text}

Career Interest:
{interest or "Not specified"}

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

    except Exception:
        return {
            "result": "AI service temporarily unavailable. Please try again later."
        }

