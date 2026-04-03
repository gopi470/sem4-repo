# -----------------------------
# Variable Class
# -----------------------------
class Variable:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def __repr__(self):
        return self.name


# -----------------------------
# Factor Class
# -----------------------------
class Factor:
    def __init__(self, var, parents, table):
        self.var = var
        self.parents = parents
        self.table = table  # CPT

    def evaluate(self, assignment):
        """
        Evaluate factor value for given assignment dictionary
        """
        try:
            val = self.table
            for p in self.parents:
                val = val[assignment[p]]
            val = val[assignment[self.var]]
            return val
        except KeyError:
            return None


# -----------------------------
# Graphical Model Class
# -----------------------------
class GraphicalModel:
    def __init__(self, variables, factors):
        self.variables = list(variables)
        self.factors = list(factors)


# -----------------------------
# Enumeration Algorithm
# -----------------------------
def enumerate_all(vars_list, assignment, factors):
    if not vars_list:
        return 1.0

    first = vars_list[0]
    rest = vars_list[1:]

    if first in assignment:
        prob = 1.0
        for f in factors:
            val = f.evaluate(assignment)
            if val is not None:
                prob *= val
        return prob * enumerate_all(rest, assignment, factors)

    else:
        total = 0
        for value in first.domain:
            new_assign = assignment.copy()
            new_assign[first] = value
            total += enumerate_all(rest, new_assign, factors)
        return total


# -----------------------------
# Marginal Probability
# -----------------------------
def marginal_prob(query, evidence, model):
    probs = {}

    for value in query.domain:
        assign = evidence.copy()
        assign[query] = value
        probs[value] = enumerate_all(model.variables, assign, model.factors)

    # Normalize
    total = sum(probs.values())
    for k in probs:
        probs[k] /= total

    return probs


# -----------------------------
# Example (from your PDF)
# -----------------------------
if __name__ == "__main__":

    boolean = [False, True]

    Tamper = Variable("Tamper", boolean)
    Fire = Variable("Fire", boolean)
    Smoke = Variable("Smoke", boolean)
    Alarm = Variable("Alarm", boolean)
    Leaving = Variable("Leaving", boolean)
    Report = Variable("Report", boolean)

    # Factors (CPTs)
    f_ta = Factor(Tamper, [], [0.98, 0.02])
    f_fi = Factor(Fire, [], [0.99, 0.01])
    f_sm = Factor(Smoke, [Fire], [[0.99, 0.01], [0.1, 0.9]])
    f_al = Factor(Alarm, [Fire, Tamper],
                  [[[0.9999, 0.0001], [0.15, 0.85]],
                   [[0.01, 0.99], [0.5, 0.5]]])
    f_lv = Factor(Leaving, [Alarm], [[0.999, 0.001], [0.12, 0.88]])
    f_re = Factor(Report, [Leaving], [[0.99, 0.01], [0.25, 0.75]])

    bn = GraphicalModel(
        {Tamper, Fire, Smoke, Alarm, Leaving, Report},
        {f_ta, f_fi, f_sm, f_al, f_lv, f_re}
    )

    # Example Query: P(Report | Smoke=True)
    evidence = {Smoke: True}
    result = marginal_prob(Report, evidence, bn)

    print("P(Report | Smoke=True):")
    for k, v in result.items():
        print(f"{k} : {v:.5f}")