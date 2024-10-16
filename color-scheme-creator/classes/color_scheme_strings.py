#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

from classes.rgb_color import RgbConst, RgbColor

#_______________________________________________________________________
class ColorSchemeStrings:

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

  BACKGND_HELP_DESC: str =\
    'Background color (int, value 0x000000 - 0xFFFFFF)'

  FOREGND_HELP_DESC: str =\
    'Foreground color (int, value 0x000000 - 0xFFFFFF)'

  RGB_LIST_HELP_DESC: str =\
    'List of 16 RGB values corresponding to color indices 0 - 13.'

  OUT_FILE_HELP_DESC: str =\
    'Base name of ouput file. Do not include extension.'

  OUT_DIR_HELP_DESC: str =\
    'Directory to put output file.'

  GNOME_OUT_EXT: str =\
    'dconf'

  KONSOLE_OUT_EXT: str =\
    'colorscheme'

  GNOME_INPUT: str = 'gnome'

  KONSOLE_INPUT: str = 'konsole'


#_______________________________________________________________________
class ErrorStrings:
  ERROR_STR: str =\
    'ERROR:'

  INVALID_ENTRY: str =\
    f'{ERROR_STR} Invalid argument input.'\
    '\n'

  INVALID_DIR: str =\
    f'{ERROR_STR} Output directory does not exist. File will be '\
    'created in cwd.'\
    '\n'


#_______________________________________________________________________
class KonsoleProfile:

  def create_simple_entry(rgb_color: int) -> str:
    return ''

  def create_konsole_profile(rgb_list: list
    , bold_bright_colors: bool = False) -> str:

    out_str: str = ''

    return out_str


#_______________________________________________________________________
class GnomeProfile:

  color_count_: int = 14

  #_____________________________________________________________________
  def __init__(self
    , backgnd: int
    , foregnd: int
    , rgb_colors: list):

    self.rgb_colors_: list = rgb_colors
    self.foregnd_: int = foregnd
    self.backgnd_: int = backgnd

    return

  #_____________________________________________________________________
  def create_color_entry(rgb_map: dict) -> str:

    red: int = rgb_map[RgbConst.RED_STR]
    grn: int = rgb_map[RgbConst.GRN_STR]
    blu: int = rgb_map[RgbConst.BLU_STR]

    out_str: str =\
      f"'rgb({red}, {grn}, {blu})'"

    return out_str

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates Gnome color profile.

    Parameters
    backgnd: int value of default background color
    foregnd: int value of default foreground color
    rgb_colors: list of 16 default ANSI colors
    """

    backgnd: dict = RgbColor.get_rgb_from_hex(self.backgnd_)
    foregnd: dict = RgbColor.get_rgb_from_hex(self.foregnd_)

    out_str: str = \
      '[/]'\
      f'\nbackground-color={GnomeProfile.create_color_entry(backgnd)}'\
      f'\nforeground-color={GnomeProfile.create_color_entry(foregnd)}'\
      f'\npalette=[{self.create_palette_str()}]'

    return out_str

  #_____________________________________________________________________
  def create_palette_str(self) -> str:
    """
    Creates string for color pallet.
    """

    out_str: str = ''


    for color in self.rgb_colors_:
      rgb_dict: dict = RgbColor.get_rgb_from_hex(color)
      color_entry: str =GnomeProfile.create_color_entry(rgb_dict)
      out_str = f'{out_str}{color_entry}'
      if (color != self.rgb_colors_[-1]):
        out_str = f'{out_str},'

    return out_str

  #_____________________________________________________________________
  if __name__ == 'main':
    print("hello")


