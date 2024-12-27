s = """\
AAA
BBB
CCC
DDD
"""

with open("test.txt", "w") as f:
    f.write(s)
    # print("My", "name", "is", "Mike", sep="#", end="!", file=f)

with open("test.txt", "r") as f:
    # print(f.read())
    while True:
        # line = f.readline()
        # print(line, end="")
        chunk = 2
        line = f.read(chunk)
        if not line:
            break
