def get_two_ints_user():
    a = int(input("First number:"))
    b = int(input("Second number:"))
    return [a, b]


def main():
    print("Calculator for ggT \n")
    numbers = get_two_ints_user()
    a = numbers[0]
    b = numbers[1]

    print(ggT_bitshift(a, b))
    print(euklid(a, b))


def ggT_bitshift(a, b):
    if a == b:
        return a
    elif (a & 1 == 0) and (b & 1 == 0):
        return ggT_bitshift(int(a/2), int(b/2))
    elif (a & 1 == 0) and (b & 1 == 1):
        return ggT_bitshift(int(a/2), b)
    elif b > a:
        return ggT_bitshift(b, a)
    else:
        return ggT_bitshift(a-b, b)


def euklid(a, b, r=0, s=1, T=0, u=0, v=1):
    print([a, b, r, s, T, u, v])
    if b == 1:
        return [a, b, r, s, T, u, v]
    # old_b = b
    r = int(a/b)
    # b = a - (b * r)
    # a = old_b
    # old_u = u
    # old_v = v
    # u = s - (r * u)
    # v = T - (r * v)
    # s = old_u
    # T = old_v
    #             a,      b     , r, s, T,      u     ,     v
    return euklid(b, a - (b * r), r, u, v, s - (r * u), T - (r * v))


if __name__ == "__main__":
    # execute only if run as a script
    main()
