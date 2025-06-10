import logging
from langchain.schema import HumanMessage, SystemMessage
from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from .state import StoryState

logger = logging.getLogger(__name__)


def draft_writer_node(state: StoryState):
    logger.info("Writing story draft...")
    model = get_llm_by_type(AGENT_LLM_MAP["story_draft_writer"])
    content = f"Outline:\n{state['outline']}"
    if state.get("partial_draft"):
        content += f"\n\nPartial Draft:\n{state['partial_draft']}"
    response = model.invoke(
        [
            SystemMessage(content=get_prompt_template("story/story_draft_writer")),
            HumanMessage(content=content),
        ]
    )
    return {"first_draft": response.content}
