from pydantic import BaseModel

from src.models.candidate import CandidateTextView


class CandidateOut(BaseModel):
    candidate: CandidateTextView
    score: float