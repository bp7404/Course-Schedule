"""
You have to complete n courses. There are m requirements of the form "course a has to be completed before course b". Your task is to find an order in which you can complete the courses.

Input
The first input line has two integers n and m: the number of courses and requirements. The courses are numbered 1,2, ... ,n.
After this, there are m lines describing the requirements. Each line has two integers a and b: course a has to be completed before course b.

Output
Print an order in which you can complete the courses. You can print any valid order that includes all the courses.
If there are no solutions, print "IMPOSSIBLE".

"""

from collections import defaultdict, deque

def find_course_order(n, m, prerequisites):
    """
    Determines an order in which courses can be completed based on prerequisites.

    This function takes the number of courses and their dependencies (prerequisites)
    and uses topological sorting to find a valid order to complete the courses. 
    If no valid order exists, the function returns "IMPOSSIBLE".

    Args:
        n (int): The total number of courses, numbered from 1 to n.
        m (int): The number of prerequisite relationships between courses.
        prerequisites (list of tuples): A list of pairs (a, b), where course `a` must be 
                                         completed before course `b`.

    Returns:
        list or str: A list representing a valid order to complete the courses, or 
                     "IMPOSSIBLE" if no such order exists.
    """    

    # Adjacency list to represent the graph
    # Default value : empty list
    graph = defaultdict(list)

    # In-degree list to keep track of prerequisites for each course
    in_degree = [0] * (n + 1)
    
    # Build the graph and calculate in-degrees
    for a, b in prerequisites:
        # Add new key, value is the list
        graph[a].append(b)
        in_degree[b] += 1

    # Queue for courses with no prerequisites
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)
    
    # Topological sort
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)
        
        # Decrease the in-degree of neighboring courses
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the number of courses in the order is less than n, it's impossible
    if len(order) != n:
        return "IMPOSSIBLE"
    
    return order


# ------------
# Input data
# ------------
n, m = map(int, input().split())
prerequisites = []
for _ in range(m):
    a, b = map(int, input().split())
    prerequisites.append((a, b))

# Calculate the course order
result = find_course_order(n, m, prerequisites)

# ------------
# Output
# ------------
if result == "IMPOSSIBLE":
    print(result)
else:
    print(" ".join(map(str, result)))
