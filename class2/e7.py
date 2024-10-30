from typing import List, Tuple
def cal_shortest_dist(a: List[Tuple[int, int]]) -> int:
    result = []
    for i in a:
        for j in a[a.index(i)+1:]:
            result.append(((i[0] - j[0])**2 + (i[1] - j[1])**2)**0.5)
    return result
    # return [((a[i][0] - a[i + 1][0])**2 + (a[i][1] - a[i + 1][1])**2)**0.5 for i in range(len(a) - 1)]

print(cal_shortest_dist([(0, 0), (3, 4)]))
print(cal_shortest_dist([(3,4), (0,1), (5,7)]))
