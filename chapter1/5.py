import re

def main():
    st = "I am an NLPer"
    split_st = st.split()
    str = ""
    word_bi = []
    al_bi = []
    # word
    for i in range(len(split_st) - 1):
        word_bi.append(split_st[i] + split_st[i + 1])
    for i in split_st:
        str += i
    for i in range(len(str) - 1):
        al_bi.append(str[i] + str[i + 1])

    print(word_bi)
    print(al_bi)

if __name__ == "__main__":
    main()
