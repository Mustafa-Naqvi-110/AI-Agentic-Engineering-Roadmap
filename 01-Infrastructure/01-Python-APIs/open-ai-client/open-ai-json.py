import os
import time
from openai import OpenAI, RateLimitError, APIError
from utils.json_utils import parse_json_safely

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

system_prompt = """
You are a JSON generator.
Return ONLY valid JSON.
"""

user_prompt = """
Return data in this schema:
{
  "task": string,
  "difficulty": number,
  "tools": [string]
}
"""

def call_openai_json(retries=3):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini", # You can use your preferred model
                temperature=0,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return parse_json_safely(response.choices[0].message.content)

        except RateLimitError:
            time.sleep(2 ** attempt)
        except APIError as e:
            raise RuntimeError(e)

    raise RuntimeError("OpenAI failed after retries")


if __name__ == "__main__":
    print(call_openai_json())
