import random

def main():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    s_spl = s.split()
    p = ""
    for i in s_spl:
        if len(i) < 4:
            p += i
        else:
            p += i[0] + "".join(random.sample(i[1:-1], len(i) - 2)) + i[-1]
        p += " "

    print(p)

if __name__ == "__main__":
    main()
