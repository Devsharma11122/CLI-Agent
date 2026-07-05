from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROJECT_ROOT = Path(__file__).parent

WORKSPACE = PROJECT_ROOT / "workspace"

WORKSPACE.mkdir(exist_ok=True)

MODEL = os.getenv("MODEL", "gpt-4.1")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)