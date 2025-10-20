def select_unassigned_var(domains, assignment):
    """MRV: variable with smallest domain (tie -> smallest id)."""
    unassigned = [v for v in domains if v not in assignment]
    if not unassigned:
        return None
    return min(unassigned, key=lambda x: (len(domains[x]), x))

def order_domain_values(var, domains, neighbors, assignment):
    """LCV: order values by least constraint on neighbors."""
    values = list(domains[var])
    ranked = []
    for val in values:
        eliminated = 0
        for nbr in neighbors[var]:
            if nbr in assignment:
                continue
            eliminated += sum(1 for b in domains[nbr] if b == val)
        ranked.append((eliminated, val))
    ranked.sort(key=lambda x: (x[0], x[1]))
    return [val for _, val in ranked]
