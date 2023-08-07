#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize a set to keep track of the unlocked boxes.
    unlocked_boxes = set([0])

    # Initialize a queue to perform BFS on the boxes and find keys.
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    # Check if all boxes can be unlocked.
    return len(unlocked_boxes) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
print(canUnlockAll(boxes2))  # Output: False

