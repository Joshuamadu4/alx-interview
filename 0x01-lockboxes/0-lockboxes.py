#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""

def can_unlock_all(boxes=None):
    """A function that returns True if all boxes in
    boxes can be opened
    """
    if not boxes:
        return False

    # Initialize a set to keep track of keys available
    keys = {0}

    # Iterate through each box and its corresponding index
    for box_id, box in enumerate(boxes):
        for key in box:
            # Check if the key is valid and not the current box
            if key < len(boxes) and key != box_id:
                keys.add(key)

    # If the number of unique keys matches the number of boxes, return True
    if len(keys) != len(boxes):
        return False

    return True

if __name__ == '__main__':
    boxes = [
        [1, 3],
        [2],
        [3, 0],
        [1, 2, 3],
    ]
    print(can_unlock_all(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(can_unlock_all(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(can_unlock_all(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(can_unlock_all(boxes))

