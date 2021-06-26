""" Algorithms referenced from Caleb Madrigal: https://github.com/calebmadrigal """

from collections import deque

def bfs (graph, start, goal):
    """Return the shortest path from the start to the goal in the graph"""

    if not graph[start]:
        raise AttributeError(f"The source {start} is not in the graph!")
    if not graph[goal]:
        raise AttributeError(f"The target {goal} is not in the graph!")

    visited = set(start)
    queue = deque([start])
    parentMap = {start: None}

    while queue:
        #print(f"FIFO: {queue}")
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor == goal:
                parentMap[neighbor] = current
                print(parentMap)
                return rebuild_path(goal, parentMap)
            
            if neighbor not in visited:
                parentMap[neighbor] = current
                visited.add(neighbor)
                queue.append(neighbor)
    return None

# Rebuild the path going backwards from goal node to start node.
def rebuild_path(current, parentMap, path=[]):
    if current is None: # Reached the start node
        return path
    else:
        return rebuild_path(parentMap[current], parentMap, [current] + path)


def main():
    """
    Test using the graph from: 
    https://commons.wikimedia.org/wiki/File:Graph_with_Chordless_and_Chorded_Cycles.svg
    """

    graph = {
        "a": ["b", "f"],
        "b": ["a", "c", "g"],
        "c": ["b", "d", "g", "l"],
        "d": ["c", "e", "k"],
        "e": ["d", "f"],
        "f": ["a", "e"],
        "g": ["b", "c", "h", "l"],
        "h": ["g", "i"],
        "i": ["h", "j", "k"],
        "j": ["i", "k"],
        "k": ["d", "i", "j", "l"],
        "l": ["c", "g", "k"],
    }
    shortestPath = bfs(graph, 'a', 'k')
    print(shortestPath)

if __name__ == "__main__":
    main()