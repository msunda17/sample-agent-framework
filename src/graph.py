from langgraph.graph import StateGraph, END
from src.state import SystemState


def explore_node(state: SystemState) -> dict:
    # TODO: Implement MARTI-MARS tree search
    pass


def update_policy_node(state: SystemState) -> dict:
    # TODO: Implement MARTI-MARS reinforcement learning update
    pass


workflow = StateGraph(SystemState)
workflow.add_node("explore", explore_node)
workflow.add_node("update_policy", update_policy_node)

workflow.set_entry_point("explore")
workflow.add_edge("explore", "update_policy")
workflow.add_edge("update_policy", END)

app = workflow.compile()
