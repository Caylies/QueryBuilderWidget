from query_builder_widget import QueryBuilderWidget
from query_builder_widget.types import FieldOperators

_COMMON_NUMBER_OPERATORS: FieldOperators = (
    ("equals", "="),
    ("not_equals", "!="),
    ("greater", ">"),
    ("greater_or_equal", ">="),
    ("less", "<"),
    ("less_or_equal", "<="),
)

QueryBuilderWidget({
    "server": {
        "text": "In server",
        "operators": (("equals", "="),)
    },
    "completion": {
        "text": "Ball completion percentage",
        "operators": _COMMON_NUMBER_OPERATORS
    },
    "ballcount": {
        "text": "Ball count",
        "operators": _COMMON_NUMBER_OPERATORS
    },
})
