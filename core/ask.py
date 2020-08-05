import os
import xml.etree.ElementTree as ET

def get_files(dir):
  f = []
  for (_, _, filename) in os.walk(dir):
    f.extend(filename)
    break
  return f

def ask_query(input_q):
  print("i am ask query")

def ask_prompt(input_q, dir, files):
  for ef in files:
    tree = ET.parse(os.path.join(dir, ef))
    root = tree.getroot()
    for text in root:
      st = ET.tostring(text, encoding='utf8').decode('utf8')
      n = 0
      if (input_q in st) and (":" not in st):
        n+=1
        print(st)

#      if (input_q in text.text) and (":" not in text.text):
#        print(text.text)

  print(n)

