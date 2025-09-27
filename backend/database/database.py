from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# 🔹 URL para asincronía con SQLite
DATABASE_URL = "sqlite+aiosqlite:///./Chinook_Sqlite.sqlite"

# 🔹 Engine asincrónico
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# 🔹 Creador de sesiones asincrónicas
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# 🔹 Crear tablas de forma asincrónica
async def crear_db_y_tablas():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# 🔹 Dependencia para obtener la sesión en FastAPI
async def get_session():
    async with async_session() as session:
        yield session