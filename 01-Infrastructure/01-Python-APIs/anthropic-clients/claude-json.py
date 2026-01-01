import os
import time
import anthropic
from open_ai_client.open_ai_json import user_prompt
from utils.json_utils import parse_json_safely

client = anthropic.Anthropic(
    api_key=os.getenv("YOUR_ANTHROPIC_API_KEY"))

system_prompt = "You are a JSON generator. Return ONLY valid JSON."

user_prompt = """
Return data in this schema:
{
  "model": string,
  "use_case": string,
  "confidence": number
}
"""

def call_claude_json(retries=3):
    for attempt in range(retries):
        try:
            message = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                temperature=0,
                max_tokens=300,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}]
            )
            return parse_json_safely(message.content[0].text)

        except anthropic.RateLimitError:
            time.sleep(2 ** attempt)
        except anthropic.APIError as e:
            raise RuntimeError(e)

    raise RuntimeError("Claude failed after retries")


if __name__ == "__main__":
    print(call_claude_json())
