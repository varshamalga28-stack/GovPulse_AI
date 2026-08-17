from database import supabase

response = supabase.table("complaints").select("*").limit(1).execute()

print(response.data)