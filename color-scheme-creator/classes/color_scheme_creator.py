#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

import argparse
from .color_scheme_strings import ColorSchemeStrings

class ColorSchemeParser:

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """
    parser.prog = ColorSchemeStrings.PROGRAM_NAME
    parser.epilog = ColorSchemeStrings.PROGRAM_EPI
    parser.description = ColorSchemeStrings.PROGRAM_DESC

    parser.add_argument( '--profile_type'
      , help=ColorSchemeStrings.PROFILE_TYPE_HELP_DESC
      , action='store'
      , type=str
      , choices=ColorSchemeStrings.PROFILE_TYPES
    )

    parser.add_argument('-rgb'
      , '--rgb_list'
      , help=ColorSchemeStrings.RGB_LIST_HELP_DESC
      , action='store'
      , type=str
    )

    return


