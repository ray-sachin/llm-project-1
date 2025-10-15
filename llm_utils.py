from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("AIPIPE_TOKEN"),
    base_url="https://aipipe.org/openai/v1"  # This is critical for aiPipe!
)

def generate_code_from_brief(brief: str) -> str:
    prompt = (
        f"You are an expert developer. Write minimal but working code as described: {brief}\n"
        "Respond with only source code."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1200
    )
    # In v1+ the completion object returns message content here:
    return response.choices[0].message.content.strip()

def save_code_to_file(code: str, filename: str = "index.html"):
    # Remove code fences if present from LLM output (e.g., ```
    if code.startswith("```"):
        code = "\n".join(line for line in code.splitlines() if not line.startswith("```"))
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)