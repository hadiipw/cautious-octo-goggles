def josephus(n=100, k=2):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


def main():
    x = int(input("please enter x: "))
    list = []

    for _ in range(x):
        n = 100
        k = 2

        while True:
            command = input("please enter n,k,*: ")

            if command == "n":
                n = int(input("please enter n: "))
            elif command == "k":
                k = int(input("please enter k: "))
            elif command == "*":
                list.append(josephus(n, k))
                break
            else:
                print("error ")

    print("\noutput:")
    for i in list:
        print(i)


main()