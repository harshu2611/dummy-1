try:
    value_1 = int(input("enter the value:"))
except:
    print("the value entered is wrong:")
    value_1 = 0

try:
    value_2 = int(input("enter the value:"))
except:
    print("the value entered is wrong:")
    value_2 = 0

try:
    value_3 = int(input("enter the value:"))
except:
    print("the value entered is wrong:")
    value_3 = 0


def add(value_1,value_2):
    answer = value_1 + value_2
    print("the answer is:", answer)
    return answer

c = add(value_1,value_2)

add(c, value_3)
