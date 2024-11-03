#_______________________________________________________________________
# Gnome color scheme
#_______________________________________________________________________

from classes.scheme_types.base_scheme import ColorScheme
from classes.rgb_color import RgbConst, RgbColor


#_______________________________________________________________________
class GnomeProfile(ColorScheme):

  OUT_EXT: str = 'dconf'

  def __init__(self, *arg):
    """
    Constructor
    """

    super(GnomeProfile, self).__init__(*arg)
    self.ext_ = GnomeProfile.OUT_EXT
    self.color_scheme_str_: str = self.create_color_scheme_str()

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
    Creates Gnome color scheme string to be printed to a file.
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
      color_entry: str = GnomeProfile.create_color_entry(rgb_dict)

      out_str = f'{out_str}{color_entry}'

      if (i != len(palette) - 1):
        out_str = f'{out_str},'

    return out_str

