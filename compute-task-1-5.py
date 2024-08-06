commanders = {(4, "Barzak"), (2, "Donesia"), (5, "Zeroza"), (1, "Yggacia"), (3, "Larzon")}

def converter(m):
    t = []
    for l in m:
        t.append(tuple(l))
    return t
    

def sort_by_rank(c):
    for i in range(len(c) - 1):
        for j in range(i,len(c)):
            if c[i][0] < c[j][0]:
                temp = c[i]
                c[i] = c[j]
                c[j] = temp
    return converter(c)
    

def sort_by_name(n):
      for i in range(len(c) - 1):
        for j in range(i,len(c)):
            if c[i][1] > c[j][1]:
                temp = c[i]
                c[i] = c[j]
                c[j] = temp
      return converter(c)
   
b = list(commanders)
t = []
for k in b:
    t.append(list(k))
    
sr = sort_by_rank(t)    
sn = sort_by_name(t)
print(f"Sorted by Rank:{sr}")
print(f"Sorted by Name:{sn}")
