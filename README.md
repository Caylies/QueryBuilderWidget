# QueryBuilderWidget

![Widget](https://i.imgur.com/qlIBPkg.png)

A small query builder widget for Django.

## Reference

### Widget

```py
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

CONDITIONS = {
    "server": {"text": "In server", "operators": ("equals", "=")},
    "completion": {"text": "Ball completion percentage", "operators": _COMMON_NUMBER_OPERATORS},
    "ballcount": {"text": "Ball count", "operators": _COMMON_NUMBER_OPERATORS},
}

QueryBuilderWidget(CONDITIONS)
```

### Evaluation

```py
async def server(expected: str, operator: str) -> tuple[bool, str | None]: ...


data = {"server": server, "completion": "50", "ballcount": "7"}

result = await evaluate(
    model.conditions,
    data,
    field_labels={"server": "Server", "completion": "Ball completion", "ballcount": "Ball count"},
)

print(result.passed, result.failures)
```
