from typing import NotRequired, TypedDict

OperatorPair = tuple[str, str]
FieldOperators = OperatorPair | tuple[OperatorPair, ...]


class QueryBuilderField(TypedDict):
    text: str
    operators: NotRequired[FieldOperators]
