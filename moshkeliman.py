def moshkel1(char):
    dic = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    return dic[char]


def moshkel2(number):
    if number >= 4.5:
        return 'A'
    elif number >= 3.5:
        return 'B'
    elif number >= 2.5:
        return 'C'
    elif number >= 1.5:
        return 'D'
    elif number >= 0.5:
        return 'E'
    else:
        return 'F'


n = int(input("please enter n: "))
w = 0
s = 0

for i in range(n):
    char = input("please enter char: ")
    nomre = input("please enter nomre: ")
    nomre = int(nomre)
    w += nomre
    s += nomre * moshkel1(char)

ave_nomre = s / w
ave_char = moshkel2(ave_nomre)

print("ave is: ", ave_char)
