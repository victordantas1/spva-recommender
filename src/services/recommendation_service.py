from typing import List, Tuple

from torch import Tensor

from models import Job, Candidate
from repositories import JobRepository, CandidateRepository
from services.embedding_model import EmbeddingModelBase


class RecommendationService:
    def __init__(self, job_repository: JobRepository, candidate_repository: CandidateRepository, embedding_model: EmbeddingModelBase):
        self.job_repository = job_repository
        self.candidate_repository = candidate_repository
        self.embedding_model = embedding_model

    async def get_job_and_candidates(self, job_id, candidates_list) -> (Job, List[Candidate]):
        job = await self.job_repository.get_job(job_id)
        candidates = await self.candidate_repository.get_candidates(candidates_list)
        return job, candidates

    async def get_recommendations(self, job_id, candidates_list, top_k) -> List[Tuple[Candidate, Tensor]]:
        job, candidates = await self.get_job_and_candidates(job_id, candidates_list)

        cosine_similarity_list = []

        for candidate in candidates:
            job_emb = self.embedding_model.encode(job.document)
            candidate_emb = self.embedding_model.encode(candidate.document)
            cosine_similarity_list.append((candidate, self.embedding_model.cosine_similarity(job_emb, candidate_emb)))

        cosine_similarity_list = sorted(cosine_similarity_list, key=lambda x: x[1], reverse=True)[:top_k]

        return cosine_similarity_list





