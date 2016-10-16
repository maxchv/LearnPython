
def generator():
    print("prepera generator")
    for i in range(10):
        print("yield {}".format(i))
        yield i

g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))
#print(next(g))
# for i in generator():
#     print(i)

def generate_inner(obj):
    for inner in obj:
        yield from inner
        # for item in inner:
        #     yield item

for item in generate_inner([(1,2),[10,20],[100,200]]):
    print(item)

lst = ["first", "secont", "third"]
for idx, item in enumerate(lst):
    print("idx = {} value = {}".format(idx, item))