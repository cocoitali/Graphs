def bft(start_node):
# make a queue, so the nodes we are about to visit can wait in line
    q = Queue()

    # make a set, to track all the nodes we have already visited
    visited = set()

    # enqueue the start node
    q.enqueue(start_node)

    # while queue isn't empty:
    while q.length():
    ##  dequeue whatever is at the front, and this is our current node
        current_node = q.dequeue()
    ## if current node has not yet been visited:
        if current_node not in visited:

    ## mark the current node as visited by putting it in our visited set
            visited.add(current_node)

    ## get all of the current node's friends / neighbors
            neighbors = getNeighbors()

    ## for each of those friends:
            for neighbor in neighbors:
    ## put them into our queue to be visited
                q.enqueue(neighbor)


