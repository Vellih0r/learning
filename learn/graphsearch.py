from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "clarie"]
graph["alice"] = ["jhon", "mike"]
graph["bob"] = ["peggy", "mike"]
graph["clarie"] = ["jhonny", "thom"]
graph["jhon"] = []
graph["mike"] = []
graph["peggy"] = []
graph["jhonny"] = []
graph["thom"] = []


def isMangoSeller(name):
    print(name)
    return name[-1] == 'm'


def Search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if isMangoSeller(person):
                print(person, " is mango seller")
                return True
            else:
                search_queue += graph[person]
                search_queue.append(person)
    return False
    

print(Search("you"))