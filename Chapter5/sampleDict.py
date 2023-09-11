ppl = {}

def addNames(name, age):
  # present = ppl.get(name)
  # print("Present",present)
  if not ppl.get(name):
    ppl[name]=age

print(ppl)
addNames('GSU',23)
ppl['GSU'] = 23
addNames('GSU',45)
print(ppl)