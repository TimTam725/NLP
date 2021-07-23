import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df = pd.read_csv("hightemp.txt", sep = "\t", header = None)

    print(df)
    print(df[0])
    # print(df[1])
    df[0].to_csv("./col1.txt", header = None, index = None)
    df[1].to_csv("./col2.txt", header = None, index = None)

if __name__ == "__main__":
    main()
