import json
from contextlib import suppress
from typing import Any, cast

from django import forms
from django.utils.safestring import mark_safe

from .script import SCRIPT
from .style import STYLE
from .types import FieldOperators, OperatorPair, QueryBuilderField

DEFAULT_OPERATORS = [
    ("equal", "="),
    ("not_equal", "!="),
    ("contains", "contains"),
    ("not_contains", "doesn't contain"),
    ("greater", ">"),
    ("greater_or_equal", ">="),
    ("less", "<"),
    ("less_or_equal", "<="),
]


def _format_operators(operators: FieldOperators | None) -> list[OperatorPair] | None:
    if not operators:
        return None

    if isinstance(operators[0], str):
        return [cast(OperatorPair, operators)]

    return list(cast(tuple[OperatorPair, ...], operators))


def _parse_fields(fields: dict[str, QueryBuilderField]) -> tuple[list[tuple[str, str]], dict[str, list[OperatorPair]]]:
    if not fields:
        return [], {}

    choices = []
    field_operators = {}

    for key, value in fields.items():
        choices.append((key, value.get("text", key)))

        new_operators = _format_operators(value.get("operators"))

        if not new_operators:
            continue

        field_operators[key] = new_operators

    return choices, field_operators


class QueryBuilderWidget(forms.Textarea):
    def __init__(self, fields: dict[str, QueryBuilderField], *, operators: list[tuple[str, str]] | None = None):
        self.operators = operators or DEFAULT_OPERATORS
        self.fields_choices, self.field_operators = _parse_fields(fields)
        super().__init__()

    def render(self, name: str, value: Any, attrs=None, renderer=None):
        attrs = dict(attrs or {})

        widget_id = attrs.get("id", f"id_{name}")
        container_id = f"{widget_id}_qb"

        rules = {"condition": "AND", "rules": []}

        if value:
            with suppress(TypeError, ValueError):
                parsed = value if isinstance(value, dict) else json.loads(value)

                if isinstance(parsed, dict) and "rules" in parsed:
                    rules = parsed

        attrs["style"] = "display:none;"

        html = super().render(name, json.dumps(rules), attrs, renderer)

        fields_json = json.dumps(self.fields_choices)
        operators_json = json.dumps(self.operators)
        field_operators_json = json.dumps(self.field_operators)
        rules_json = json.dumps(rules)

        formatted_script = SCRIPT.format(
            container_id=container_id,
            widget_id=widget_id,
            fields_json=fields_json,
            operators_json=operators_json,
            field_operators_json=field_operators_json,
            rules_json=rules_json,
        )

        return mark_safe(
            f'<div class="simple-qb" id="{container_id}"></div>{html}'
            f"<style>{STYLE}</style>"
            f"<script>(function(){{{formatted_script}}})();</script>"
        )
