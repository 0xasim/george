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
      # https://www.datacamp.com/community/tutorials/python-xml-elementtree
      st = ET.tostring(text, encoding='utf8').decode('utf8')
      n = 0
      if (input_q in st) and (":" not in st):
        n+=1
        time = int(float(text.attrib["start"]))-3
        url = f"https://youtu.be/{ef[:-8]}?t={time}"
        print(f"\u001b]8;;{url}\u001b\\{text.text}\u001b]8;;\u001b\\")

  print(n)

