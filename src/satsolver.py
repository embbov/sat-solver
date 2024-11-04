from enum import Enum
import sys
import re
import copy


class Satisfiability(Enum):
    SATISFIABLE = "satisfiable"
    UNSATISFIABLE = "unsatisfiable"

class Formula:
    def __init__(self, formula_str: str):
        self._formula_str = formula_str
        self._literals, self._clauses = self.parse_formula_str(self._formula_str)

    def get_clauses(self):
        return [list(clause) for clause in self._clauses]

    def get_literals(self):
        return self._literals

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
        unit_literals = set()
        changed = True

        while changed:
            changed = False
            for clause in self._clauses:
                if len(clause) == 1:  # Unit clause found
                    unit_literal = clause[0]
                    unit_literals.add(unit_literal)
                    changed = True

            # Simplify clauses using unit literals
            new_clauses = []
            for clause in self._clauses:
                if any(lit in unit_literals for lit in clause):
                    continue  # Clause satisfied by a unit literal
                new_clause = [lit for lit in clause if self.negate(lit) not in unit_literals]
                if not new_clause:  # Found an empty clause, unsatisfiable
                    return False
                new_clauses.append(new_clause)

            self._clauses = new_clauses
            self._literals.update(unit_literals)

        return True

def prove(formula: Formula):

    if any(len(clause) == 0 for clause in formula.get_clauses()):
        return Satisfiability.UNSATISFIABLE

    if not formula.get_clauses():
        return Satisfiability.SATISFIABLE

    if not formula.unit_propagate():
        return Satisfiability.UNSATISFIABLE

    for literal in formula.get_literals():

        formula_with_literal = copy.deepcopy(formula)
        formula_with_literal.get_clauses().append([literal])

        if prove(formula_with_literal) == Satisfiability.SATISFIABLE:
            return Satisfiability.SATISFIABLE

        formula_with_neg_literal = copy.deepcopy(formula)
        formula_with_neg_literal.get_clauses().append([formula.negate(literal)])

        if prove(formula_with_neg_literal) == Satisfiability.SATISFIABLE:
            return Satisfiability.SATISFIABLE

    return Satisfiability.UNSATISFIABLE

def validate_format(formula_str):
    """Validate that the input string is in the correct format."""
    clause_pattern = r"-?[1-9]\d*(\s-?[1-9]\d*)*" # Regular expression pattern to match clause
    formula_pattern = f"^{clause_pattern}(, {clause_pattern})*$" # Regular expression pattern for entire formula
    return re.match(formula_pattern, formula_str) is not None # Check for match

def main():
    if len(sys.argv) == 2:
        if validate_format(sys.argv[1]):
            formula = Formula(sys.argv[1])
            result = prove(formula)
            print(f"Formula is {result}")
        else:
            print("Invalid input argument. Exiting program.")
            sys.exit(1)
    else:
        print("Please provide exactly one argument. Exiting program.")
        sys.exit(1)

if __name__ == "__main__":
    main()
