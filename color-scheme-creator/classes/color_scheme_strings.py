#_______________________________________________________________________
# Collection of strings used in color_scheme_designer.
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
