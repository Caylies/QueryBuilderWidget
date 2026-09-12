from __future__ import annotations

from typing import Literal, NamedTuple, NotRequired, TypedDict

OperatorPair = tuple[str, str]
FieldOperators = OperatorPair | tuple[OperatorPair, ...]


class QueryBuilderField(TypedDict):
    text: str
    operators: NotRequired[FieldOperators]


class QueryRule(TypedDict):
    field: str
    value: str
    operator: str


class QueryGroup(TypedDict):
    rules: list[QueryGroup | QueryRule]
    condition: Literal["AND", "OR"]


class EvaluationResult(NamedTuple):
    passed: bool
    failures: list[str]
