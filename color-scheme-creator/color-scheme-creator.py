#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

import argparse

#_______________________________________________________________________
class HelpStrings:
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

  RGB_LIST_HELP_DESC: str =\
    'List of 8 RGB values corresponding to color indices 0 - 7.'

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

def new_line () -> None:
    print()

#_______________________________________________________________________
if __name__ == '__main__':

  new_line()
  new_line()

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  color_list: list =\
    args.rgb_list.split()


  print(args.profile_type)
  for color in color_list:
    print (f'{hex(int(color, base=16)):08}')

  #print(type(args))
  print("Test")
