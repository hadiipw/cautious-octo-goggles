def parvaz(shahr, khat):
    dic = {C: [] for C in shahr}
    for a, b in khat:
        if a in dic:
            dic[a].append(b)
    return dic

n, m = map(int, input("please enter n and m: ").split())

if n < 1 or m < 0:
    print("error")
else:
    print("enter names:")
    shahr = [input(f"C {i + 1}: ").strip() for i in range(n)]
    print("enter khat parvaz: ")
    khat = [tuple(input().split()) for j in range(m)]
    dic = parvaz(shahr, khat)
    print("\nDirect parvaz:")
    for C, D in dic.items():
        count = len(D)
        if D:
            print(f"{C} ({count} parvaz): {', '.join(D)}")
        else:
            print(f"{C} (0 parvaz)")