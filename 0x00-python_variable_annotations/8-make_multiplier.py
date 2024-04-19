#!/usr/bin/env python3
"""
type annotated task 8
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    return it multiblied by multiblier
    """
    return lambda x: x * multiplier
