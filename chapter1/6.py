import re

def ngram(n, lst):
    return set(zip(*[lst[i:] for i in range(n)]))
# def bi_gram(a):
#     a2 = a[1::]
#     return [[i, j] for i, j in zip(a, a2)]

def main():
    a = "paraparaparadise"
    b = "paragraph"
    X = ngram(2, a)
    Y = ngram(2, b)
    set_add = X | Y
    set_mul = X & Y
    set_sub = X - Y
    check_X = ("s", "e") in X
    check_Y = ("s", "e") in Y
    print(X)
    print(Y)
    print(set_add)
    print(set_mul)
    print(set_sub)
    print(check_X)
    print(check_Y)

if __name__ == "__main__":
    main()
