from fastapi import FastAPI
from database import crear_db_y_tablas
from contextlib import asynccontextmanager
from routers import artist_router, album_router, customer_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await crear_db_y_tablas()
    yield

app = FastAPI(title='API Chinook', lifespan=lifespan)

app.include_router(artist_router.router)
app.include_router(album_router.router)
app.include_router(customer_router.router)

@app.get('/')
async def root():
  return {'message': 'API conectada con SQLite'}
