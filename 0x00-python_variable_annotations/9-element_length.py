#!/usr/bin/env python3
"""
type annotated task 10
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    return len(i) i in list
    """
    return [(i, len(i)) for i in lst]
