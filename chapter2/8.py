import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df = pd.read_csv("hightemp.txt",sep = "\t", header = None)
    print(df)
    df.sort_values(by=3, ascending = False, inplace = True)
    print(df)


if __name__ == "__main__":
    main()
