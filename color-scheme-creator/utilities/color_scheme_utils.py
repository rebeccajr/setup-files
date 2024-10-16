#_______________________________________________________________________
# This file contains general utilities. The classes and functions in
# this file should be independent of the programs that consume it.
#_______________________________________________________________________

class GeneralUtils:

  MAX_COLOR: int = 0xFFFFFF

  #_____________________________________________________________________
  def hex_int(s: str):
    """
    Parameter
    s - hex integer represented as a string

    Returns
    The int represented by the input string as hex.
    """

    return int(s, base=16)