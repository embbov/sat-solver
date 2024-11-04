from enum import Enum
import sys

class Satisfiability(Enum):
    SATISFIABLE = "satisfiable"
    UNSATISFIABLE = "unsatisfiable"

def negate(literal):
    """Returns the negation of literal."""
    return -literal

def unit_propagate(formula, literal):
    """Performs unit subsumption or unit resolution if applicable."""
    return

def prove(sequent):
    return

def main():
    if len(sys.argv) == 2:
        prove(sys.argv[1])
    else:
        print("Please provide exactly one argument. Exiting program.")
        sys.exit(1)

if __name__ == "__main__":
    main()
