from pydantic import BaseModel
from typing import Optional

class MentorForm(BaseModel):
    token: str
    username: str