import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import SYSTEM_PROMPT


load_dotenv()
api_key: str | None = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set! Please edit .env and add your API key.")

parser: argparse.ArgumentParser = argparse.ArgumentParser(description="AI Agent")
parser.add_argument("prompt", type=str, help="Given prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args: argparse.Namespace = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
)

prompt_tokens: int | None = (
    response.usage_metadata.prompt_token_count if response.usage_metadata else None
)
response_tokens: int | None = (
    response.usage_metadata.candidates_token_count if response.usage_metadata else None
)

if args.verbose:
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

print(response.text)
