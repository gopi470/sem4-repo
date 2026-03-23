#Clause Class
class Clause:
    def __init__(self, body, head):
        self.body = body      
        self.head = head      

    def __str__(self):
        if self.body:
            return f"{' ∧ '.join(self.body)} → {self.head}"
        return f"→ {self.head}"


#Knowledge Base Class
class KB:
    def __init__(self, clauses=None):
        self.clauses = []
        self.head_to_clauses = {}
        if clauses:
            for c in clauses:
                self.add_clause(c)

    def add_clause(self, c):
        self.clauses.append(c)
        if c.head not in self.head_to_clauses:
            self.head_to_clauses[c.head] = []
        self.head_to_clauses[c.head].append(c)

    def clauses_for_head(self, atom):
        return self.head_to_clauses.get(atom, [])

    def __iter__(self):
        return iter(self.clauses)

    def __str__(self):
        return "\n".join(str(c) for c in self.clauses)


#Resolution for Horn Clauses
def resolve(c1, c2):
    # If head of c1 appears in body of c2
    if c1.head in c2.body:
        new_body = [x for x in c2.body if x != c1.head] + c1.body
        return Clause(new_body, c2.head)
    return None


#Top-Down Proof (Backward Chaining)
def prove_topdown(kb, goals):
    print("Top-Down Proving:", goals)

    if not goals:
        return True

    first, rest = goals[0], goals[1:]

    for clause in kb.clauses_for_head(first):
        new_goals = clause.body + rest
        print(f"Using {clause}, New Goals: {new_goals}")
        if prove_topdown(kb, new_goals):
            return True

    return False


#Bottom-Up (Forward Chaining / Fixed Point)
def fixed_point(kb):
    derived = set()
    changed = True

    while changed:
        changed = False
        for clause in kb:
            if all(atom in derived for atom in clause.body):
                if clause.head not in derived:
                    derived.add(clause.head)
                    changed = True
                    print(f"Derived: {clause.head}")

    return derived



if __name__ == "__main__":

    example_kb = KB([
        Clause(['b', 'c'], 'a'),
        Clause(['d', 'e'], 'b'),
        Clause(['g', 'e'], 'b'),
        Clause(['e'], 'c'),
        Clause([], 'd'),
        Clause([], 'e'),
        Clause(['a', 'g'], 'f'),
        Clause(['a'], 'y')
    ])

    print("Knowledge Base:")
    print(example_kb)

    
    goal = ['a']

    print("\n--- TOP-DOWN RESULT ---")
    result_td = prove_topdown(example_kb, goal)
    print("Proved?" , result_td)

    print("\n--- BOTTOM-UP RESULT ---")
    fp = fixed_point(example_kb)
    print("Fixed Point:", fp)
    print("Goal in Fixed Point?", 'a' in fp)
