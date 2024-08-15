from collections.abc import Callable

def make_multiplier(multiplier: float) -> callable[[], float]:
    return lambda num: num * multiplier