#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        returns a tuple
        
        Args: 
            k (str): string
            v (int/float): number
        
        Returns:
            a tuple
    """
    return (k, float(v ** 2))