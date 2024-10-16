#_______________________________________________________________________
#
import argparse
from os import path

from classes.color_scheme_strings import ColorSchemeStrings
from classes.color_scheme_strings import ErrorStrings
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

  #_____________________________________________________________________
  # Parse color inputs to list of strings
  #_____________________________________________________________________
  color_str_list: list = args.rgb_list.split()

  color_count: int = len(color_str_list)

  # Initialize int color list
  rgb_int_list: list = [0] * color_count

  # Convert list of strings to list of ints
  for i in range(color_count):
    rgb_int_list[i] = int(color_str_list[i], base=16)
  #_____________________________________________________________________

  if (args.profile_type == ColorSchemeStrings.GNOME_INPUT):
    gnome_profile: GnomeProfile =\
        GnomeProfile(args.background_color
          , args.foreground_color
          , rgb_int_list)

    out_str: str = gnome_profile.create_color_scheme_str()

    if (args.name):
      out_file_path: str =\
        f'{args.name}.{ColorSchemeStrings.GNOME_OUT_EXT}'

      if (args.out_dir):
        if (not path.isdir(args.out_dir)):
          print(ErrorStrings.INVALID_DIR)
        else:
          out_file_path = path.join(args.out_dir, args.name)

      f = open(out_file_path, 'w')
      f.write(out_str)
      f.close()

      print(out_str)

  print()