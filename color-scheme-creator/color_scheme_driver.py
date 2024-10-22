#_______________________________________________________________________
#
import argparse
from os import path

from classes.color_scheme_parser import ColorSchemeParser
from classes.color_scheme_strings import ColorSchemeStrings
from classes.color_scheme_strings import GnomeProfile
from classes.color_scheme_strings import ErrorStrings
from classes.color_scheme_parser import ParserStrings
from utilities.color_scheme_utils import GeneralUtils

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

#_______________________________________________________________________
if __name__ == '__main__':

  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  ColorSchemeParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  #_____________________________________________________________________
  # Parse color inputs to list of strings
  #_____________________________________________________________________
  rgb_int_list: list = GeneralUtils.rgb_str_to_int_list(args.rgb_list)

  #_____________________________________________________________________
  if (args.profile_type == ParserStrings.GNOME_INPUT):

    if(args.file):
      color_scheme_dict: dict =\
        GeneralUtils.read_hex_color_json(args.file)

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