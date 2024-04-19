#!/usr/bin/env python3
"""
type annotated task adv 1
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
                            typing.Union[typing.Any, None]:
    """
    fixing its type annotation
    """
    if lst:
        return lst[0]
    else:
        return None
