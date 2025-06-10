import logging
from langchain.schema import HumanMessage, SystemMessage
from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from .state import StoryState

logger = logging.getLogger(__name__)


def critique_node(state: StoryState):
    logger.info("Critiquing draft...")
    model = get_llm_by_type(AGENT_LLM_MAP["story_critique"])
    response = model.invoke(
        [
            SystemMessage(content=get_prompt_template("story/story_critique")),
            HumanMessage(content=state["first_draft"]),
        ]
    )
    return {"critique": response.content}
