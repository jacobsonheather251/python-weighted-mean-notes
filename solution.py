

def solve(value):
    return sum(x*w for x, w in zip(value["values"], value["weights"])) / sum(value["weights"]) if len(value["values"]) == len(value["weights"]) and all(w >= 0 for w in value["weights"]) and sum(value["weights"]) > 0 else (_ for _ in ()).throw(ValueError("invalid weights"))
