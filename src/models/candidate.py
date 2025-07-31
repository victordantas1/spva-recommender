from typing import Optional, List

from odmantic import Field, Model
from pydantic import EmailStr


class Candidate(Model):
    user_id: int
    first_name: str
    last_name: str
    email: EmailStr
    resume_path: str
    document: str
    tokens: Optional[List[str]] = None
    tokens_clean: Optional[List[str]] = None
    tokens_ner: Optional[List[str]] = None

    model_config = {
        "collection": "user_app"
    }