import json
import re

def is_category(text_uk):
    pattern = r"^(.*\[\[Category:.*\]\].*)$"
    result = '\n'.join(re.findall(pattern, text_uk, re.MULTILINE))
    return result

def main():

    filename = 'jawiki-country.json'
    # lis = []
    with open(filename, mode='r') as f:
      for line in f:
        line = json.loads(line)
        # text_uk = line
        # break
        # lis.append(line["title"])
        if line['title'] == 'イギリス':
          text_uk = line['text']
          break
    # print(lis)
    print(text_uk[0:500])

    # result = is_category(text_uk)
    # print(result)

if __name__ == "__main__":
    main()
