from typing import List, Optional

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel

from src.enums.category_enum import CategoryEnum

class Job(Document):
    job_id: Indexed(int, index_type=pymongo.ASCENDING)
    user_id: int
    title: str
    description: str
    position: str
    category: CategoryEnum
    create_date: int
    responsibilities: str
    requirements: str
    level: str
    contract_type: str
    schedule: str
    salary_range: str
    company: str
    document: str
    tokens: Optional[List[str]] = None
    tokens_clean: Optional[List[str]] = None
    tokens_ner: Optional[List[str]] = None

    class Settings:
        name = 'job'

class JobTextView(BaseModel):
    job_id: int
    document: str
    tokens: Optional[List[str]] = None
    tokens_clean: Optional[List[str]] = None
    tokens_ner: Optional[List[str]] = None