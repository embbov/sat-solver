from enum import Enum

class Satisfiability(Enum):
    SATISFIABLE = "satisfiable"
    UNSATISFIABLE = "unsatisfiable"

def negate(literal):
    """Returns the negation of literal."""
    return -literal
