from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.v1.recommendation import router as recommendation_router
from src.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="SPVA Recommender", description="Recommendation of candidates API", license=lifespan)

app.include_router(recommendation_router, tags=["recommendation"])