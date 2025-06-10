import logging
from langchain.schema import HumanMessage, SystemMessage
from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from .state import StoryState

logger = logging.getLogger(__name__)


def outline_planner_node(state: StoryState):
    if state["outline"]:
        logger.info("Outline provided, skipping generation.")
        return {}
    logger.info("Generating story outline...")
    model = get_llm_by_type(AGENT_LLM_MAP["story_outline_planner"])
    response = model.invoke(
        [
            SystemMessage(content=get_prompt_template("story/story_outline_planner")),
            HumanMessage(content=state["input"]),
        ]
    )
    return {"outline": response.content}
