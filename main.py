from random import randint 
from timer import timer

n = int(input())
l = []
for _ in range(n):
  l.append(randint(10,1000000))

@timer
def bubblesort(list):
  for i in range(n):
      for j in range(0, n-i-1):
        if l[j] > l[j+1]:
          l[j], l[j+1] = l[j+1], l[j]
    
  return l 

@timer
def quicksort(l):
  if len(l) <= 1:
    return l
  pivot = l[len(l) // 2]
  left = [x for x in l if x < pivot]
  middle = [x for x in l if x == pivot]
  right = [x for x in l if x > pivot]
  return quicksort(left) + middle + quicksort(right)


print(l)
print(bubblesort(l))
#print(quicksort(l))