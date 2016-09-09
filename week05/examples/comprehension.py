## [subcode]

lst = [1, 2, 3]

sq = []
for x in lst:
    sq.append(x * x)
print (sq)

## [subcode]
lst = [1, 2, 3, 4, 5, 6]

sq = [x * x for x in lst]

print (sq)

## [subcode]

lst = [1, 2, 3, 4, 5, 6]

sq = []

for x in lst:
    if x % 2 == 0:
        sq.append(x*x)

print (sq)

## [subcode]

lst = [1, 2, 3, 4, 5, 6]

sq = [x*x for x in lst if x % 2 == 0]

print (sq)

## [subcode]

d = {}
for x in range(1, 16):
    d[x] = x*x

print(d)

## [subcode]

d = {x: x*x for x in range(1, 16)}
print(d)

## [subcode]

data = [input() for x in range(3)]
print(data)
