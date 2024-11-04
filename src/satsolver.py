from enum import Enum
import sys
from typing import Tuple


class Satisfiability(Enum):
    SATISFIABLE = "satisfiable"
    UNSATISFIABLE = "unsatisfiable"

class Formula:
    def __init__(self, formula_str: str):
        self._formula_str = formula_str
        self._literals, self._clauses = self.parse_formula_str(self._formula_str)

    def get_clauses(self):
        return [list(clause) for clause in self._clauses]

    def parse_formula_str(self, formula_str: str):
        literals = set()
        clauses = []

        clause_strings = formula_str.split(",")

        for clause_str in clause_strings:
            clause = [int(lit) for lit in clause_str.strip().split()]
            clauses.append(clause)

            literals.update(clause)

        return literals, clauses

    def negate(self, literal: int):
        """Returns the negation of literal."""
        return -literal

    def unit_propagate(self):
        """Performs unit subsumption or unit resolution if applicable."""
        return

def prove(formula: Formula) -> Satisfiability:

    if any(len(clause) == 0 for clause in formula.get_clauses()):
        return Satisfiability.UNSATISFIABLE

    if not formula.get_clauses():
        return Satisfiability.SATISFIABLE

    if not formula.unit_propagate():
        return Satisfiability.UNSATISFIABLE

    # Insert unit propagation here

def main():
    if len(sys.argv) == 2:
        formula = Formula(sys.argv[1])
        prove(formula)
    else:
        print("Please provide exactly one argument. Exiting program.")
        sys.exit(1)

if __name__ == "__main__":
    main()
