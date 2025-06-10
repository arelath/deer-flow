from langgraph.graph import END, START, StateGraph

from .state import StoryState
from .outline_planner_node import outline_planner_node
from .draft_writer_node import draft_writer_node
from .critique_node import critique_node
from .editor_node import editor_node


def start_node(state: StoryState):
    return "draft_writer" if state.get("outline") else "outline_planner"


def build_graph():
    builder = StateGraph(StoryState)
    builder.add_node("outline_planner", outline_planner_node)
    builder.add_node("draft_writer", draft_writer_node)
    builder.add_node("critique_draft", critique_node)
    builder.add_node("editor", editor_node)
    builder.add_conditional_edges(
        START,
        start_node,
        ["outline_planner", "draft_writer"],
    )
    builder.add_edge("outline_planner", "draft_writer")
    builder.add_edge("draft_writer", "critique_draft")
    builder.add_edge("critique_draft", "editor")
    builder.add_edge("editor", END)
    return builder.compile()


workflow = build_graph()
