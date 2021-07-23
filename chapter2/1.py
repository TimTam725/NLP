import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df = pd.read_csv("hightemp.txt", header = None)
    df_rep = df.replace("\t", " ", regex = True)

    print(df)
    print(df_rep)
    # print(df[0][0])
    # print(df[0][1])

if __name__ == "__main__":
    main()
