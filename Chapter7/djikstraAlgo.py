graph = {}

# Table 1: nodes and beighbours
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# Table 2: cost table
infinity = float('inf')
cost = {}
cost['a'] = 6
cost['b'] = 2
cost['fin'] = infinity

# Table 3: parent table
parent = {}
parent['a'] = 'start'
parent['b'] = 'start'
parent['fin'] = None

processed = []

def find_lowest_cost_node(cost):
  lowest_cost = float('inf')
  lowest_cost_node = None
  for node in cost:
    if cost[node] < lowest_cost and node not in processed:
      lowest_cost = cost[node]
      lowest_cost_node = node
  return lowest_cost_node

node = find_lowest_cost_node(cost)
while node is not None:
  oldCost = cost[node]
  neighbours = graph[node]
  for i in neighbours.keys():

  # for i in graph[node].keys():
    # print(neighbours[i])
    newCost = oldCost + neighbours[i]
    if cost[i] > newCost:
      cost[i] = newCost
      parent[i] = node
  processed.append(node)
  node = find_lowest_cost_node(cost)


    