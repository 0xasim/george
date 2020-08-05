#!/usr/bin/env python3
from core import ask, update
import argparse

def main(args):
  dir = "subtitles"                                 #output directory
  if args['query']:
    ask.ask_query(args['query'])
  
  if args['update']:
    url = "https://www.youtube.com/c/commaaiarchive/" #channel url
    update.confirm_directory(dir)
    update.get_subtitles(url, dir)

  if args['prompt']:
    files = ask.get_files(dir)
    while True:
       i = input('>>> ')
       ask.ask_prompt(input_q=i, dir=dir, files=files)

if __name__=="__main__":
  parser = argparse.ArgumentParser(description="Ask george something...")
  parser.add_argument('query', metavar='q', type=str, nargs='?', help="Query to ask")
  parser.add_argument('--update', '-u', dest='update', action='store_true', help="Update subtitle files (should be done if a new video arrives)")
  parser.add_argument('--prompt', '-p', dest='prompt', action='store_true', help="Enter into a prompt to repeatdly ask something")
  args = vars(parser.parse_args())
  main(args)
