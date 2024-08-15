#!/usr/bin/env python3
"""
    Contains the element_length function
"""
from typing import Sequence, List, Tuple, Any


def element_length(lst: Sequence[Any]) -> List[Tuple[Any, int]]:
    """
        Returns a list of tuples, where each tuple contains an element from the 
        input sequence and the length of that element.
        
        This function takes a sequence of elements (e.g., strings, lists, or tuples)
        and returns a list of tuples. Each tuple consists of the element itself 
        and its length as calculated by the `len()` function.

        Args:
            lst (Sequence[Any]): A sequence of elements that can be passed to the
                                `len()` function (e.g., strings, lists, tuples).

        Returns:
            List[Tuple[Any, int]]: A list of tuples. Each tuple contains an element 
                                from the input sequence and the length of that 
                                element.
    """
    return [(i, len(i)) for i in lst]

