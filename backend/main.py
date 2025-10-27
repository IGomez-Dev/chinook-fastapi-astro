from fastapi import FastAPI
from database import crear_db_y_tablas
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routers import *

origins = [
    "http://localhost",
    "http://localhost:4321", # Puerto de desarrollo de Astro (Común)
    "http://127.0.0.1:4321", # Por si acaso
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await crear_db_y_tablas()
    yield

app = FastAPI(title='API Chinook', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(album_router)
app.include_router(artist_router)
app.include_router(customer_router)
app.include_router(employee_router)
app.include_router(genre_router)
app.include_router(invoice_line_router)
app.include_router(invoice_router)
app.include_router(media_type_router)
app.include_router(playlist_router)
app.include_router(playlist_track_router)
app.include_router(track_router)

@app.get('/')
async def root():
  return {'message': 'API conectada con SQLite'}
