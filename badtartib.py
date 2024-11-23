def badtartib(vorodi):
    letters = []
    digits = []
    specials = []

    for char in vorodi:
        if char==" ":
            continue
        elif char.isalpha():
            letters.append(char)
        elif char.isdigit():
            digits.append(char)
        else:
            specials.append(char)

    sorted_letters = sorted(letters, key=lambda c: (c.lower(), c))
    sorted_digits = sorted(digits)

    result = ''.join(specials) + ''.join(sorted_letters) + ''.join(sorted_digits)
    return result


vorodi = input("Enter a str: ")

khoroji = badtartib(vorodi)
print("Sorted Output:", khoroji)
