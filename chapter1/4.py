import re

def main():
    st = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    # split_st = re.split(",| ", st)
    split_st = st.split()
    check = [0, 4, 5, 6, 7, 8, 14, 15, 18]
    check_id = 0
    lis = {} # 辞書（連想配列の初期化）
    # lis = []
    # co_st = ""
    for i in range(len(split_st)):
        temp = split_st[i].replace(",", "").replace(".", "")
        if i == check_id:
            lis[temp[0]] = i + 1 #辞書に入力
            # co_st += temp[0]
            # lis.append(i + 1)
        else:
            lis[temp[0:2]] = i + 1
            # co_st += temp[0:2]
            # lis.append(i + 1)
            # lis.append(i + 2)
    # print(split_st)
    # print(lis)
    # print(co_st)
    print(lis)
    for i in range(3):
        print("Please input string")
        str = input()
        print("Output string number")
        print(lis.get(str)) # 辞書から取り出す
    # split : 区切り文字を１つだけ指定


if __name__ == "__main__":
    main()
