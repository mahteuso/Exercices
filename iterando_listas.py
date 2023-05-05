from itertools import chain

a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 10, 11]

c = chain(a, b)

print(next(c))
print(next(c))
print(next(c))

print('iteração  do chain por meio do for')

for n in c:
    print(n)

print('absorvendo todos os valores do chain')
for a in list(c):
    print(a)

def chain(*iters):
    for l in iters:
        yield from l

r = chain(a, b)


print(next(r))
print(next(r))
print(next(r))
