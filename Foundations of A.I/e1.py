

def negate(lit):
    return lit[1:] if lit.startswith("¬") else "¬" + lit



# Knowledge Base Class
class KB:
    def __init__(self):
        self.clauses = set()

    def add(self, clause):
        self.clauses.add(frozenset(clause))

    def __iter__(self):
        return iter(self.clauses)

    def __str__(self):
        return "\n".join(str(set(c)) for c in self.clauses)


#Resolution Function
def resolve(c1, c2):
    resolvents = []

    for lit in c1:
        if negate(lit) in c2:
            new_clause = (c1 - {lit}) | (c2 - {negate(lit)})
            resolvents.append(frozenset(new_clause))

    return resolvents


#Linear Resolution
def refute_linear(K, G):
    print("\n--- Linear Resolution ---")

    kb = set(K.clauses)
    kb.add(frozenset({negate(G)}))   # Add ¬G

    proof = [frozenset({negate(G)})]

    while True:
        last = proof[-1]
        derived = False

        for clause in kb | set(proof):
            resolvents = resolve(last, clause)
            for res in resolvents:
                print(f"Resolve {set(last)} with {set(clause)} -> {set(res)}")
                if not res:
                    print("Derived EMPTY clause. PROVED.")
                    return True
                if res not in proof:
                    proof.append(res)
                    derived = True
                    break
            if derived:
                break

        if not derived:
            print("No new clause derived. FAILED.")
            return False


#Unit Resolution
def refute_unit(K, G):
    print("\n--- Unit Resolution ---")

    kb = set(K.clauses)
    kb.add(frozenset({negate(G)}))

    proof = [frozenset({negate(G)})]

    while True:
        last = proof[-1]
        derived = False

        for clause in kb | set(proof):

            # One must be unit clause
            if len(last) == 1 or len(clause) == 1:

                resolvents = resolve(last, clause)

                for res in resolvents:
                    print(f"Resolve {set(last)} with {set(clause)} -> {set(res)}")
                    if not res:
                        print("Derived EMPTY clause. PROVED.")
                        return True
                    if res not in proof:
                        proof.append(res)
                        derived = True
                        break

            if derived:
                break

        if not derived:
            print("No new clause derived. FAILED.")
            return False



if __name__ == "__main__":

    # Test 1
    print("\nTEST 1")
    kb1 = KB()
    kb1.add({"A"})
    kb1.add({"¬B"})
    kb1.add({"¬A", "¬C", "B"})
    print("Linear Result:", refute_linear(kb1, "C"))
    print("Unit Result:", refute_unit(kb1, "C"))

    # Test 2
    print("\nTEST 2")
    kb2 = KB()
    kb2.add({"P", "Q"})
    kb2.add({"¬P", "R"})
    kb2.add({"¬Q", "R"})
    print("Linear Result:", refute_linear(kb2, "R"))
    print("Unit Result:", refute_unit(kb2, "R"))

    # Test 3 (Unit resolution fails here)
    print("\nTEST 3")
    kb3 = KB()
    kb3.add({"¬P", "¬Q", "R"})
    kb3.add({"¬P", "S"})
    kb3.add({"¬Q", "S"})
    kb3.add({"P"})
    kb3.add({"Q"})
    print("Linear Result:", refute_linear(kb3, "R"))
    print("Unit Result:", refute_unit(kb3, "R"))
