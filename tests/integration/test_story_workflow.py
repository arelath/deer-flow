import pytest
from unittest.mock import MagicMock

from src.story.graph.builder import build_graph


def make_llm(response: str):
    llm = MagicMock()
    llm.invoke.return_value = MagicMock(content=response)
    return llm


def setup_mocks(monkeypatch):
    # patch get_llm_by_type in each node module
    monkeypatch.setattr(
        "src.story.graph.outline_planner_node.get_llm_by_type",
        lambda _: make_llm("outline"),
    )
    monkeypatch.setattr(
        "src.story.graph.draft_writer_node.get_llm_by_type",
        lambda _: make_llm("draft"),
    )
    monkeypatch.setattr(
        "src.story.graph.critique_node.get_llm_by_type",
        lambda _: make_llm("critique"),
    )
    monkeypatch.setattr(
        "src.story.graph.editor_node.get_llm_by_type",
        lambda _: make_llm("final"),
    )


@pytest.fixture(autouse=True)
def patch_llms(monkeypatch):
    setup_mocks(monkeypatch)


def test_workflow_runs_without_outline():
    workflow = build_graph()
    state = workflow.invoke({"input": "idea", "outline": "", "partial_draft": ""})
    assert state["final_draft"] == "final"
    assert state["outline"] == "outline"


def test_workflow_skips_outline_when_provided():
    workflow = build_graph()
    state = workflow.invoke({"input": "idea", "outline": "user outline"})
    assert state["final_draft"] == "final"
    assert state["outline"] == "user outline"
