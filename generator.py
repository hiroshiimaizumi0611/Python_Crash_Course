# l = ["morning", "afternoon", "night"]

# for i in l:
#     print(i)


# print("##################")


def counter(num=10):
    for _ in range(num):
        yield "run"


def greeting():
    yield "morning"
    yield "afternoon"
    yield "night"


for g in greeting():
    print(g)

print("##################")

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(g))
print(next(c))
