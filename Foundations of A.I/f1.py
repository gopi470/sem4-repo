# ---------------- Clause ----------------
class Clause:
    def __init__(self, body, head):
        # body = list of conditions (premises)
        # head = conclusion
        self.body = body
        self.head = head

    def __str__(self):
        # Format: A ∧ B → C  OR  → C (fact)
        return f"{' ∧ '.join(self.body)} → {self.head}" if self.body else f"→ {self.head}"


# ---------------- Knowledge Base ----------------
class KB:
    def __init__(self, clauses=None):
        # Store all clauses
        self.clauses = clauses or []

        # Map: head → list of clauses that derive it
        self.map = {}

        # Build mapping for quick lookup
        for c in self.clauses:
            self.map.setdefault(c.head, []).append(c)

    def clauses_for_head(self, atom):
        # Return all rules that can produce 'atom'
        return self.map.get(atom, [])

    def __iter__(self):
        # Allow iteration over clauses
        return iter(self.clauses)

    def __str__(self):
        # Print all clauses nicely
        return "\n".join(map(str, self.clauses))


# ---------------- Top-Down (Backward Chaining) ----------------
def prove_topdown(kb, goals):
    # Print current goals
    print("Top-Down Proving:", goals)

    # If no goals left → success
    if not goals:
        return True

    # Take first goal and remaining goals
    first, rest = goals[0], goals[1:]

    # Try all clauses that can produce this goal
    for clause in kb.clauses_for_head(first):

        # Replace goal with its subgoals (body of rule)
        new_goals = clause.body + rest
        print(f"Using {clause}, New Goals: {new_goals}")

        # Recursively try to prove new goals
        if prove_topdown(kb, new_goals):
            return True

    # If no rule works → failure
    return False


# ---------------- Bottom-Up (Forward Chaining) ----------------
def fixed_point(kb):
    # Set of derived facts
    derived = set()

    while True:
        added = False  # track if new fact is added

        for c in kb:
            # If all conditions (body) are already derived
            if all(x in derived for x in c.body) and c.head not in derived:

                # Add new fact
                derived.add(c.head)
                added = True
                print(f"Derived: {c.head}")

        # If no new facts → fixed point reached
        if not added:
            return derived


# ---------------- DRIVER ----------------
if __name__ == "__main__":

    # Create Knowledge Base (Horn clauses)
    kb = KB([
        Clause(['b', 'c'], 'a'),     # b ∧ c → a
        Clause(['d', 'e'], 'b'),     # d ∧ e → b
        Clause(['g', 'e'], 'b'),     # g ∧ e → b
        Clause(['e'], 'c'),          # e → c
        Clause([], 'd'),             # fact: d
        Clause([], 'e'),             # fact: e
        Clause(['a', 'g'], 'f'),     # a ∧ g → f
        Clause(['a'], 'y')           # a → y
    ])

    # Print KB
    print("Knowledge Base:")
    print(kb)

    # Goal to prove
    goal = ['a']

    # ---------------- Top-Down ----------------
    print("\n--- TOP-DOWN RESULT ---")
    print("Proved?", prove_topdown(kb, goal))

    # ---------------- Bottom-Up ----------------
    print("\n--- BOTTOM-UP RESULT ---")
    fp = fixed_point(kb)

    print("Fixed Point:", fp)
    print("Goal in Fixed Point?", 'a' in fp)