#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = [None] * length

    # loop through tickets to create dictionary
    for ticket in tickets:
        # if ticket.source not in cache:
        cache[ticket.source] = ticket.destination

        # set the head and tail
        if ticket.source == "NONE":
            route[0] = ticket.destination
        elif ticket.destination == "NONE":
            # route[-1] = ticket.source
            route[-1] = ticket.destination
    
    # loop through route
    # route[i + 1] = cache[route[i]] 
    for i, el in enumerate(route[:-2]):
        route[i + 1] = cache[route[i]]

    return route
