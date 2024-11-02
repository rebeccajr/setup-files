#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

import argparse
from os import getcwd

from utilities.color_scheme_utils import GeneralUtils
from classes.rgb_color import RgbConst


#_______________________________________________________________________
class ParserStrings:

  PROGRAM_NAME: str =\
    'Color Scheme Creator'

  PROGRAM_DESC: str =\
    'This program creates color scheme files in the format of several '\
    'terminal programs.'

  PROGRAM_EPI:  str =\
    'This is the epilog to the help menu.'

  PROFILE_TYPE_HELP_DESC: str =\
    'Type of profile, e.g. Gnome, Konsole'

  PROFILE_TYPES: list =\
    [ 'gnome'
    , 'konsole'
    ]

  CMD_LINE_ENTRY_GROUP_TITLE: str =\
    'Command Line Color Entry'

  CMD_LINE_ENTRY_GROUP_DESC: str =\
    'Argument group for command line entry'

  BACKGND_HELP_DESC: str =\
    'Background color'

  FOREGND_HELP_DESC: str =\
    'Foreground color'

  RGB_LIST_HELP_DESC: str =\
    'List of 16 RGB values corresponding to color indices 0 - 15.'

  OUT_FILE_HELP_DESC: str =\
    'Base name of ouput file. Do not include extension.'

  OUT_DIR_HELP_DESC: str =\
    'Directory to put output file.'

  COLOR_JASON_HELP_DESC: str =\
    'Path to json file containing the foreground, background, '\
    'and pallette. Should not be used  if the '\
    f'{CMD_LINE_ENTRY_GROUP_TITLE} argument group is entered.'\
    '\nExample:'\
    '\n{ "background": "0x282828"'\
    '\n  , "foreground": "0xDF5f87"'\
    '\n  , "pallette":["0x5f0000"'\
    '\n    , "0xFF5f00"'\
    '\n    , "0x5fFF00"'\
    '\n    , "0xFFFF5f"'\
    '\n    , "0x5f00FF"'\
    '\n    , "0xFF5fFF"'\
    '\n    , "0x5fFFFF"'\
    '\n    , "0xFFFFFF"'\
    '\n    , "0x5f0000"'\
    '\n    , "0xFF5f00"'\
    '\n    , "0x5fFF00"'\
    '\n    , "0xFFFF5f"'\
    '\n    , "0x5f00FF"'\
    '\n    , "0xFF5fFF"'\
    '\n    , "0x5fFFFF"'\
    '\n    , "0xFFFFFF"'\
    '\n  ]'\
    '\n}'\

  GNOME_INPUT: str = 'gnome'

  KONSOLE_INPUT: str = 'konsole'

  COLOR_RANGE: str = '{0x000000-0xFFFFFF}'

  DEFAULT_NAME: str = 'color-scheme-name'


#_______________________________________________________________________
class ColorSchemeParser:

  #_______________________________________________________________________
  def init_parser(parser: argparse.ArgumentParser) -> None:
    """
    Initializes the argument parser.
    """
    parser.prog = ParserStrings.PROGRAM_NAME
    parser.epilog = ParserStrings.PROGRAM_EPI
    parser.description = ParserStrings.PROGRAM_DESC

    parser.add_argument( '--profile_type'
      , help=ParserStrings.PROFILE_TYPE_HELP_DESC
      , action='store'
      , type=str
      , required=False
      , default=ParserStrings.GNOME_INPUT
      , choices=ParserStrings.PROFILE_TYPES
    )

    # Add type, move strings to class
    cmd_line_group = parser.add_argument_group(\
      ParserStrings.CMD_LINE_ENTRY_GROUP_TITLE
       , ParserStrings.CMD_LINE_ENTRY_GROUP_DESC)

    cmd_line_group.add_argument('--background_color'
      , help=ParserStrings.BACKGND_HELP_DESC
      , action='store'
      , type=GeneralUtils.hex_int
      , required=False
      , default=RgbConst.DEFAULT_BACKGROUND
      , choices=range(0, GeneralUtils.MAX_COLOR + 1)
      , metavar=ParserStrings.COLOR_RANGE
    )

    cmd_line_group.add_argument('--foreground_color'
      , help=ParserStrings.FOREGND_HELP_DESC
      , action='store'
      , type=GeneralUtils.hex_int
      , required=False
      , default=RgbConst.DEFAULT_FOREGROUND
      , choices=range(0, GeneralUtils.MAX_COLOR + 1)
      , metavar=ParserStrings.COLOR_RANGE
    )

    cmd_line_group.add_argument('-rgb'
      , '--rgb_list'
      , help=ParserStrings.RGB_LIST_HELP_DESC
      , action='store'
      , type=str
      , required=False
      , default=RgbConst.DEFAULT_RGB_STR_LIST
    )

    cmd_line_group.add_argument('--name'
      , help=ParserStrings.OUT_FILE_HELP_DESC
      , action='store'
      , type=str
      , required=False
      , default=ParserStrings.DEFAULT_NAME
    )

    cmd_line_group.add_argument('--out_dir'
      , help=ParserStrings.OUT_DIR_HELP_DESC
      , action='store'
      , type=str
      , default=getcwd()
    )

    parser.add_argument('--file'
      , help=ParserStrings.COLOR_JASON_HELP_DESC
      , action='store'
      , type=str
      , required=False
    )

    return

