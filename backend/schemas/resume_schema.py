from pydantic import BaseModel

class ResumeInput(BaseModel):
    resume_text: str
    interest: str | None = None

