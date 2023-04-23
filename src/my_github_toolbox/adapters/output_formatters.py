"""Collection of output formatters."""

import pprint
from enum import Enum
from typing import Any
from typing import Callable

import jsons  # type: ignore


class OutputFormat(Enum):
    """An enumeration of the available output formats."""

    JSON = "json"
    TEXT = "text"


def serialize_json(data: Any) -> str:
    """Serializes the given data to a JSON string.

    Args:
        data: Any, the data to be serialized.

    Returns:
        str, the JSON string representation of the data.
    """
    return str(
        jsons.dumps(data, strict=True, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE)
    )


def serialize_text(data: Any) -> str:
    """Serializes the given data to a string.

    Args:
        data: Any, the data to be serialized.

    Returns:
        str, the string representation of the data.
    """
    return pprint.pformat(data)


def get_serializer(output_format: OutputFormat) -> Callable[[Any], str]:
    """Get a serializer function based on the requested output format.

    Args:
        output_format: The desired output format.

    Returns:
        A function that can be used to serialize data to the desired output format.

    Raises:
        ValueError: If the output format is invalid.
    """
    # Validate the input argument.
    if not isinstance(output_format, OutputFormat):
        raise ValueError("Invalid output format")

    # Return the appropriate serializer function based on the requested output format.
    if output_format == OutputFormat.JSON:
        return serialize_json
    else:
        return serialize_text
