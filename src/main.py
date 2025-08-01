import asyncio

from beanie import init_beanie, Document, Indexed
from beanie.odm.operators.find.comparison import In
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import AsyncMongoClient

from config import config
from models import Job, Candidate
from repositories import JobRepository, CandidateRepository
from services.embedding_model import EmbeddingModelTransformer
from services.recommendation_service import RecommendationService

async def main_recommendation_service():
    job_repository = JobRepository()
    candidate_repository = CandidateRepository()
    embedding_model = EmbeddingModelTransformer(config)

    job_id = 21
    candidate_ids = [3, 4]
    recommendation_service = RecommendationService(job_repository, candidate_repository, embedding_model)
    recommendations = await recommendation_service.get_recommendations(job_id, candidate_ids, 10)

    print(recommendations)

async def main_test_repository():
    job_repository = JobRepository()
    candidate_repository = CandidateRepository()
    job_id = 21
    candidate_ids = [3, 4]

    job = await job_repository.get_job(job_id)
    candidates = await candidate_repository.get_candidates(candidate_ids)

    print(f"Job {job_id}:\n{job}")
    print(f"Candidates {candidate_ids}:\n{candidates}")

async def init():
    client = AsyncIOMotorClient("mongodb://localhost:27017/spva")
    await init_beanie(database=client.get_database(), document_models=[Job, Candidate])
    await main_test_repository()

if __name__ == "__main__":
    asyncio.run(init())