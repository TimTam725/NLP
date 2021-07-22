import re

def mk_string(x, y, z):
    return x + "時の" + y + "は" + z
    # return (f"{x}時のとき{y}は{z}")

def main():
    x = str(input())
    y = str(input())
    z = str(input())
    out = mk_string(x, y, z)
    print(out)

if __name__ == "__main__":
    main()
