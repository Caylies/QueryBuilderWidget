import pytest  # noqa: F401

from query_builder_widget import evaluate
from query_builder_widget.types import QueryGroup

CONDITIONS: QueryGroup = {
    "rules": [
        {"field": "server", "value": "1255250024741212262", "operator": "equals"},
        {
            "rules": [
                {"field": "completion", "value": "70", "operator": "greater_or_equal"},
                {"field": "ballcount", "value": "5", "operator": "greater_or_equal"},
            ],
            "condition": "AND",
        },
    ],
    "condition": "OR",
}


async def test_evaluation():
    data = {"server": "1255250024741212262", "completion": "50", "ballcount": "7"}

    result = await evaluate(
        CONDITIONS, data, field_labels={"server": "Server", "completion": "Ball completion", "ballcount": "Ball count"}
    )

    assert result.passed, ", ".join(result.failures)
