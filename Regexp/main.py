import re
import csv
import pandas as pd
from fun import s1

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  names = [' '.join(j[:3]).rstrip().split() for j in contacts_list]
  other = [j for j in contacts_list]
  for i in range(len(other)):
    other[i][:3] = names[i]
  del names

  for ind, i in enumerate(other):
    for j in other[ind+1:]:
      if i[:2] == j[:2]:
        for _ in range(len(i)-1):
          if i[_] == '':
            i[_] = j[_]
        other.remove(j)
  for i in other:
    if i[5] != '':
      if 'доб' in i[5]:
        patern = r'(\+7|8)[-\s]*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})[\s]*(\(*доб.\s*(\d+))*\)*'
        replace = r'+7(\2)\3-\4-\5 доб.\7'
        i[5] = re.sub(patern, replace, i[5])
      else:
        patern = r'(\+7|8)[-\s]*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})'
        replace = r'+7(\2)\3-\4-\5'
        i[5]= re.sub(patern, replace, i[5])

  pd.set_option('display.max_columns', 7)
  pd.set_option('display.expand_frame_repr', False)
  print(pd.DataFrame(other[1:], columns=other[0]))

  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(other)

if __name__ == '__main__':
  s1()