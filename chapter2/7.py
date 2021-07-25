import pandas as pd

def main():

    # df = pd.read_csv("hightemp.txt", header = None)
    df1 = pd.read_csv("mercol.txt",sep = "\t", header = None)

    s = set(df1[0])
    print(s)
    
if __name__ == "__main__":
    main()
