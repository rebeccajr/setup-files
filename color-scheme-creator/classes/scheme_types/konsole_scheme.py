#_______________________________________________________________________
# Konsole color scheme
#_______________________________________________________________________

from classes.rgb_color import RgbColor, RgbConst
from classes.scheme_types.base_scheme import ColorScheme


#_______________________________________________________________________
class KonsoleProfile(ColorScheme):

  OUT_EXT: str = 'colorscheme'

  def __init__(self, intense_bold_: bool = True, *arg):
    super(KonsoleProfile, self).__init__(*arg)

    self.construct_label_list()
    self.intense_bold_ = intense_bold_
    self.normal_colors_: list[int] = self[self.PALETTE][0:8]
    self.intense_colors_: list[int] = self[self.PALETTE][8:16]

    self.color_scheme_str_: str = self.create_color_scheme_str()

    return

  #_____________________________________________________________________
  def construct_label_list(self):
    """
    Construct the list of labels for color scheme.
    """

    self.label_list: list[str] = ['Background', 'BackgroundIntense']

    for i in range(ColorScheme.PALETTE_COLOR_COUNT):
      self.label_list.append(f'Color{i}')
      self.label_list.append(f'Color{i}Intense')

    self.label_list.append('Foreground')
    self.label_list.append('ForegroundIntense')

    return

  #_____________________________________________________________________
  # TODO URGENT account for scheme name
  #_____________________________________________________________________
  def create_simple_entry(self, rgb_color: int, label: str) -> str:
    """
    Creates color entry.

    Parameters
    rgb_color - 24 bit RGB color to represent
    label     - label in color scheme file

    Sample Output
    [Color2Intense]
    Bold=true
    Color=215,0,0
    """

    rgb_map: dict = RgbColor.get_rgb_from_hex(rgb_color)

    red: int = rgb_map[RgbConst.RED_STR]
    grn: int = rgb_map[RgbConst.GRN_STR]
    blu: int = rgb_map[RgbConst.BLU_STR]

    outstr = f'[{label}]'

    # Add Bold configuration if applicable
    if(self.intense_bold_ and ('Intense' in label)):
      outstr = f'{outstr}\nBold=true'

    outstr = f'{outstr}\nColor={red},{grn},{blu}\n\n'

    return outstr

  #_____________________________________________________________________
  def create_color_scheme_str(self
    , bold_bright_colors: bool = False ) -> str:
    """
    Creates color scheme string to be printed to a file.
    """

    out_str: str = ''

    label_index: int = 0

    background_normal_str: str = self.create_simple_entry(
      rgb_color=self[self.BACKGROUND_COLOR]
      , label=self.label_list[label_index])

    label_index = label_index + 1

    background_intense_str: str = self.create_simple_entry(
      rgb_color=self[self.BACKGROUND_COLOR]
      , label=self.label_list[label_index])

    label_index = label_index + 1

    out_str: str = f'{background_normal_str}{background_intense_str}'

    #___________________________________________________________________
    # Iterate through palette and append to out_str
    # Assumption that normal_colors_ and intense_colors_ are same size
    #___________________________________________________________________
    for i in range(len(self.normal_colors_)):

      color_normal_str: str = self.create_simple_entry(
        rgb_color=self.normal_colors_[i]
        , label=self.label_list[label_index])

      label_index = label_index + 1

      color_intense_str: str = self.create_simple_entry(
        rgb_color=self.intense_colors_[i]
        , label=self.label_list[label_index])

      label_index = label_index + 1

      out_str = f'{out_str}{color_normal_str}{color_intense_str}'
    #___________________________________________________________________

    foreground_normal_str: str = self.create_simple_entry(
      rgb_color=self[self.BACKGROUND_COLOR]
      , label=self.label_list[label_index])

    label_index = label_index + 1

    foreground_intense_str: str = self.create_simple_entry(
      rgb_color=self[self.BACKGROUND_COLOR]
      , label=self.label_list[label_index])

    out_str: str = f'{out_str}{foreground_normal_str}{foreground_intense_str}'

    return out_str
