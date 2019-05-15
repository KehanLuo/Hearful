import csv

use = 0
use_pos = 0
use_neg = 0
fit = 0
fit_pos = 0
fit_neg = 0
value = 0
value_pos = 0
value_neg = 0
style = 0
style_pos = 0
style_neg = 0
quality = 0
quality_pos = 0
quality_neg = 0

output = open("apparel.csv", "w", encoding='utf-8')
columnTitleRow = "use_count, use_pos, use_neg, fit_count, fit_pos, fit_neg, value_count, value_pos, " \
                 "value_neg, style_count, style_pos, style_neg, quality_count, quality_pos, quality_neg\n"
output.write(columnTitleRow)

with open("APPAREL_ids_1_2019.csv", encoding='utf-8') as csv_file:
    readCSV = csv.reader(csv_file)
    for row in readCSV:
        if row[6] == '1.0':
            use += 1
            if row[5] == "pos":
                use_pos += 1
            elif row[5] == "neg":
                use_neg += 1
        if row[8] == '1.0':
            fit += 1
            if row[7] == "pos":
                fit_pos += 1
            elif row[7] == "neg":
                fit_neg += 1
        if row[10] == '1.0':
            value += 1
            if row[9] == "pos":
                value_pos += 1
            elif row[9] == "neg":
                value_neg += 1
        if row[12] == '1.0':
            style += 1
            if row[11] == "pos":
                style_pos += 1
            elif row[11] == "neg":
                style_neg += 1
        if row[14] == '1.0':
            quality += 1
            if row[13] == "pos":
                quality_pos += 1
            elif row[13] == "neg":
                quality_neg += 1
    row = str(use) + "," + str(use_pos) + "," + str(use_neg) + "," + str(fit) + "," + str(fit_pos) + "," + str(fit_neg)\
          + "," + str(value) + "," + str(value_pos) + "," + str(value_neg) + "," + str(style) + "," + str(style_pos) +\
          "," + str(style_neg) + "," + str(quality) + "," + str(quality_pos) + "," + str(quality_neg) + "\n"
    output.write(row)
    '''
    print("use count: ", use)
    print("use pos count: ", use_pos)
    print("use neg count: ", use_neg)
    print("fit count: ", fit)
    print("fit pos count: ", fit_pos)
    print("fit neg count: ", fit_neg)
    print("value count: ", value)
    print("value pos count: ", value_pos)
    print("value neg count: ", value_neg)
    print("style count: ", style)
    print("style pos count: ", style_pos)
    print("style neg count: ", style_neg)
    print("quality count: ", quality)
    print("quality pos count: ", quality_pos)
    print("quality neg count: ", quality_neg)
    '''