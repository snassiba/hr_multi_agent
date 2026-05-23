from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from agents.hr_agent import (
    select_tool,
    answer_hr_question
)


# Etat partagé entre les nodes
class HRState(TypedDict):
    question: str
    selected_tool: str
    response: str
    validated: bool


# Node 1 : Router
def router_node(state: HRState):

    question = state["question"]

    tool = select_tool(question)

    return {
        "selected_tool": tool.name
    }


# Node 2 : Generator
def generator_node(state: HRState):

    question = state["question"]

    response = answer_hr_question(question)

    return {
        "response": response
    }


# Node 3 : Human validation
def human_validation_node(state: HRState):

    print("\n===== REPONSE PROPOSEE =====\n")

    print(state["response"])

    validation = input("\nValider cette réponse ? oui/non : ")

    validated = validation.lower() == "oui"

    return {
        "validated": validated
    }


# Construction du graph
workflow = StateGraph(HRState)

workflow.add_node("router", router_node)

workflow.add_node("generator", generator_node)

workflow.add_node("human_validation", human_validation_node)

# Flux
workflow.set_entry_point("router")

workflow.add_edge("router", "generator")

workflow.add_edge("generator", "human_validation")

workflow.add_edge("human_validation", END)

# Compilation
app = workflow.compile()