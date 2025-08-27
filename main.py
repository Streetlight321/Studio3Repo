from supabase import create_client, Client
import os
import pandas as pd
import dotenv

dotenv.load_dotenv()
SUPABASE_URL: str = os.getenv("SUPA_URL")
SUPABASE_KEY: str = os.getenv("SUPA_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

data = supabase.table("shows").select("*").execute().data
df = pd.DataFrame(data)

print(df.head())