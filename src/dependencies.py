from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from loguru import logger
from .config import config
from .repositories import JobRepository, CandidateRepository
from .services import RecommendationService
from .services.embedding_model import EmbeddingModelBase, EmbeddingModelTransformer

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