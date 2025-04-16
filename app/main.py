from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine, Base
from app.api.routes import user, auth, project, bug, note
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting App...")
    Base.metadata.create_all(bind=engine)  # Create database tables
    yield
    print("Shutting Down App...")

app = FastAPI(lifespan=lifespan)

# Allow frontend origin
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in origins if origin.strip()],            # or ["*"] to allow all (not recommended for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/users", tags=["User"])
app.include_router(auth.router, prefix="/auths", tags=["Auth"])
app.include_router(project.router, prefix="", tags=["Project"])
app.include_router(bug.router, prefix="", tags=["Bug"])
app.include_router(note.router, prefix="", tags=["Note"])
