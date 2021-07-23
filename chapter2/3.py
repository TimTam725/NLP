import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df1 = pd.read_csv("col1.txt", header = None)
    df2 = pd.read_csv("col2.txt", header = None)

    df_con = pd.concat([df1, df2], axis = 1)

    print(df_con)
    df_con.to_csv("./mercol.txt", index = None, header = None, sep = "\t")

if __name__ == "__main__":
    main()
