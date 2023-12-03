from typing import List

from pydantic import BaseModel


class QuestionCreateRequest(BaseModel):
    question: str


class QuestionAnswer(BaseModel):
    answer: str
    context: List[str]
