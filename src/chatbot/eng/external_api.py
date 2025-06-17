import os
import openai
from dotenv import load_dotenv

# โหลดค่า .env ถ้ามี (ไม่จำเป็น แต่ช่วยใน dev)
load_dotenv()

# ดึง API key จาก environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

# ตั้งค่า API key ให้ openai
openai.api_key = OPENAI_API_KEY

def call_openai(prompt: str, model: str = "gpt-4o") -> tuple[str | None, str | None]:
    """
    เรียก OpenAI Chat Completion API
    คืนค่า (response_text, error)
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"], None
    except Exception as e:
        return None, str(e)

# การใช้
# from external_api import call_openai
# prompt = "ช่วยสรุปงบกำไรขาดทุนบริษัท A ให้หน่อย"
# response, error = call_openai(prompt)