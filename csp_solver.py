from ac3 import ac3
from heuristics import select_unassigned_var, order_domain_values

def build_neighbors(edges):
    neighbors = {}
    for (u, v) in edges:
        neighbors.setdefault(u, set()).add(v)
        neighbors.setdefault(v, set()).add(u)
    return neighbors

def backtrack(domains, neighbors, edges, assignment, trail):
    if len(assignment) == len(domains):
        return True

    var = select_unassigned_var(domains, assignment)
    if var is None:
        return True

    for value in order_domain_values(var, domains, neighbors, assignment):
        assignment[var] = value
        saved_index = len(trail)

        old_domain = set(domains[var])
        domains[var] = {value}

        ok, removed = ac3(domains, edges)
        trail.extend(removed)

        if ok and backtrack(domains, neighbors, edges, assignment, trail):
            return True

        for (v, val) in reversed(trail[saved_index:]):
            domains[v].add(val)
        del trail[saved_index:]
        domains[var] = old_domain
        del assignment[var]

    return False

def solve_csp(filename, parser):
    k, vertices, selfloop, edges = parser(filename)

    if k is None:
        print("failure (no color count found)")
        return

    if selfloop:
        print("failure (self-loop detected)")
        return

    if not vertices:
        print("SOLUTION: {}")
        return

    domains = {v: set(range(1, k + 1)) for v in vertices}
    neighbors = build_neighbors(edges)

    ok, _ = ac3(domains, edges)
    if not ok:
        print("failure (AC3 inconsistency)")
        return

    assignment = {}
    trail = []

    result = backtrack(domains, neighbors, edges, assignment, trail)

    if result:
        ordered = ", ".join(f"{v}: {assignment[v]}" for v in sorted(assignment))
        print(f"SOLUTION: {{{ordered}}}")
    else:
        print("failure")
