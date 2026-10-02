from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app=FastAPI()
class SummarizeRequest(BaseModel):
    text: str
    length: str = "medium"

@app.get("/")
def chat():
  return "hello world"

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    response = agent.invoke({
        "messages": [{
            "role": "user",
            "content": (
                f"Summarize this text in a {request.length} format:\n"
                f"{request.text}"
            )
        }]
    })

    return {
        "summary": response["messages"][-1].content
    }
