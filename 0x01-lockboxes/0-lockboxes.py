#!/usr/bin/python3
""" 0-lockboxes module """
from collections import deque


def canUnlockAll(boxes):
    """ a method which determines if all boxes can be opened """
    # Initialize the visited list queue
    visited = [False] * len(boxes)
    visited[0] = True
    queue = deque([0])
    # Loop until the queue is empty
    while queue:
        # Pop the first element
        current_box = queue.popleft()
        # Loop through the adjacent boxes
        for key in boxes[current_box]:
            # Check if the box is visited
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)  # add the newly invitied box to the queue

    # Check if all boxes are visited
    return all(visited)
