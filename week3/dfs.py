def find_path(
    neighbour_fn, start, goal, visited, reachable=lambda pos: True, depth=100000
):
    # The reachable function returns true if the given node is not blocked by a wall.

    if start == goal:
        return [goal]

    if depth == 0 or start in visited or not reachable(start):
        return []

    visited.append(start)  # Use a set for visited to improve efficiency

    # check neighbours
    neighbours = neighbour_fn(start)
    for n in neighbours:
        rest_of_path = find_path(neighbour_fn, n, goal, visited, reachable, depth - 1)
        if rest_of_path:
            return [start] + rest_of_path

    return []
