BOARD_SIZE = 3

goal_board = [1, 2, 3, 4, 5, 6, 7, 8, " "]
board3 = [7, 4, 6, 5, 2, 1, 8, 3, " "]
board41 = [1, 2, 3, 4, 5, 6, 7, 8, ' ', 9, 10, 12, 13, 14, 11, 15]
board44 = [1, 2, 3, 4, 5, 6, " ", 7, 8]


def boardSize(num):
    global BOARD_SIZE
    global board
    BOARD_SIZE = num
    for i in range(num**2):
        if i != (num**2) - 1: goal_board.append(i + 1)
        else: goal_board.append(" ")
    board = list(goal_board)


def show_board(board):
    index = board.index(" ")
    for i in range(len(board)):
        print('{:2}'.format(board[i]), end=" ")
        if (i % BOARD_SIZE == BOARD_SIZE - 1):
            print()
    print()


def get_possible_actions(board):
    actions = []
    empty_index = board.index(" ")
    x = empty_index % BOARD_SIZE  # 2
    y = empty_index // BOARD_SIZE  # 3

    if y < ((len(board) - 1) // BOARD_SIZE):
        actions.append("Down")
    if y > 0:
        actions.append("Up")
    if x < ((len(board) - 1) % BOARD_SIZE):
        actions.append("Right")
    if x > 0:
        actions.append("Left")

    return actions


def update_board(board, action):
    empty_index = board.index(" ")

    if action == "Left":
        target = empty_index - 1
    elif action == "Right":
        target = empty_index + 1
    elif action == "Up":
        target = empty_index - BOARD_SIZE
    else:
        target = empty_index + BOARD_SIZE

    board[empty_index], board[target] = board[target], board[empty_index]


def shuffle(board, move_cnt):
    movement = []
    for i in range(move_cnt):
        tmp_action = random.choice(get_possible_actions(board))
        update_board(board, tmp_action)
        movement.append(tmp_action)


def BFS(board):
    visited_states = set()
    root_node = (0, board, None)
    frontier = [root_node]
    loop_cnt = 0
    num_created_successors = 0
    while frontier != []:
        loop_cnt += 1
        node = frontier.pop(0)
        if node[1] == goal_board:
            show_solution(node)
            print("solution is found on level: ", node[0])
            print(loop_cnt, num_created_successors, len(visited_states))
            return
        successors = expand(node[1])
        num_created_successors += len(successors)
        for suc in successors:
            if tuple(suc) not in visited_states:
                visited_states.add(tuple(suc))
                new_node = (node[0] + 1, suc, node)
                frontier.append(new_node)


def show_solution(node):
    path = [node[1]]
    while node[2] != None:
        node = node[2]
        path.append(node[1])
    path.reverse()
    print("solution sequence is...")
    for b in path:
        show_board(b)
    print("solution is found in {} steps".format(len(path) - 1))


def expand(board):
    actions = get_possible_actions(board)
    successors = []
    board_number = 0
    for act in actions:
        board_number += 1
        new_board = board[:]
        update_board(new_board, act)
        #print(new_board)
        successors.append(new_board)
    return successors


def DFS(board):
    visited_states = set()
    root_node = (0, board, None)
    frontier = [root_node]
    loop_cnt = 0
    num_created_successors = 0
    while frontier != []:
        loop_cnt += 1
        node = frontier.pop(0)
        if node[1] == goal_board:
            print(loop_cnt)
            show_solution(node)
            print("solution is found on level: ", node[0])
            print(loop_cnt, num_created_successors, len(visited_states))
            return
        successors = expand(node[1])
        num_created_successors += len(successors)
        for suc in successors:
            if tuple(suc) not in visited_states:
                visited_states.add(tuple(suc))
                new_node = (node[0] + 1, suc, node)
                frontier.insert(0, new_node)


def DFS_limited(board, max_depth):
    visited_states = {}
    root_node = (0, board, None)
    frontier = [root_node]
    loop_cnt = 0
    num_created_successors = 0
    num_used_successors = 0
    while frontier != []:
        loop_cnt += 1
        node = frontier.pop(0)
        if node[1] == goal_board:
            show_solution(node)
            print("solution was found on level: ", node[0])
            print(loop_cnt, num_created_successors, len(visited_states))
            return
        elif max_depth == 0:
            print("Max Depth = 0, no solution found")
            return False
        elif node[0] < max_depth:
            successors = expand(node[1])
            num_created_successors += len(successors)
            for suc in successors:
                if tuple(suc) not in visited_states or node[
                        0] + 1 < visited_states[tuple(suc)]:
                    num_used_successors += 1
                    visited_states[tuple(suc)] = node[0] + 1
                    new_node = (node[0] + 1, suc, node)
                    frontier.insert(0, new_node)

    if frontier == []:
        print("no of loops: ", loop_cnt)
        print("created states: ", len(visited_states))
        print("no of created successors:", num_created_successors)
        print("no of used successors: ", num_used_successors)
        if node[0] == max_depth:
            print("Max depth reached at level ", node[0],
                  "and no solution was found")
        else:
            print("no new states were found between level", node[0],
                  "and max depth", max_depth, "and no solution was found")
        return False


def DFS_Iterative_Deepening(board):
    counter = 1
    while True:
        max_depth = counter
        visited_states = {}
        root_node = (0, board, None)
        frontier = [root_node]
        loop_cnt = 0
        num_created_successors = 0
        num_used_successors = 0
        while frontier != []:
            loop_cnt += 1
            node = frontier.pop(0)
            if node[1] == goal_board:
                show_solution(node)
                print("solution was found on level: ", node[0])
                print("no of loops: ", loop_cnt)
                print("created states: ", len(visited_states))
                print("no of created successors:", num_created_successors)
                print("no of used successors: ", num_used_successors)
                return
            elif node[0] < max_depth:
                successors = expand(node[1])
                num_created_successors += len(successors)
                for suc in successors:
                    if tuple(suc) not in visited_states or node[
                            0] + 1 < visited_states[tuple(suc)]:
                        num_used_successors += 1
                        visited_states[tuple(suc)] = node[0] + 1
                        new_node = (node[0] + 1, suc, node)
                        frontier.insert(0, new_node)
        counter += 1


def show_solution2(node):
    path = [node[3]]
    while node[4] != None:
        node = node[4]
        path.append(node[3])
    path.reverse()
    print("Solution sequences...")
    if len(path) < 100:
        for b in path:
            show_board(b)
    print("Solution in {} steps".format(len(path) - 1))


def heuristic(board):
    count = 0
    for i in range(len(board)):
        if board[i] != goal_board[i]:
            count += 1
    return count


def AStar(board):

    visited_states = {}
    g = 0
    h = heuristic(board)
    root_node = (g + h, h, time.perf_counter(), board, None)
    frontier = [root_node]
    loop_cnt = 0
    num_created_successors = 0
    while frontier != []:
        loop_cnt += 1
        node = heappop(frontier)
        if node[3] == goal_board:
            show_solution2(node)
            print(loop_cnt, num_created_successors, len(visited_states))
            return

        successors = expand(node[3])
        num_created_successors += len(successors)

        for suc in successors:
            h = heuristic(suc)
            g = node[0] - node[1] + 1
            if tuple(suc) not in visited_states or g + h < visited_states[
                    tuple(suc)]:
                visited_states[tuple(suc)] = g + h
                new_node = (g + h, h, time.perf_counter(), suc, node)
                heappush(frontier, new_node)


BFS(board44)

print(get_possible_actions(board44))


# By Montana Mendy for Travis CI 
