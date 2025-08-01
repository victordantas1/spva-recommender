from typing import List

from beanie.odm.operators.find.comparison import In

from models import Candidate, CandidateTextView


class CandidateRepository:
    def __init__(self):
        pass

    async def get_candidates(self, candidates_list) -> List[CandidateTextView]:
        candidates = await Candidate.find(In(Candidate.user_id, candidates_list)).project(CandidateTextView).to_list()
        return candidates