from hw1 import Solution

test_cases = [
    # test case 1
    [[4, 2, 1, 3], [0, 5, 0, 2], [2, 3, 1, 0]],
    # test case 2
    [
        [1, 0, 3, 2, 1],
        [2, 3, 0, 0, 1],
        [3, 0, 3, 0, 2],
        [0, 4, 1, 5, 2],
        [2, 1, 2, 3, 0],
    ],
    # test case 3
    [
        [2, 0, 0, 2, 2, 2, 2, 0, 0, 3, 0, 2, 0, 1, 2],
        [1, 0, 2, 0, 2, 1, 3, 0, 2, 0, 3, 0, 0, 2, 2],
        [1, 2, 2, 0, 2, 2, 3, 0, 2, 3, 0, 2, 2, 0, 0],
        [0, 2, 5, 1, 2, 1, 0, 2, 2, 0, 2, 0, 2, 3, 0],
        [0, 0, 0, 0, 1, 2, 0, 3, 2, 0, 3, 0, 3, 0, 2],
        [2, 0, 3, 0, 2, 0, 3, 0, 0, 0, 1, 0, 3, 3, 1],
        [0, 1, 0, 0, 1, 1, 2, 0, 2, 2, 0, 1, 2, 3, 2],
        [2, 1, 0, 0, 2, 2, 1, 0, 2, 0, 3, 0, 4, 2, 0],
        [0, 0, 0, 0, 2, 1, 0, 0, 2, 2, 2, 2, 0, 0, 0],
        [0, 2, 0, 2, 2, 3, 0, 3, 2, 0, 3, 1, 1, 2, 2],
    ],
]

shortest_length = [3, 5, -1]


def is_path_valid(map: list[list[int]], path: list[tuple[int, int]]) -> bool:
    # check whether this path is valid, i.e., the player can reach the exit
    if path is None:
        return False
    if len(path) == 0:
        return False
    HEIGHT = len(map)
    WIDTH = len(map[0]) if HEIGHT > 0 else 0
    # scan the map to find the start and the exit
    player = None
    exit = None
    ROAD = 0
    DOOR = 1
    WALL = 2
    KEY = 3
    EXIT = 4
    PLAYER = 5
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if map[i][j] == PLAYER:
                player = (i, j)
            if map[i][j] == EXIT:
                exit = (i, j)
    num_keys = 0
    last = player
    if path[0] != player:
        return False
    for i in range(1, len(path)):
        # check the element is a tuple with two integers in the range
        if not isinstance(path[i], tuple):
            return False
        if len(path[i]) != 2:
            return False
        if not (0 <= path[i][0] < HEIGHT and 0 <= path[i][1] < WIDTH):
            return False
        # check the current location is adjacent to the last location
        if abs(path[i][0] - last[0]) + abs(path[i][1] - last[1]) != 1:
            return False
        # rules of the game
        if map[path[i][0]][path[i][1]] == WALL:
            return False
        if map[path[i][0]][path[i][1]] == KEY:
            num_keys += 1
            map[path[i][0]][path[i][1]] = ROAD
        if map[path[i][0]][path[i][1]] == DOOR:
            if num_keys == 0:
                return False
            num_keys -= 1
            map[path[i][0]][path[i][1]] = ROAD
        last = path[i]
    if path[-1] != exit:
        return False
    return True


score = []

solution = Solution()
for i, test_case in enumerate(test_cases):
    # deep copy the test case
    test_case_copy = [row.copy() for row in test_case]
    path = solution.shortest_path(test_case_copy)
    if shortest_length[i] == -1:
        if path is None:
            score.append(1)
        else:
            score.append(0)
    else:
        if is_path_valid(test_case, path) and len(path) == shortest_length[i]:
            score.append(1)
        else:
            score.append(0)
print(score)
