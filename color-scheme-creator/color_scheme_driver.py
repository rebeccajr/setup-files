#_______________________________________________________________________
#
import argparse
from os import path

from classes.color_scheme_parser import ColorSchemeParser
from classes.color_scheme_parser import ParserStrings

from classes.color_scheme_strings import ColorSchemeStrings
from classes.color_scheme_strings import ErrorStrings

from classes.scheme_types.base_scheme import ColorScheme
from classes.scheme_types.gnome_scheme import GnomeProfile
from classes.scheme_types.konsole_scheme import KonsoleProfile

from utilities.color_scheme_utils import GeneralUtils as Utils

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

#_______________________________________________________________________
if __name__ == '__main__':

  new_line(2)

  #_____________________________________________________________________
  # TODO create unit test framework
  #_____________________________________________________________________
  # print(GeneralUtils.str_hex_to_int('g'))
  # print(GeneralUtils.str_hex_to_int('0x00000F'))
  #_____________________________________________________________________

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  ColorSchemeParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  if (args.profile_type == ParserStrings.GNOME_INPUT):
    SchemeType = GnomeProfile

  elif (args.profile_type == ParserStrings.KONSOLE_INPUT):
    SchemeType = KonsoleProfile

  if(args.file):
    color_scheme = SchemeType(Utils.read_hex_color_json(args.file))

  else:
    color_scheme =\
      SchemeType(args.background_color
        , args.foreground_color
        , args.rgb_list)


  out_file_path: str =\
    f'{args.name}.{SchemeType.OUT_EXT}'

  if (args.out_dir):
    if (not path.isdir(args.out_dir)):
      print(ErrorStrings.INVALID_DIR)
    else:
        out_file_path = path.join(args.out_dir, out_file_path)

    f = open(out_file_path, 'w')
    f.write(color_scheme.color_scheme_str_)
    f.close()

    print(color_scheme.color_scheme_str_)
    print("!!!!")