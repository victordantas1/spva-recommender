from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.models.candidate import Candidate
from src.models.job import Job
from src.api.v1.recommendation import router as recommendation_router
from src.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db([Job, Candidate])
    yield

app = FastAPI(title="SPVA Recommender", description="Recommendation of candidates API", lifespan=lifespan)

app.include_router(recommendation_router, tags=["recommendation"])