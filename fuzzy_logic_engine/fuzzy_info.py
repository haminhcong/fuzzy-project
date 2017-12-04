import xlrd

light_rule = []

# LAMP STATE FUZZY INFO

RED_FUZZY_INFO = []
LESS_RED_FUZZY_INFO = []
YELLOW_FUZZY_INFO = []
LESS_GREEN_FUZZY_INFO = []
GREEN_FUZZY_INFO = []

DISTANCE_NEAR_FUZZY_INFO = []
DISTANCE_MEDIUM_FUZZY_INFO = []
DISTANCE_FAR_FUZZY_INFO = []

ANGLE_SMALL_FUZZY_INFO = []
ANGLE_MEDIUM_FUZZY_INFO = []
ANGLE_BIG_FUZZY_INFO = []

SPEED_DOMAIN_FUZZY_INFO=[]
SPEED_FAST_FUZZY_INFO = []
SPEED_SLOW_FUZZY_INFO = []
SPEED_SLOWER_FUZZY_INFO = []
SPEED_STOP_FUZZY_INFO = []

with xlrd.open_workbook('knowledge_base/fuzzy_info.xlsx') as book:
    # import lamp state fuzzy info data
    sheet = book.sheet_by_index(0)
    RED_FUZZY_INFO = sheet.row_values(0)
    LESS_RED_FUZZY_INFO = sheet.row_values(1)
    YELLOW_FUZZY_INFO = sheet.row_values(2)
    LESS_GREEN_FUZZY_INFO = sheet.row_values(3)
    GREEN_FUZZY_INFO = sheet.row_values(4)
    sheet = book.sheet_by_index(1)
    DISTANCE_NEAR_FUZZY_INFO = sheet.row_values(0)
    DISTANCE_MEDIUM_FUZZY_INFO = sheet.row_values(1)
    DISTANCE_FAR_FUZZY_INFO = sheet.row_values(2)
    sheet = book.sheet_by_index(2)
    ANGLE_SMALL_FUZZY_INFO = sheet.row_values(0)
    ANGLE_MEDIUM_FUZZY_INFO = sheet.row_values(1)
    ANGLE_BIG_FUZZY_INFO = sheet.row_values(2)
    sheet = book.sheet_by_index(3)
    SPEED_DOMAIN_FUZZY_INFO=sheet.row_values(0)
    SPEED_FAST_FUZZY_INFO = sheet.row_values(1)
    SPEED_SLOW_FUZZY_INFO = sheet.row_values(2)
    SPEED_SLOWER_FUZZY_INFO = sheet.row_values(3)
    SPEED_STOP_FUZZY_INFO = sheet.row_values(4)