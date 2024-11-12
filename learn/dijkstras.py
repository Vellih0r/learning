graph = {}
graph['Start'] = {}
graph['Start']['a'] = 6
graph['Start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

infinity = float("inf")

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = ['Start', 'b']
parents['b'] = ['Start']
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs):
    min = infinity
    min_node = None
    for node, val in costs.items():
        if val < min:
            min = val
            min_node = node
    return min_node
        


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs['fin'])