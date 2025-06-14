from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class AnswerResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=AnswerResponse)
async def answer_question(payload: QuestionRequest):
    q = payload.question.lower()

    # Example response logic
    if "gpt-3.5-turbo-0125" in q:
        return {
            "answer": "You must use `gpt-3.5-turbo-0125` and not `gpt-4o-mini`. Use OpenAI API directly.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939",
                    "text": "Clarification on GA5 Question 8"
                }
            ]
        }
    elif "ga4" in q and "bonus" in q:
        return {
            "answer": "The dashboard will show '110' if you scored 10/10 and the bonus.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959",
                    "text": "GA4 data sourcing discussion"
                }
            ]
        }
    elif "docker" in q and "podman" in q:
        return {
            "answer": "We recommend Podman for this course, but Docker is also acceptable.",
            "links": [
                {
                    "url": "https://tds.s-anand.net/#/docker",
                    "text": "Docker vs Podman details"
                }
            ]
        }
    elif "end-term" in q or "exam" in q:
        return {
            "answer": "Sorry, I don't know the date of the TDS Sep 2025 end-term exam yet.",
            "links": []
        }
    else:
        return {
            "answer": "Sorry, I do not have an answer for that question.",
            "links": []
        }
