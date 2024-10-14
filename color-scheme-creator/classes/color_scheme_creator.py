#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

import argparse
from .color_scheme_strings import HelpStrings

class ColorSchemeParser:

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """
    parser.prog = HelpStrings.PROGRAM_NAME
    parser.epilog = HelpStrings.PROGRAM_EPI
    parser.description = HelpStrings.PROGRAM_DESC

    parser.add_argument( '--profile_type'
      , help=HelpStrings.PROFILE_TYPE_HELP_DESC
      , action='store'
      , type=str
      , choices=HelpStrings.PROFILE_TYPES
    )

    parser.add_argument('-rgb'
      , '--rgb_list'
      , help=HelpStrings.RGB_LIST_HELP_DESC
      , action='store'
      , type=str
    )

    return


