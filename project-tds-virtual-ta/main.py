from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Link(BaseModel):
    url: str
    text: str

class Query(BaseModel):
    question: str
    image: Optional[str] = None

class Answer(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=Answer)
async def get_answer(query: Query):
    # Simple logic (you can enhance this)
    response = Answer(
        answer=f"Your question was: {query.question}. Please refer to the provided links.",
        links=[
            Link(
                url="https://discourse.onlinedegree.iitm.ac.in/",
                text="Discourse main page"
            )
        ]
    )
    return response
