#_______________________________________________________________________
# This file contains general utilities. The classes and functions in
# this file should be independent of the programs that consume it.
#_______________________________________________________________________

import json


#_______________________________________________________________________
class GeneralUtils:

  MAX_COLOR: int = 0xFFFFFF

  #_____________________________________________________________________
  def hex_int(s: str) -> int:
    """
    Parameter
    s - hex integer represented as a string

    Returns
    The int represented by the input string as hex.
    """

    return int(s, base=16)

  #_____________________________________________________________________
  def str_list_to_hex_list(l: list[str]) -> list[int]:
    """
    Converts a list of strings representing hexadecimal numbers to a
    list of ints.

    Parameters
    l - list of strings representing hex numbers
      E.g. ["0xFF","0x5F","0x87"]

    Returns
    List of ints corresponding with the hex representation of the
    argument.
      E.g. [255, 95, 135]
    """

    list_length: int = len(l)
    int_list: list[int] = [0] * list_length

    for i in range(list_length):
      int_list[i] = GeneralUtils.hex_int(l[i])

    return int_list

  #_____________________________________________________________________
  def read_hex_color_json(file_path: str) -> dict:
    """
    Reads json file in the format
    ________________________________
    { "background": "0x282828"
      , "foreground": "0xDF5f87"
      , "color-list":["0x5f0000"
      ...
        , "0xFFFFFF"
      ]
    }
    ________________________________

    Paramters
    file_path - path to json file

    Returns
    Dictionary with key value pairs from json file
    """

    # Open and read the JSON file
    with open(file_path, 'r') as file:
      return json.load(file)
