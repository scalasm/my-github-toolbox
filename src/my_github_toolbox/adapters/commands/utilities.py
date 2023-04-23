"""Shared Click command options."""
import functools
from typing import Any
from typing import Callable
from typing import Tuple

import click

from my_github_toolbox.adapters.output_formatters import OutputFormat


# Note that not sharing options in Click is design decision, see
# https://github.com/pallets/click/issues/108 .
# But since we want to be DRY, using a decorator function is a common
# pattern.
def common_options(func: Callable[..., Any]) -> Callable[..., Any]:
    """Common options for Click commands, like the output format."""

    @click.option(
        "--output-format",
        default=OutputFormat.JSON.value,
        type=click.Choice([format_.value for format_ in OutputFormat]),
        show_default=True,
        help="Output format",
    )
    @click.pass_context
    @functools.wraps(func)
    def _wrapper(
        ctx: click.Context, *args: Tuple[Any], **kwargs: dict[str, Any]
    ) -> Any:
        # XXX Click does not support EnumChoice options yet,
        # see https://github.com/pallets/click/pull/2210
        # So we need to convert the string value to an Enum here to be DRY.

        kwargs["output_format"] = OutputFormat(kwargs["output_format"])  # type: ignore

        return func(ctx, *args, **kwargs)

    return _wrapper
