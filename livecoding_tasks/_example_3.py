import random

a = random.sample([1,2,3,4,5,6], 3)
b = random.choices([1,2,3,4,5,6], k=3)
c = random.choice([1,2,3,4,5,6])

print(a)
print(b)
print(c)
print(''.join(random.choice(['1','2','3','4','5','6']) for _ in range(3)))