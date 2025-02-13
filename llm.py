from fastapi import FastAPI
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from graph import flow
from context import context_retreival
load_dotenv()

app = FastAPI()
@app.get("/")
def send_response(conversation_id: str,query:str):
    config = {"configurable": {"thread_id": f"{conversation_id}"}}
    input_messages = [HumanMessage(query)]
    context =  context_retreival(query=query)
    output = flow.invoke(input={"messages": input_messages,"context":context },config=config)
    return output["messages"][-1]