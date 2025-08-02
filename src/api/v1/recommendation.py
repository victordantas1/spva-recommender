from typing import Annotated, List, Tuple

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from torch import Tensor

from src.schemas.candidate_schema import CandidateOut
from src.models.job import JobTextView
from src.dependencies import get_recommendation_service
from src.services.recommendation_service import RecommendationService

router = APIRouter(tags=["recommendation"], prefix="/recommendation")

class RecommendationQueryParams(BaseModel):
    candidates_list: List[int]
    top_k: int

@router.get("/recommendation/{job_id}", response_model=List[CandidateOut])
async def recommendation(job_id: int, query_params: Annotated[RecommendationQueryParams, Query()], recommendation_service: Annotated[RecommendationService, Depends(get_recommendation_service)]):
    candidates = await recommendation_service.get_recommendations(job_id, query_params.candidates_list, query_params.top_k)
    return candidates
