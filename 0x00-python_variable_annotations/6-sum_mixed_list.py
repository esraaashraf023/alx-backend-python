#!/usr/bin/env python3
"""
type annotated task 6
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    return their float sum
    """
    return float(sum(mxd_lst))
