import asyncio

from odmantic import AIOEngine

from config import config
from models.candidate import Candidate
from models.job import Job
from services.embedding_model import EmbeddingModelTransformer


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


if __name__ == "__main__":
    asyncio.run(main())