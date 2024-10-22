#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

from classes.rgb_color import RgbConst, RgbColor

#_______________________________________________________________________
class ColorSchemeStrings:
  GNOME_OUT_EXT: str =\
    'dconf'

  KONSOLE_OUT_EXT: str =\
    'colorscheme'

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
class ColorScheme(dict):

  BACKGROUND_COLOR: str = "background-color"
  FOREGROUND_COLOR: str = "foreground-color"
  PALLETTE: str = "pallette"

  def __init__(self
    , backgnd: int
    , foregnd: int
    , rgb_colors: list):

    self[ColorScheme.BACKGROUND_COLOR] = backgnd
    self[ColorScheme.FOREGROUND_COLOR] = foregnd
    self[ColorScheme.PALLETTE] = rgb_colors

    return

#_______________________________________________________________________
class KonsoleProfile:

  def create_simple_entry(rgb_color: int) -> str:
    return ''

  def create_konsole_profile(rgb_list: list
    , bold_bright_colors: bool = False) -> str:

    out_str: str = ''

    return out_str


#_______________________________________________________________________
class GnomeProfile(ColorScheme):

  color_count_: int = 14

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

    BACKGND: str = ColorScheme.BACKGROUND_COLOR
    FOREGND: str = ColorScheme.FOREGROUND_COLOR
    PALLETTE: str = ColorScheme.PALLETTE

    backgnd: dict = RgbColor.get_rgb_from_hex(self[BACKGND])
    foregnd: dict = RgbColor.get_rgb_from_hex(self[FOREGND])

    out_str: str = \
      '[/]'\
      f'\n{BACKGND}={GnomeProfile.create_color_entry(backgnd)}'\
      f'\n{FOREGND}={GnomeProfile.create_color_entry(foregnd)}'\
      f'\n{PALLETTE}=[{self.create_palette_str()}]'

    return out_str

  #_____________________________________________________________________
  def create_palette_str(self) -> str:
    """
    Creates string for color pallet.
    """

    out_str: str = ''


    for color in self[ColorScheme.PALLETTE]:
      rgb_dict: dict = RgbColor.get_rgb_from_hex(color)
      color_entry: str =GnomeProfile.create_color_entry(rgb_dict)
      out_str = f'{out_str}{color_entry}'
      if (color != self[ColorScheme.PALLETTE][-1]):
        out_str = f'{out_str},'

    return out_str

  #_____________________________________________________________________
  if __name__ == 'main':
    print("hello")


