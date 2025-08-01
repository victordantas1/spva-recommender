from typing import Optional, List

import pymongo
from beanie import Document, Indexed
from pydantic import EmailStr, BaseModel


class Candidate(Document):
    user_id: Indexed(int, index_type=pymongo.ASCENDING)
    first_name: str
    last_name: str
    email: EmailStr
    resume_path: str
    document: str
    tokens: Optional[List[str]] = None
    tokens_clean: Optional[List[str]] = None
    tokens_ner: Optional[List[str]] = None

    class Settings:
        name = 'user_app'

class CandidateTextView(BaseModel):
    user_id: int
    document: str
    tokens: Optional[List[str]] = None
    tokens_clean: Optional[List[str]] = None
    tokens_ner: Optional[List[str]] = None