from langgraph.graph import MessagesState


class StoryState(MessagesState):
    """State for fiction story generation."""

    input: str = ""
    outline: str = ""
    partial_draft: str = ""
    first_draft: str = ""
    critique: str = ""
    final_draft: str = ""
