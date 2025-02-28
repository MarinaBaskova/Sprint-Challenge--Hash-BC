#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    source = hash_table_retrieve(hashtable, "NONE")
    route[0] = source

    i = 1
    while source != "NONE":
        destination = hash_table_retrieve(hashtable, source)

        source = destination
        route[i] = destination

        i += 1

    return route
