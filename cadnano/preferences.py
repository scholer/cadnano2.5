
from cadnano.color import Color

# Slice Sizing
SLICE_HELIX_RADIUS = 15
SLICE_HELIX_STROKE_WIDTH = 0.5
SLICE_HELIX_HILIGHT_WIDTH = 2.5
SLICE_HELIX_MOD_HILIGHT_WIDTH = 1
HONEYCOMB_PART_MAXROWS = 30
HONEYCOMB_PART_MAXCOLS = 32
HONEYCOMB_PART_MAXSTEPS = 2
SQUARE_PART_MAXROWS = 50
SQUARE_PART_MAXCOLS = 50
SQUARE_PART_MAXSTEPS = 2

# Slice Colors
BLUE_FILL = Color(153, 204, 255)  # 99ccff
BLUE_STROKE = Color(0, 102, 204)  # 0066cc
BLUISH_STROKE = Color(0, 182, 250)  # 
ORANGE_FILL = Color(255, 204, 153)  # ffcc99
ORANGE_STROKE = Color(204, 102, 51)  # cc6633
LIGHT_ORANGE_FILL = Color(255, 234, 183)
LIGHT_ORANGE_STROKE = Color(234, 132, 81)
GRAY_FILL = Color(238, 238, 238)  # eeeeee (was a1a1a1)
GRAY_STROKE = Color(102, 102, 102)  # 666666 (was 424242)

# Path Sizing
VIRTUALHELIXHANDLEITEM_RADIUS = 30
VIRTUALHELIXHANDLEITEM_STROKE_WIDTH = 2
PATH_BASE_WIDTH = 20  # used to size bases (grid squares, handles, etc)
PATH_HELIX_HEIGHT = 2 * PATH_BASE_WIDTH  # staple + scaffold
PATH_HELIX_PADDING = 50 # gap between PathHelix objects in path view
PATH_GRID_STROKE_WIDTH = 0.5
SLICE_HANDLE_STROKE_WIDTH = 1
PATH_STRAND_STROKE_WIDTH = 3
PATH_STRAND_HIGHLIGHT_STROKE_WIDTH = 8
PATH_SELECTBOX_STROKE_WIDTH = 1.5
PCH_BORDER_PADDING = 1
PATH_BASE_HL_STROKE_WIDTH = 2  # PathTool highlight box
MINOR_GRID_STROKE_WIDTH = 0.5
MAJOR_GRID_STROKE_WIDTH = 0.5
OLIGO_LEN_BELOW_WHICH_HIGHLIGHT = 20
OLIGO_LEN_ABOVE_WHICH_HIGHLIGHT = 49

# Path Drawing
PATH_XOVER_LINE_SCALE_X = 0.035
PATH_XOVER_LINE_SCALE_Y = 0.035

# Path Colors
SCAFFOLD_BKG_FILL = Color(230, 230, 230)
ACTIVE_SLICE_HANDLE_FILL = Color(255, 204, 153, 128)  # ffcc99
ACTIVE_SLICE_HANDLE_STROKE = Color(204, 102, 51, 128)  # cc6633
MINOR_GRID_STROKE = Color(204, 204, 204)  # 999999
MAJOR_GRID_STROKE = Color(153, 153, 153)  # 333333
SCAF_STROKE = Color(0, 102, 204)  # 0066cc
HANDLE_FILL = Color(0, 102, 204)  # 0066cc
PXI_SCAF_STROKE = Color(0, 102, 204, 153)
PXI_STAP_STROKE = Color(204, 0, 0, 153)
PXI_DISAB_STROKE = Color(204, 204, 204, 255)
RED_STROKE = Color(204, 0, 0)
ERASE_FILL = Color(204, 0, 0, 63)
FORCE_FILL = Color(0, 255, 255, 63)
BREAK_FILL = Color(204, 0, 0, 255)
COLORBOX_FILL = Color(204, 0, 0)
COLORBOX_STROKE = Color(102, 102, 102)
STAP_COLORS = [Color(204, 0, 0),
              Color(247, 67, 8),
              Color(247, 147, 30),
              Color(170, 170, 0),
              Color(87, 187, 0),
              Color(0, 114, 0),
              Color(3, 182, 162),
              Color(23, 0, 222),
              Color(115, 0, 222),
              Color(184, 5, 108),
              Color(51, 51, 51),
              Color(136, 136, 136)]
SCAF_COLORS = [Color(0, 102, 204)]
              # Color(64, 138, 212),
              # Color(0, 38, 76),
              # Color(23, 50, 76),
              # Color(0, 76, 153)]
DEFAULT_STAP_COLOR = "#888888"
DEFAULT_SCAF_COLOR = "#0066cc"
SELECTED_COLOR = Color(255, 51, 51)

# brightColors = [Color() for i in range(10)]
# for i in range(len(brightColors)):
#     brightColors[i].setHsvF(i/12.0, 1.0, 1.0)
# bright_palette = Palette(brightColors)
# cadnn1_palette = Palette(cadnn1Colors)
# default_palette = cadnn1_palette

# Loop/Insertion path details
INSERTWIDTH = 2
SKIPWIDTH = 2

# Add Sequence Tool
INVALID_DNA_COLOR = Color(204, 0, 0)
UNDERLINE_INVALID_DNA = True

# Additional Prefs
PREF_AUTOSCAF_INDEX = 0
PREF_STARTUP_TOOL_INDEX = 0
PREF_ZOOM_SPEED = 20#50
PREF_ZOOM_AFTER_HELIX_ADD = True


#Z values
#bottom
ZACTIVESLICEHANDLE = 10
ZPATHHELIXGROUP = 20
ZPATHHELIX = 30
ZPATHSELECTION = 40
ZSLICEHELIX = 50
ZDESELECTOR = 60
ZFOCUSRING = 70
ZPREXOVERHANDLE = 80
ZXOVERITEM = 90
ZBREAKPOINTHANDLE = 100
ZSKIPHANDLE = 110
ZBREAKITEM = 120
ZPATHTOOL = 130
ZSTRANDITEM = 140
ZENDPOINTITEM = 150
ZINSERTHANDLE = 160
ZPARTITEM = 200
#top

XOVER_LABEL_COLOR = Color(0,0,0) 

# Overwrite for Maya
# MAJOR_GRID_STROKE = Color(255, 255, 255)  # ffffff for maya
