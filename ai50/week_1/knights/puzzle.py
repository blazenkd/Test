'''
AI50 2023
Week 1: puzzle.py

Your task in this problem is to determine how to represent these puzzles using propositional logic,
such that an AI running a model-checking algorithm could solve these puzzles for us.


'''

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can only be a knight or a knave
    Or(AKnave, AKnight),
    # A cannot be both a Knight and a Knave at the same time.
    Not(And(AKnave, AKnight)),

    #  If A is a Knight, then A is both a Knight and a Knave. If A is a Knave, then A is not both a Knight and a Knave.
    Biconditional(AKnight, And(AKnight, AKnave))
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Not(And(AKnight, AKnave)),  # cannot be knight and knave at the same time
    Or(AKnight, AKnave),        # will be Knight or Knave

    Not(And(BKnight, BKnave)),  # cannot be knight and knave at the same time
    Or(BKnight, BKnave),        # will be Knight or Knave

    # Or(And(AKnight, BKnave), And(AKnave, BKnight)), # A and B can't be the same figure

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are either knights or knaves
    # A and B cannot be both knights or both knaves
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),

    # A says "We are the same kind."
    # If A is a Knight, then A and B are either both knaves or both knights.
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    # B says "We are of different kinds."
    # If B is a Knight, then A and B are different kinds (one is a knight and one is a knave).
    Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
)


# Puzzle 3
# A, B, C are either knights or knaves
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Not(And(CKnave, CKnight)),

    Biconditional(Or(AKnight, AKnave), Or(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
