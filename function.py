# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("Average is: ", (x+y)/2)


def average(x=3,y=7):
    # print("Average: ",(x+y)/2)
    z = (x+y)/2
    return z


avg = average(4,10)
print(avg)
print(type(avg))