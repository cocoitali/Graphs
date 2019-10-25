
# same goal as bft: visit everyone once, leave no one out, visit no one more than once

def dft(start_node):
    # make a stack
    stack = []
    # make a set for visited nodes
    visited = set()
    # put the start node on the stack
    stack.push(start_node)
    # while the stack isn't empty:
    while len(stack):
        # pop off whatever is on top of the stack, this is our current node
        current_node = stack.pop()
        ## if current node has not yet been visited:
        if current_node not in visited:
            visited.add(current_node)
            print(current_node)
            neighbors = getNeighbors()
            for neighbor in neighbors:
                stack.append(neighbor)
                
            ## mark the current node as visited by putting it in our visited set
             ## get all of the current node's neighbors
            ## for each of those neighbors:
                ## put them into our stack to be visited