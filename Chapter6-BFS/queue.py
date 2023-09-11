from collections import deque

def isMangoSeller(name):
  if name[-1] == 'm':
    return True


def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    print("search_queue", search_queue)
    if not name in searched:
      person = search_queue.popleft()
      print(person,"popped")
      if isMangoSeller(person):
        print(person, "is seller.")
        return person
      else:
        search_queue += graph[person]
        searched.append(person)
        print("searched", searched)
        print()
        
  return False


graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['mangom']
graph['claire'] = ['alpha']

# search_queue = deque()
# search_queue += graph['you']
# search_queue += graph['bob']
# print(search_queue)

# if search('you'):
print("Seller - ", search('you'))