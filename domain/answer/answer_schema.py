import datetime
from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):
    # id: int
    content: str
    # create_date: datetime
    # question_id: int
    @field_validator('content')
    def not_empyt(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime