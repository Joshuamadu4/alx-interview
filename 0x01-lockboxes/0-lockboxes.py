#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes.
    visited_boxes = set()

    # Define a helper function for DFS.
    def dfs(box):
        visited_boxes.add(box)
        for key in boxes[box]:
            if key not in visited_boxes:
                dfs(key)

    # Start DFS from the first box.
    dfs(0)

    # Check if all boxes have been visited.
    return len(visited_boxes) == len(boxes)

# Test cases from main_0.py
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

