import asyncpg
import asyncio

# DB_URL: str = "postgresql://teste_user:ollpemjnlwsg@db-57878.dc-sp-1.absamcloud.com:11087/teste"
# DATABASE_URL="postgresql://postgres.srecyickytvjgkwetayb:[testeteste]@aws-0-us-east-1.pooler.supabase.com:6543/postgres?pgbouncer=true"
DATABASE_URL = "postgresql://postgres.tascqincqdsjvmdjdwnh:123456@aws-0-us-east-2.pooler.supabase.com:5432/postgres"


async def test_connection():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        print("✅ Conexão bem-sucedida!")
        await conn.close()
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")


asyncio.run(test_connection())