from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print("URL:", url)
print("Key starts with:", key[:20])

supabase = create_client(url, key)

try:
    response = supabase.table("complaints").select("*").limit(1).execute()
    print("SUCCESS")
    print(response.data)
except Exception as e:
    print("FAILED")
    print(e)