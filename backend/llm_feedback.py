import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"


def generate_feedback(resume_text: str, jd_text: str, match_score: float) -> str:
    """
    Generates resume feedback using a local open-source LLM via Ollama.
    Uses trimmed input to avoid memory/context errors.
    """

    # 🔹 Limit text size (IMPORTANT)
    resume_snippet = resume_text[:1500]
    jd_snippet = jd_text[:800]

    prompt = f"""
    From the resume text below, list ONLY 3 important skills that are
    missing compared to the job description.
    
    Resume(partial):
    {resume_snippet}
    
    Job Description:
    {jd_snippet}
    
    Rules:
    - Respond ONLY with a bullet list
    - Maximum 3 bullet points
    - Do NOT repeat resume text
    - Do NOT explain
    
    """


    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.4
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=90)
        response.raise_for_status()
        return response.json().get("response", "No feedback generated.")

    except Exception as e:
        return (
            "AI feedback could not be generated due to model limits.\n"
            "Try again or reduce input size.\n\n"
            f"Details: {str(e)}"
        )
