import logging
from langchain.schema import HumanMessage, SystemMessage
from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from .state import StoryState

logger = logging.getLogger(__name__)


def editor_node(state: StoryState):
    logger.info("Editing draft...")
    model = get_llm_by_type(AGENT_LLM_MAP["story_editor"])
    content = f"Draft:\n{state['first_draft']}\n\nCritique:\n{state['critique']}"
    response = model.invoke(
        [
            SystemMessage(content=get_prompt_template("story/story_editor")),
            HumanMessage(content=content),
        ]
    )
    return {"final_draft": response.content}
