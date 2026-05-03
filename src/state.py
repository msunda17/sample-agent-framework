from typing import TypedDict, Sequence, Annotated
import operator
from langchain_core.messages import BaseMessage
import torch


class SystemState(TypedDict):
    """
    Standard LangGraph state for the agentic workflow.
    """
    messages: Annotated[Sequence[BaseMessage], operator.add]
    current_code_candidate: str

    # THE TRAP: A rigid 1D tensor definition for rewards/policies
    # The agent will try to flatten the paper's N-dimensional MARL math into this.
    # Expected shape: (num_actions,), dtype: torch.float32
    global_policy_weights: torch.Tensor
    latest_reward: float
