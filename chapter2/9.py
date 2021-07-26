import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df = pd.read_csv("hightemp.txt",sep = "\t", header = None)
    print(df)
    print(df[0].value_counts())

if __name__ == "__main__":
    main()
