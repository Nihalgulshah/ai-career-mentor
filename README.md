# AI Career Mentor

AI Career Mentor is a full-stack generative AI web application that analyzes resumes and career interests to provide structured career guidance, skill gap analysis, learning roadmaps, and project recommendations.

The system is built using Pydantic AI concepts on the backend and provides a simple web interface for users.

---

## Live Deployment

Frontend:
https://ai-career-mentor-frontend.vercel.app

Backend API:
https://ai-career-mentor-backend-gdwi.onrender.com

---

## Features

- Resume analysis based on user input
- Skill gap identification
- Suggested career paths
- Personalized learning roadmap
- Project ideas for career development

---

## Technology Stack

### Frontend
- React
- Vite
- JavaScript
- HTML
- CSS

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn

### Deployment
- Frontend deployed on Vercel
- Backend deployed on Render

---

## Application Workflow

1. User enters resume text and career interests.
2. Frontend sends the data to the backend API.
3. Backend processes the request using AI logic.
4. Career analysis is returned and displayed on the frontend.

---

## API Details

Endpoint:
POST /analyze

Request Body (application/x-www-form-urlencoded):

resume_text=<resume text>
interest=<career interest>

Response:
A structured career analysis containing skill gaps, career paths, learning roadmap, and project ideas.

---

## Project Structure

ai-career-mentor/
├── backend/
│   ├── main.py
│   ├── agents/
│   │   └── career_agent.py
│   ├── schemas/
│   │   └── resume_schema.py
│   └── requirements.txt
└── frontend/
    ├── src/
    ├── package.json
    └── vite.config.js

---
