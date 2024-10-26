#_______________________________________________________________________
# This program creates color scheme files in the format of several
# terminal programs.
#_______________________________________________________________________

from classes.rgb_color import RgbConst, RgbColor
from utilities.color_scheme_utils import GeneralUtils as Utils

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
  PALETTE: str = "palette"

  #_____________________________________________________________________
  def __init__(self, *arg):

    self[ColorScheme.BACKGROUND_COLOR] = RgbConst.DEFAULT_BACKGROUND
    self[ColorScheme.FOREGROUND_COLOR] = RgbConst.DEFAULT_FOREGROUND
    self[ColorScheme.PALETTE] = RgbConst.DEFAULT_RGB_INT_LIST

    if (not len(arg)):
      return

    #___________________________________________________________________
    if (isinstance(arg[0], dict)):
      self.construct_from_dict(arg[0])

    #___________________________________________________________________
    if (isinstance(arg[0], int)):
        self[ColorScheme.BACKGROUND_COLOR] = arg[0]

    #___________________________________________________________________
    if (len(arg) > 1):
      try:
        self[ColorScheme.FOREGROUND_COLOR] = arg[1]
      except TypeError:
        pass

    #___________________________________________________________________
    if (len(arg) > 2):
      try:
        rgb_colors: str = arg[2]

        rgb_color_str_list: list[str] = rgb_colors.split()

        self[ColorScheme.PALETTE] =\
          Utils.str_list_to_hex_list(rgb_color_str_list)

      except TypeError:
        pass

    return

  #___________________________________________________________________
  def construct_from_dict(self, input_dict: dict):
    """
    Constructs color scheme from dictionary created from json.
    """
    try:
      self[ColorScheme.BACKGROUND_COLOR] =\
        Utils.hex_int(input_dict[ColorScheme.BACKGROUND_COLOR])

    except TypeError:
      pass

    #_________________________________________________________________
    try:
      self[ColorScheme.FOREGROUND_COLOR] =\
        Utils.hex_int(input_dict[ColorScheme.FOREGROUND_COLOR])

    except TypeError:
      pass

    #_________________________________________________________________
    try:
      color_pallette: list = input_dict[ColorScheme.PALETTE]

      if (len(color_pallette)):

        # Assumption that color pallette is list of ints
        if (isinstance(color_pallette[0], int)):
          self[ColorScheme.PALETTE] = color_pallette

        # Assumption that color pallette is list of hex strings
        elif (isinstance(color_pallette[0], str)):
          self[ColorScheme.PALETTE] =\
          Utils.str_list_to_hex_list(color_pallette)

    except TypeError:
      pass

    return

  #_____________________________________________________________________
  def construct(self, json_file: dict):
    json_file = json_file[0]
    Cs = ColorScheme
    background: int = Utils.hex_int(json_file[Cs.BACKGROUND_COLOR])
    foreground: int = Utils.hex_int(json_file[Cs.FOREGROUND_COLOR])
    rgb_color_str_list: str = json_file[Cs.PALETTE]

    self.construct(background, foreground, rgb_color_str_list)


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
    PALETTE: str = ColorScheme.PALETTE

    backgnd: dict = RgbColor.get_rgb_from_hex(self[BACKGND])
    foregnd: dict = RgbColor.get_rgb_from_hex(self[FOREGND])

    out_str: str = \
      '[/]'\
      f'\n{BACKGND}={GnomeProfile.create_color_entry(backgnd)}'\
      f'\n{FOREGND}={GnomeProfile.create_color_entry(foregnd)}'\
      f'\n{PALETTE}=[{self.create_palette_str()}]'

    return out_str

  #_____________________________________________________________________
  def create_palette_str(self) -> str:
    """
    Creates string for color pallet.
    """

    out_str: str = ''

    palette: list[int] = self[ColorScheme.PALETTE]

    for i in range(len(palette)):
      color: int = palette[i]
      rgb_dict: dict = RgbColor.get_rgb_from_hex(color)
      color_entry: str =GnomeProfile.create_color_entry(rgb_dict)

      out_str = f'{out_str}{color_entry}'

      if (i != len(palette) - 1):
        out_str = f'{out_str},'

    return out_str

  #_____________________________________________________________________
  if __name__ == 'main':
    print("hello")


