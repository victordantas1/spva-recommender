from typing import List
from odmantic import query
from models.candidate import Candidate


class CandidateRepository:
    def __init__(self, engine):
        self.engine = engine

    async def get_candidates(self, candidates_list) -> List[Candidate]:
        candidates = await self.engine.find(Candidate, Candidate.user_id.in_(candidates_list))
        return candidates