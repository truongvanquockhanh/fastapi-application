from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine, Base
from app.api.routes import user, auth, project, bug, note
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting App...")
    Base.metadata.create_all(bind=engine)  # Create database tables
    yield
    print("Shutting Down App...")

app = FastAPI(lifespan=lifespan)

# Allow frontend origin
origins = [
    "http://localhost:3000",  # your React/TS frontend
    # add any additional origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # or ["*"] to allow all (not recommended for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/users", tags=["User"])
app.include_router(auth.router, prefix="/auths", tags=["Auth"])
app.include_router(project.router, prefix="", tags=["Project"])
app.include_router(bug.router, prefix="", tags=["Bug"])
app.include_router(note.router, prefix="", tags=["Note"])
