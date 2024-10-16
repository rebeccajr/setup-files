#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

import argparse

from classes.color_scheme_strings import ColorSchemeStrings
from utilities.color_scheme_utils import GeneralUtils


#_______________________________________________________________________
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

    # Add limit
    parser.add_argument('--background_color'
      , help=ColorSchemeStrings.BACKGND_HELP_DESC
      , action='store'
      , type=GeneralUtils.hex_int
      , choices=range(0, GeneralUtils.MAX_COLOR + 1)
    )

    # Add limit
    parser.add_argument('--foreground_color'
      , help=ColorSchemeStrings.FOREGND_HELP_DESC
      , action='store'
      , type=GeneralUtils.hex_int
      , choices=range(0, GeneralUtils.MAX_COLOR + 1)
    )

    parser.add_argument('-rgb'
      , '--rgb_list'
      , help=ColorSchemeStrings.RGB_LIST_HELP_DESC
      , action='store'
      , type=str
    )

    parser.add_argument('--name'
      , help=ColorSchemeStrings.OUT_FILE_HELP_DESC
      , action='store'
      , type=str
    )

    parser.add_argument('--out_dir'
      , help=ColorSchemeStrings.OUT_DIR_HELP_DESC
      , action='store'
      , type=str
    )

    return


