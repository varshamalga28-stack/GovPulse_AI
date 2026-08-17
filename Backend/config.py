from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

MODEL_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.getenv("MODEL_DIR")
    )
)