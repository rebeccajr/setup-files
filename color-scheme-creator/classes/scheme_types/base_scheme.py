#_______________________________________________________________________
# Base class for color schemes
#_______________________________________________________________________

from classes.rgb_color import RgbConst
from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class ColorScheme(dict):

  BACKGROUND_COLOR: str = "background-color"
  FOREGROUND_COLOR: str = "foreground-color"
  PALETTE: str = "palette"

  PALETTE_COLOR_COUNT: int = 8

  #_____________________________________________________________________
  def __init__(self, *arg):

    self[ColorScheme.BACKGROUND_COLOR] = RgbConst.DEFAULT_BACKGROUND
    self[ColorScheme.FOREGROUND_COLOR] = RgbConst.DEFAULT_FOREGROUND
    self[ColorScheme.PALETTE] = RgbConst.DEFAULT_RGB_INT_LIST

    #___________________________________________________________________
    # Default with no arguments
    #___________________________________________________________________
    if (not len(arg)):
      return


    #___________________________________________________________________
    if (isinstance(arg[0], dict)):
      self.construct_from_json(arg[0])

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
    # Third argument is assumed to be a string containing white space
    # separated hex int strings, used when command line input.
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

  #_____________________________________________________________________
  def construct_from_json(self, input_dict: dict):
    """
    Constructs color scheme from dictionary created from json.
    """
    try:
      self[ColorScheme.BACKGROUND_COLOR] =\
        Utils.str_hex_to_int(input_dict[ColorScheme.BACKGROUND_COLOR])

    except TypeError:
      pass

    #___________________________________________________________________
    try:
      self[ColorScheme.FOREGROUND_COLOR] =\
        Utils.str_hex_to_int(input_dict[ColorScheme.FOREGROUND_COLOR])

    except TypeError:
      pass

    #___________________________________________________________________
    try:
      color_palette: list = input_dict[ColorScheme.PALETTE]

      if (len(color_palette)):

        # Assumption that color palette is list of hex strings
        if (isinstance(color_palette[0], str)):
          self[ColorScheme.PALETTE] =\
          Utils.str_list_to_hex_list(color_palette)

        #_______________________________________________________________
        # TODO modify function to take other types of dicts
        #      currently shouldn't ever enter this branch
        #_______________________________________________________________
        # Assumption that color palette is list of ints
        elif (isinstance(color_palette[0], int)):
          self[ColorScheme.PALETTE] = color_palette

    except TypeError:
      pass

    return

  #_____________________________________________________________________
  # TODO is this being used?
  #_____________________________________________________________________
  def construct(self, json_file: dict):
    json_file = json_file[0]
    Cs = ColorScheme
    background: int = Utils.str_hex_to_int(json_file[Cs.BACKGROUND_COLOR])
    foreground: int = Utils.str_hex_to_int(json_file[Cs.FOREGROUND_COLOR])
    rgb_color_str_list: str = json_file[Cs.PALETTE]

    self.construct(background, foreground, rgb_color_str_list)
