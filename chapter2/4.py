import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df1 = pd.read_csv("mercol.txt",sep = "\t", header = None)
    print("please input n")
    n = int(input())
    print(df1[:n])
    print(df1.head(n))

if __name__ == "__main__":
    main()
