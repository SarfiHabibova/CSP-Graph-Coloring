def parse_input(filename):
    k = None
    edges = set()
    vertices = set()

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # first line defines number of colors
            if line.startswith("colors="):
                try:
                    k = int(line.split("=")[1])
                except ValueError:
                    raise ValueError("Invalid colors line format")
                continue

            # remaining lines are edges
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 2:
                u, v = int(parts[0]), int(parts[1])

                # self-loop means unsatisfiable
                if u == v:
                    return k, [], True

                edge = tuple(sorted((u, v)))
                edges.add(edge)
                vertices.add(u)
                vertices.add(v)

    return k, sorted(vertices), False, sorted(edges)
