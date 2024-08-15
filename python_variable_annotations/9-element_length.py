from typing import Sequence, List, Tuple, Any

def element_length(lst: Sequence[Any]) -> List[Tuple[Any, int]]:
    return [(i, len(i)) for i in lst]
