from typing import TypedDict
from langgraph.graph import StateGraph,START,END

class State(TypedDict):
    question : str
    attempts : int
    ready : bool
    