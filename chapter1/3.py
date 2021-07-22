import re

def main():
    st = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    # split_st = re.split(",| ", st)
    split_st = st.split()
    lis = []
    for i in split_st:
        lis.append(i.replace(",", "").replace(".", ""))
    print(lis)
    # split : 区切り文字を１つだけ指定


if __name__ == "__main__":
    main()
