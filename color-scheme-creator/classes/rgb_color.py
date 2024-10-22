#_______________________________________________________________________
# Contains operations related to RGB colors
#_______________________________________________________________________

class RgbConst:

  RED_STR: str = 'RED'
  GRN_STR: str = 'GRN'
  BLU_STR: str = 'BLU'

  RED_MASK: str = 0xFF0000
  GRN_MASK: str = 0x00FF00
  BLU_MASK: str = 0x0000FF

  RED_RIGHT_SHIFT: int = 16
  GRN_RIGHT_SHIFT: int = 8
  BLU_RIGHT_SHIFT: int = 0

  DEFAULT_BACKGROUND: int = 0x1c1c1c
  DEFAULT_FOREGROUND: int = 0xeeeeee

  DEFAULT_RGB_LIST: list[str] = "0x000000"\
     " 0xd75f5f"\
     " 0x5fd75f"\
     " 0xd7d75f"\
     " 0x5f5fd7"\
     " 0xd75fd7"\
     " 0x5fd7d7"\
     " 0xeeeeee"\
     " 0x000000"\
     " 0xd75f5f"\
     " 0x5fd75f"\
     " 0xd7d75f"\
     " 0x5f5fd7"\
     " 0xd75fd7"\
     " 0x5fd7d7"\
     " 0xeeeeee"\

#_______________________________________________________________________
class RgbColor:

#_______________________________________________________________________
  def get_rgb_from_hex(rgb_color: int) -> dict:
    """
    Creates map of red, green, and blue values from a single number.

    E.g.
    input:  0xFFFF00
    output: {'red': 255, 'grn': 255, blu: 0}
    """

    rgb_map: dict = {}

    red: int = (rgb_color & RgbConst.RED_MASK) >> RgbConst.RED_RIGHT_SHIFT
    grn: int = (rgb_color & RgbConst.GRN_MASK) >> RgbConst.GRN_RIGHT_SHIFT
    blu: int = (rgb_color & RgbConst.BLU_MASK) >> RgbConst.BLU_RIGHT_SHIFT

    rgb_map[RgbConst.RED_STR] = red
    rgb_map[RgbConst.GRN_STR] = grn
    rgb_map[RgbConst.BLU_STR] = blu

    return rgb_map
