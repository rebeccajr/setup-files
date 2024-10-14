#_______________________________________________________________________
#
import argparse

from classes.color_scheme_creator import ColorSchemeParser

#_______________________________________________________________________

def new_line () -> None:
  print()
#_______________________________________________________________________
if __name__ == '__main__':

  new_line()
  new_line()

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  ColorSchemeParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  color_list: list =\
    args.rgb_list.split()


  print(args.profile_type)
  for color in color_list:
    print (f'{hex(int(color, base=16)):08}')

  #print(type(args))
  print("Test")
