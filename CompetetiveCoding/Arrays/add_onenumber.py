def add_one_to_number(a):
    int_a = int("".join(map(str, a)))
    return list(map(int, str(int_a+1)))


if __name__ == "__main__":
    _, *a = map(int, input("a=").split())
    print(add_one_to_number(a))
