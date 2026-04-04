# --------------------------------------------------
# Negation Function
# --------------------------------------------------
def negate(lit):
    # If literal starts with ¬ → remove it
    # Else → add ¬ in front
    return lit[1:] if lit.startswith("¬") else "¬" + lit


# --------------------------------------------------
# Knowledge Base Class (stores clauses)
# --------------------------------------------------
class KB:
    def __init__(self):
        # Set of clauses (each clause = frozenset)
        self.clauses = set()

    def add(self, clause):
        # Add clause as immutable set (avoids duplicates)
        self.clauses.add(frozenset(clause))

    def __iter__(self):
        # Allow iteration over KB
        return iter(self.clauses)

    def __str__(self):
        # Pretty print KB
        return "\n".join(str(set(c)) for c in self.clauses)


# --------------------------------------------------
# Resolution Function
# --------------------------------------------------
def resolve(c1, c2):
    resolvents = []

    # Try resolving each literal in clause c1
    for lit in c1:
        # Check if complementary literal exists in c2
        if negate(lit) in c2:

            # Remove lit from c1 and ¬lit from c2
            # Combine remaining parts → new clause
            new_clause = (c1 - {lit}) | (c2 - {negate(lit)})

            # Add resulting clause
            resolvents.append(frozenset(new_clause))

    return resolvents


# --------------------------------------------------
# Linear Resolution
# --------------------------------------------------
def refute_linear(K, G):
    print("\n--- Linear Resolution ---")

    # Copy KB and add negation of goal ¬G
    kb = set(K.clauses)
    kb.add(frozenset({negate(G)}))

    # Proof list (stores derived clauses)
    proof = [frozenset({negate(G)})]

    while True:
        # Always resolve using last derived clause
        last = proof[-1]
        derived = False

        # Try resolving with all clauses
        for clause in kb | set(proof):

            resolvents = resolve(last, clause)

            for res in resolvents:
                print(f"Resolve {set(last)} with {set(clause)} -> {set(res)}")

                # Empty clause → contradiction → success
                if not res:
                    print("Derived EMPTY clause. PROVED.")
                    return True

                # Add new clause if not already present
                if res not in proof:
                    proof.append(res)
                    derived = True
                    break

            if derived:
                break

        # No new clause → failure
        if not derived:
            print("No new clause derived. FAILED.")
            return False


# --------------------------------------------------
# Strict Unit Resolution
# --------------------------------------------------
def refute_unit(K, G):
    print("\n--- Unit Resolution ---")

    # Copy KB and add ¬G
    kb = set(K.clauses)
    kb.add(frozenset({negate(G)}))

    # Start with unit clause ¬G
    proof = [frozenset({negate(G)})]

    while True:
        last = proof[-1]
        derived = False

        # Only proceed if last clause is UNIT (size = 1)
        if len(last) != 1:
            print("No new clause derived. FAILED.")
            return False

        # Try resolving with all clauses in KB
        for clause in kb:

            resolvents = resolve(last, clause)

            for res in resolvents:
                print(f"Resolve {set(last)} with {set(clause)} -> {set(res)}")

                # Empty clause → proof success
                if not res:
                    print("Derived EMPTY clause. PROVED.")
                    return True

                # Only accept UNIT clauses (strict rule)
                if len(res) == 1 and res not in proof:
                    proof.append(res)
                    derived = True
                    break

            if derived:
                break

        # No new unit clause → failure
        if not derived:
            print("No new clause derived. FAILED.")
            return False


# --------------------------------------------------
# MAIN DRIVER (Test Cases)
# --------------------------------------------------
if __name__ == "__main__":

    # ---------------- TEST 1 ----------------
    print("\nTEST 1")
    kb1 = KB()

    # Clauses:
    # A
    # ¬B
    # ¬A ∨ ¬C ∨ B
    kb1.add({"A"})
    kb1.add({"¬B"})
    kb1.add({"¬A", "¬C", "B"})

    # Prove C
    print("Linear Result:", refute_linear(kb1, "C"))
    print("Unit Result:", refute_unit(kb1, "C"))

    # ---------------- TEST 2 ----------------
    print("\nTEST 2")
    kb2 = KB()

    # Clauses:
    # P ∨ Q
    # ¬P ∨ R
    # ¬Q ∨ R
    kb2.add({"P", "Q"})
    kb2.add({"¬P", "R"})
    kb2.add({"¬Q", "R"})

    # Prove R
    print("Linear Result:", refute_linear(kb2, "R"))
    print("Unit Result:", refute_unit(kb2, "R"))

    # ---------------- TEST 3 ----------------
    print("\nTEST 3")
    kb3 = KB()

    # Clauses:
    # ¬P ∨ ¬Q ∨ R
    # ¬P ∨ S
    # ¬Q ∨ S
    # P
    # Q
    kb3.add({"¬P", "¬Q", "R"})
    kb3.add({"¬P", "S"})
    kb3.add({"¬Q", "S"})
    kb3.add({"P"})
    kb3.add({"Q"})

    # Prove R
    print("Linear Result:", refute_linear(kb3, "R"))
    print("Unit Result:", refute_unit(kb3, "R"))