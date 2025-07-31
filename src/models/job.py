from typing import List, Optional

from odmantic import Model

from enums import CategoryEnum

class Job(Model):
    job_id: int
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

    model_config = {
        "collection": "job"
    }