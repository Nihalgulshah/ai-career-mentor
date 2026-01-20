from pydantic_ai import Agent

agent = Agent(
    model="openrouter:meta-llama/llama-3.1-8b-instruct",
    system_prompt="""
You are an AI Career Mentor.
Analyze the resume and career interest.
Provide:
1. Skill gaps
2. Suitable career paths
3. Learning roadmap
4. Project ideas
"""
)

async def analyze_with_ai(resume: str, interest: str | None):
    prompt = f"""
Resume:
{resume}

Career Interest:
{interest}
"""
    result = await agent.run(prompt)
    return result.output_text

