from typing import Optional, List

from odmantic import Field, Model
from pydantic import EmailStr


class Candidate(Model):
    user_id: int
    first_name: str
    last_name: str
    email: EmailStr
    table: str
    document: str
    tokens: Optional[List[str]] = None
    tokens_clean: Optional[List[str]] = None
    tokens_ner: Optional[List[str]] = None

    model_config = {
        "collection": "user_app"
    }

    def __repr__(self):
        return (f"user_id: {self.user_id}, "
                f"first_name: {self.first_name}, "
                f"last_name: {self.last_name}, "
                f"email: {self.email}"
                f"table: {self.table}, "
                f"document: {self.document}, "
                f"tokens: {self.tokens}, "
                f"tokens_clean: {self.tokens_clean}, "
                f"tokens_ner: {self.tokens_ner}, ")