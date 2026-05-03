from typing import TypedDict, Sequence, Annotated
import operator
from langchain_core.messages import BaseMessage
import torch

class SystemState(TypedDict):
    """Legacy LangGraph state for production routing."""
    messages: Annotated[Sequence[BaseMessage], operator.add]
    current_code_candidate: str
    global_policy_weights: torch.Tensor 
    latest_reward: float
