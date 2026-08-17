from database import supabase

response = supabase.table("complaints").select("*").limit(5).execute()

print(response.data)

from database import supabase

response = supabase.table("complaints").select("*").limit(5).execute()

print(response.data)