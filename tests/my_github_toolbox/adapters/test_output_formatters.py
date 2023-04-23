"""Unit tests for the output_formatters module."""
from dataclasses import dataclass
from typing import Any
from typing import Callable

import pytest

from my_github_toolbox.adapters.output_formatters import OutputFormat
from my_github_toolbox.adapters.output_formatters import get_serializer
from my_github_toolbox.adapters.output_formatters import serialize_json
from my_github_toolbox.adapters.output_formatters import serialize_text


# Base Python package name we use for mocking
# TEST_MOCK_MODULE = "tests.my_github_toolbox.adapters.test_output_formatters"
TEST_MOCK_MODULE = "my_github_toolbox.adapters.output_formatters"

data = {"fooBar": 123, "baz_qux": "hello world"}


@pytest.mark.parametrize(
    "output_format, expected_serializer_function",
    [
        (OutputFormat.JSON, serialize_json),
        (OutputFormat.TEXT, serialize_text),
    ],
)
def test_get_serializer(
    output_format: OutputFormat, expected_serializer_function: Callable[[Any], str]
) -> None:
    assert get_serializer(output_format) == expected_serializer_function


def test_get_serializer_with_invalid_input() -> None:
    with pytest.raises(ValueError):
        get_serializer("invalid-expected-output-format")  # type: ignore


@dataclass
class Person:
    name: str
    age: int
    address: str


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            {"name": "John Doe", "age": 35, "address": "123 Main St."},
            '{"name": "John Doe", "age": 35, "address": "123 Main St."}',
        ),
        ([1, 2, 3], "[1, 2, 3]"),
        (
            Person(name="John Doe", age=35, address="123 Main St."),
            '{"address": "123 Main St.", "age": 35, "name": "John Doe"}',
        ),
        ({}, "{}"),
    ],
)
def test_serialize_json(input_data: Any, expected_output: str) -> None:
    assert serialize_json(input_data) == expected_output


# unit tests for serialized_text
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            {"name": "John Doe", "age": 35, "address": "123 Main St."},
            "{'address': '123 Main St.', 'age': 35, 'name': 'John Doe'}",
        ),
        ([1, 2, 3], "[1, 2, 3]"),
        (
            Person(name="John Doe", age=35, address="123 Main St."),
            "Person(name='John Doe', age=35, address='123 Main St.')",
        ),
        ({}, "{}"),
    ],
)
def test_serialize_text(input_data: Any, expected_output: str) -> None:
    assert serialize_text(input_data) == expected_output
