from config import SUPABASE_URL, SUPABASE_KEY, MODEL_DIR

print("URL:", SUPABASE_URL)
print("KEY:", SUPABASE_KEY[:20] + "...")
print("MODEL_DIR:", MODEL_DIR)

from config import SUPABASE_URL, SUPABASE_KEY

print("URL:", SUPABASE_URL)
print("KEY:", SUPABASE_KEY)
print("Length:", len(SUPABASE_KEY))

from config import SUPABASE_URL, SUPABASE_KEY

print("URL:", SUPABASE_URL)
print("KEY Length:", len(SUPABASE_KEY))
print("KEY:", SUPABASE_KEY[:30] + "...")

from config import SUPABASE_URL, SUPABASE_KEY

print(SUPABASE_URL)
print(SUPABASE_KEY)
print(len(SUPABASE_KEY))