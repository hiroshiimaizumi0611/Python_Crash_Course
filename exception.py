l = [1, 2, 3]
i = 5

try:
    () + l
except IndexError as ex:
    print("Dont worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other:{}".format(ex))
else:
    print("done")
finally:
    print("clean up")
