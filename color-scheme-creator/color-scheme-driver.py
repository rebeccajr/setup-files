#_______________________________________________________________________
#
import argparse

from classes.color_scheme_strings import GnomeProfile
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

  color_str_list: list =\
    args.rgb_list.split()

  color_count: int = len(color_str_list)

  rgb_int_list: list = [0] * color_count

  for color in color_str_list:
    print(f'{hex(int(color, base=16)):08}')

  for i in range(color_count):
    rgb_int_list[i] = int(color_str_list[i], base=16)

  for color in rgb_int_list:
    print(f'{hex(color):08}')

  gnome_profile: GnomeProfile =\
      GnomeProfile(0x000000, 0xFFFFFF, rgb_int_list)

  print(gnome_profile.create_color_scheme_str())