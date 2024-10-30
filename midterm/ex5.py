def print_shortest_dist(points: list[tuple[int, int]]) -> None: # type hints for clarity
    # can be shortened as:
    # result = [((i,j), ((i[0] - j[0])**2 + (i[1] - j[1])**2)**0.5) for i in data for j in data[data.index(i)+1:]]
    result = []
    for i in points:
        for j in points[points.index(i)+1:]:
            result.append(((i,j), ((i[0] - j[0])**2 + (i[1] - j[1])**2)**0.5))
    minimum = min(result, key = lambda x: x[1])[1]
    for i in result:
        if i[1] == minimum:
            print("coordinates:", i[0][0], i[0][1], "distance:", i[1])


data = [(3,4),
        (33,22),
        (-5,8),
        (13,17),
        (23,15),
        (-12,3),
        (8,7)]

print_shortest_dist(data)
