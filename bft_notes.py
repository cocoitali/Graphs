def bft(start_node):
# make a queue, so the nodes we are about to visit can wait in line
    q = Queue()

    # make a set, to track all the nodes we have already visited
    visited = set() # use a set to get unique values, no duplicates

    # enqueue the first node
    q.enqueue(start_node)

    # while queue isn't empty:
    while q.length():
    ##  dequeue whatever is at the front, and this is our current node
        current_node = q.dequeue()
    ## if current node has not yet been visited:
        if current_node not in visited:

    ## mark the current node as visited by putting it in our visited set
            visited.add(current_node)
            print(current_node)

    ## get all of the current node's neighbors
            neighbors = getNeighbors()

    ## for each of those neighbors:
            for neighbor in neighbors:
    ## put them into our queue to be visited
                q.enqueue(neighbor)

## And that's all there is to it!

# Time Complexity : O(E + V) Linear


