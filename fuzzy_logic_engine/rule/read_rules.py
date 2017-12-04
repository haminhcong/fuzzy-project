import xlrd


def read_light_rule():
    light_rule = []
    with xlrd.open_workbook('knowledge_base/fuzzy_rule.xlsx') as book:
        sheet = book.sheet_by_index(1)

        distance = [x for x in sheet.col_values(1)]
        light_status = [y for y in sheet.col_values(2)]
        angle = [z for z in sheet.col_values(3)]
        speed = [t for t in sheet.col_values(4)]

        for i in range(1, len(distance)):
            light_rule.append((distance[i].strip(), light_status[i].strip(), angle[i].strip(), speed[i].strip()))

    return light_rule


def read_barrier_rule():
    barrier_rule = []
    with xlrd.open_workbook('knowledge_base/fuzzy_rule.xlsx') as book:
        sheet = book.sheet_by_index(0)
        # k = sheet.row_values(0)
        distance = [x for x in sheet.col_values(1)]
        angle = [y for y in sheet.col_values(2)]
        speed = [z for z in sheet.col_values(3)]

        for i in range(1, len(distance)):
            barrier_rule.append((distance[i].strip(), angle[i].strip(), speed[i].strip()))

    return barrier_rule
