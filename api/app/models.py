from pydantic import BaseModel
from typing import Optional

class MentorForm(BaseModel):
    my_node_id: str
    mentor_username: str
    gh_tok: str