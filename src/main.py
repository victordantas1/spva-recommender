from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.models.candidate import Candidate
from src.models.job import Job
from src.api.v1.recommendation import router as recommendation_router
from src.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db([Job, Candidate])
    yield

app = FastAPI(title="SPVA Recommender", description="Recommendation of candidates API", lifespan=lifespan)

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommendation_router, tags=["recommendation"])