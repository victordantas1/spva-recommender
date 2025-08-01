import asyncio

from odmantic import AIOEngine

from config import config
from models.candidate import Candidate
from models.job import Job
from repositories import JobRepository, CandidateRepository
from services.embedding_model import EmbeddingModelTransformer
from services.recommendation_service import RecommendationService


async def main():
    engine = AIOEngine(database='spva')
    candidate_id = 3
    job_id = 21
    candidate = await engine.find_one(Candidate, Candidate.user_id == candidate_id)
    job = await engine.find_one(Job, Job.job_id == job_id)
    print(f"Candidate {candidate_id}:\n{candidate}")
    print(f"Job {job_id}:\n{job}")

    print("-" * 5, "Test Embedding Model", "-" * 5)
    model = EmbeddingModelTransformer(config)
    model.load_model()
    candidate_emb = model.encode(candidate.document)
    job_emb = model.encode(job.document)
    print(f"Candidate {candidate_id}:\n{candidate_emb}")
    print(f"Job {job_id}:\n{job_emb}")
    print(f"Cosine Similarity: {model.cosine_similarity(job_emb, candidate_emb)}")

async def main_test_repository():
    engine = AIOEngine(database='spva')
    job_repository = JobRepository(engine)
    candidate_repository = CandidateRepository(engine)
    job_id = 21
    candidate_ids = [3, 4]
    job = await job_repository.get_job(job_id)
    candidates = await candidate_repository.get_candidates(candidate_ids)
    print(f"Job {job_id}:\n{job}")
    print(f"Candidates {candidate_ids}:\n{candidates}")

async def main_recommendation_service():
    engine = AIOEngine(database='spva')
    job_repository = JobRepository(engine)
    candidate_repository = CandidateRepository(engine)
    embedding_model = EmbeddingModelTransformer(config)
    job_id = 21
    candidate_ids = [3, 4]
    recommendation_service = RecommendationService(job_repository, candidate_repository, embedding_model)

    recommendations = await recommendation_service.get_recommendations(job_id, candidate_ids, 10)

    print(recommendations)

if __name__ == "__main__":
    asyncio.run(main_recommendation_service())