def input_get():
    string = input()
    char = input()
    count = int(input())
    return string, char, count


def char_count(string, char, count):
    index = 0
    for x in range(len(string)):
        if(string[x] == char):
            count -= 1
            if count == 0:
                index = x+1
                break
    return index, count


def display(value, string):
    for x in range(value, len(string)):
        print(string[x], end="")


test_case = int(input())

for test in range(test_case):
    string, char, count = input_get()
    index, count = char_count(string, char, count)
    if count == 0 and index < len(string)-1:
        display(index, string)
        print()
    else:
        print("Empty string")
