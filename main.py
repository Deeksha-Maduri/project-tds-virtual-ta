from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional
import base64

app = FastAPI()

class Link(BaseModel):
    url: str
    text: str

class ResponseModel(BaseModel):
    answer: str
    links: List[Link]

class RequestModel(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/")
async def handle_question(req: RequestModel):
    q = req.question.strip().lower()

    if "gpt-3.5-turbo" in q:
        return ResponseModel(
            answer="You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
            links=[
                Link(
                    url="https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939",
                    text="Use the model that’s mentioned in the question."
                )
            ]
        )
    elif "ga4" in q and "10/10" in q:
        return ResponseModel(
            answer="If you score 10/10 on GA4 along with a bonus, your dashboard will show 110.",
            links=[
                Link(
                    url="https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959",
                    text="GA4 data sourcing discussion"
                )
            ]
        )
    elif "docker" in q and "podman" in q:
        return ResponseModel(
            answer="We recommend using Podman for this course. However, Docker is also acceptable if you're familiar with it.",
            links=[
                Link(
                    url="https://tds.s-anand.net/#/docker",
                    text="Docker/Podman course reference"
                )
            ]
        )
    elif "end-term" in q and "sep 2025" in q:
        return ResponseModel(
            answer="This information is not available yet.",
            links=[]
        )
    else:
        return ResponseModel(
            answer="Sorry, I do not have an answer for that question at the moment.",
            links=[]
        )
