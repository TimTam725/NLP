import pandas as pd

def split_file(N, df):
  tmp = df.reset_index(drop=False)
  # print("tmp")
  # print(tmp)
  df_cut = pd.qcut(tmp.index, N, labels=[i for i in range(N)])
  print("df_cut")
  print(df_cut)
  df_cut = pd.concat([df, pd.Series(df_cut, name='sp')], axis=1)

  return df_cut

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    # df1 = pd.read_csv("mercol.txt",sep = "\t", header = None)
    df1 = pd.read_csv("popular-names.txt",sep = "\t", header = None)
    print("please input n")
    n = int(input())
    # for i in range(0, len(df1), n):
    #     print(df1[i:i + n])

    df_cut = split_file(10, df1)
    print(df_cut['sp'].value_counts())
    print(df_cut["sp"])
    # print(df_cut)

if __name__ == "__main__":
    main()
