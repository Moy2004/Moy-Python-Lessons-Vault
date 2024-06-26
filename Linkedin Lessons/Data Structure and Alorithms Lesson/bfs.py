"""
2024 - 5/25
1445 - ذُو ٱلْقَعْدَة - 18

Read Maze
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue


def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessor = {start: None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessor, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, column_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + column_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessor:
                queue.enqueue(neighbour)
                predecessor[neighbour] = current_cell

    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
