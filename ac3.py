from collections import deque

def revise(domains, xi, xj):
    removed = []
    for a in list(domains[xi]):
        if all(a == b for b in domains[xj]):
            domains[xi].remove(a)
            removed.append((xi, a))
    return removed

def ac3(domains, edges):
    queue = deque()
    for (u, v) in edges:
        queue.append((u, v))
        queue.append((v, u))

    removed_total = []
    while queue:
        xi, xj = queue.popleft()
        removed = revise(domains, xi, xj)
        if removed:
            removed_total.extend(removed)
            if not domains[xi]:
                return False, removed_total
            for (a, b) in edges:
                if b == xi and a != xj:
                    queue.append((a, xi))
                elif a == xi and b != xj:
                    queue.append((b, xi))
    return True, removed_total
