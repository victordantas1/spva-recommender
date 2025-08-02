from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from loguru import logger
from src.config.config import config
from src.repositories.job_repository import JobRepository
from src.repositories.candidate_repository import CandidateRepository
from src.services.recommendation_service import RecommendationService
from src.services.embedding_model import EmbeddingModelBase, EmbeddingModelTransformer

@lru_cache()
def get_job_repository() -> JobRepository:
    return JobRepository()

@lru_cache()
def get_candidate_repository() -> CandidateRepository:
    return CandidateRepository()

@lru_cache()
def get_embedding_model() -> EmbeddingModelBase:
    logger.info("--- LOADING EMBEDDING MODEL ---")
    return EmbeddingModelTransformer(config=config)

@lru_cache()
def get_recommendation_service(
        job_repository: Annotated[JobRepository, Depends(get_job_repository)],
        candidate_repository: Annotated[CandidateRepository, Depends(get_candidate_repository)],
        embedding_model: Annotated[EmbeddingModelBase, Depends(get_embedding_model)]
) -> RecommendationService:
    logger.info("--- CREATING RECOMMENDATION SERVICE ---")
    return RecommendationService(job_repository, candidate_repository, embedding_model)