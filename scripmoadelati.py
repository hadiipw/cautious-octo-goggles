def shib(x1, x2, y1, y2):
    if (x2 - x1) != 0:
        m = (y2 - y1) / (x2 - x1)
        return m
    else:
        return None

def arz(x1, x2, y1, y2):
    m = shib(x1, x2, y1, y2)
    if m is not None:
        b = y1 - (m * x1)
        return b
    else:
        return None

def moadele(x1, x2, y1, y2):
    m = shib(x1, x2, y1, y2)
    b = arz(x1, x2, y1, y2)
    if m is None:
        khat = f"y = {y1}"
        return khat
    else:
        khat = f"y = {m:.2f}x + {b:.2f}"
        return khat

def Main():
    x1,y1 = map(int,input("please enter x1 , y1: ").split())
    x2,y2 = map(int,input("please enter x2 , y2: ").split())

    m = shib(x1, x2, y1, y2)
    b = arz(x1, x2, y1, y2)
    khat = moadele(x1, x2, y1, y2)

    print(f"moadele khat: {khat}")

Main()