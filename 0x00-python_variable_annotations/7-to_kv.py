#!/usr/bin/env python3
"""
type annotated task 7
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    returns a tuple
    """
    return (k, v**2)
