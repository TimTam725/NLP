import pandas as pd
import json

def main():

    filename = 'jawiki-country.json'
    with open(filename, mode='r') as f:
      for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
          text_uk = line['text']
          break
    print(text_uk)
    print(type(text_uk))
    # json_open = open("jawiki-country.json", mode = "r")
    # json_load = json.load(json_open)
    # print(type(json_open))

if __name__ == "__main__":
    main()
