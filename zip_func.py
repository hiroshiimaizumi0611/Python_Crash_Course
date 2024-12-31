days = ["mon", "tue", "wed"]
fruits = ["apple", "banana", "orange"]
drinks = ["coffe", "tea", "beer"]

# for i in range(len(days)):
# print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
