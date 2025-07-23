from typing import List, Tuple, Dict, Union
# Type hints are added using the colon (:) syntax for variables 
n : int = 5

# These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.
numbers: List[int] = [1, 2, 3, 4,5]


name : str = " harry"

# the -> syntax for function return types.
def sum(a : int, b : int ) -> int:
    return a+b
