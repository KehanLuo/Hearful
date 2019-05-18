import csv


def acc(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + fp + fn)


def precision(tp, fp):
    return tp / (tp + fp)


def recall(tp, fn):
    return tp / (tp + fn)


def fmeasure(pre, rec):
    return 2 * pre * rec / (pre + rec)

# declaring variables
# theme existence
use_e_tp, use_e_tn, use_e_fp, use_e_fn = 0, 0, 0, 0
fit_e_tp, fit_e_tn, fit_e_fp, fit_e_fn = 0, 0, 0, 0
value_e_tp, value_e_tn, value_e_fp, value_e_fn = 0, 0, 0, 0
style_e_tp, style_e_tn, style_e_fp, style_e_fn = 0, 0, 0, 0
quality_e_tp, quality_e_tn, quality_e_fp, quality_e_fn = 0, 0, 0, 0

# theme sentiment
use_s_tp, use_s_tn, use_s_fp, use_s_fn = 0, 0, 0, 0
fit_s_tp, fit_s_tn, fit_s_fp, fit_s_fn = 0, 0, 0, 0
value_s_tp, value_s_tn, value_s_fp, value_s_fn = 0, 0, 0, 0
style_s_tp, style_s_tn, style_s_fp, style_s_fn = 0, 0, 0, 0
quality_s_tp, quality_s_tn, quality_s_fp, quality_s_fn = 0, 0, 0, 0

# a dictionary to store data from hand validated dataset
hand = {}

# read and store hand validated data
with open("APPAREL_ODOM_1_2019.csv", encoding='utf-8') as csv_file:
    readCSV = csv.reader(csv_file)
    next(readCSV)
    for row in readCSV:
        id = row[0]
        if row[7] == '1':
            hand.setdefault(id, {}).setdefault('use', []).append(row[6])
        if row[9] == '1':
            hand.setdefault(id, {}).setdefault('fit', []).append(row[8])
        if row[11] == '1':
            hand.setdefault(id, {}).setdefault('value', []).append(row[10])
        if row[13] == '1':
            hand.setdefault(id, {}).setdefault('style', []).append(row[12])
        if row[15] == '1':
            hand.setdefault(id, {}).setdefault('quality', []).append(row[14])
        # if none of the themes exists, store the id with empty data fields
        if row[7] == '0' and row[9] == '0' and row[11] == '0' and row[13] == '0' and row[15] == '0':
            hand.setdefault(id, {}).setdefault('', []).append('')
            # print(hand)
# print(len(hand))

# processing the data from model
with open("APPAREL_ids_1_2019.csv", encoding='utf-8') as csv_file1:
    readCSV = csv.reader(csv_file1)
    next(readCSV)
    for row in readCSV:
        id = row[0]
        if id in hand:
            # use
            if row[6] == '1.0':
                if 'use' in hand[id]:
                    use_e_tp += 1
                    if row[5] == 'pos' and hand[id]['use'][0] == 'pos':
                        use_s_tp += 1
                    elif row[5] == 'pos' and hand[id]['use'][0] == 'neg':
                        use_s_fp += 1
                    elif row[5] == 'neg' and hand[id]['use'][0] == 'pos':
                        use_s_fn += 1
                    elif row[5] == 'neg' and hand[id]['use'][0] == 'neg':
                        use_s_tn += 1
                else:
                    use_e_fp += 1
                    if row[5] == 'pos':
                        use_s_fp += 1
                    elif row[5] == 'neg':
                        use_s_fn += 1
            else:
                if 'use' in hand[id]:
                    use_e_fn += 1
                else:
                    use_e_tn += 1

            # fit
            if row[8] == '1.0':
                if 'fit' in hand[id]:
                    fit_e_tp += 1
                    if row[7] == 'pos' and hand[id]['fit'][0] == 'pos':
                        fit_s_tp += 1
                    elif row[7] == 'pos' and hand[id]['fit'][0] == 'neg':
                        fit_s_fp += 1
                    elif row[7] == 'neg' and hand[id]['fit'][0] == 'pos':
                        fit_s_fn += 1
                    elif row[7] == 'neg' and hand[id]['fit'][0] == 'neg':
                        fit_s_tn += 1
                else:
                    fit_e_fp += 1
                    if row[7] == 'pos':
                        fit_s_fp += 1
                    elif row[7] == 'neg':
                        fit_s_fn += 1
            else:
                if 'fit' in hand[id]:
                    fit_e_fn += 1
                else:
                    fit_e_tn += 1

            # value
            if row[10] == '1.0':
                if 'value' in hand[id]:
                    value_e_tp += 1
                    if row[9] == 'pos' and hand[id]['value'][0] == 'pos':
                        value_s_tp += 1
                    elif row[9] == 'pos' and hand[id]['value'][0] == 'neg':
                        value_s_fp += 1
                    elif row[9] == 'neg' and hand[id]['value'][0] == 'pos':
                        value_s_fn += 1
                    elif row[9] == 'neg' and hand[id]['value'][0] == 'neg':
                        value_s_tn += 1
                else:
                    value_e_fp += 1
                    if row[9] == 'pos':
                        value_s_fp += 1
                    elif row[9] == 'neg':
                        value_s_fn += 1
            else:
                if 'value' in hand[id]:
                    value_e_fn += 1
                else:
                    value_e_tn += 1

            # style
            if row[12] == '1.0':
                if 'style' in hand[id]:
                    style_e_tp += 1
                    if row[11] == 'pos' and hand[id]['style'][0] == 'pos':
                        style_s_tp += 1
                    elif row[11] == 'pos' and hand[id]['style'][0] == 'neg':
                        style_s_fp += 1
                    elif row[11] == 'neg' and hand[id]['style'][0] == 'pos':
                        style_s_fn += 1
                    elif row[11] == 'neg' and hand[id]['style'][0] == 'neg':
                        style_s_tn += 1
                else:
                    style_e_fp += 1
                    if row[11] == 'pos':
                        style_s_fp += 1
                    elif row[11] == 'neg':
                        style_s_fn += 1
            else:
                if 'style' in hand[id]:
                    style_e_fn += 1
                else:
                    style_e_tn += 1

            # quality
            if row[14] == '1.0':
                if 'quality' in hand[id]:
                    quality_e_tp += 1
                    if row[13] == 'pos' and hand[id]['quality'][0] == 'pos':
                        quality_s_tp += 1
                    elif row[13] == 'pos' and hand[id]['quality'][0] == 'neg':
                        quality_s_fp += 1
                    elif row[13] == 'neg' and hand[id]['quality'][0] == 'pos':
                        quality_s_fn += 1
                    elif row[13] == 'neg' and hand[id]['quality'][0] == 'neg':
                        quality_s_tn += 1
                else:
                    quality_e_fp += 1
                    if row[13] == 'pos':
                        quality_s_fp += 1
                    elif row[13] == 'neg':
                        quality_s_fn += 1
            else:
                if 'quality' in hand[id]:
                    quality_e_fn += 1
                else:
                    quality_e_tn += 1

'''
print(use_e_tp, use_e_tn, use_e_fp, use_e_fn)
print(use_s_tp, use_s_tn, use_s_fp, use_s_fn)
print(fit_e_tp, fit_e_tn, fit_e_fp, fit_e_fn)
print(fit_s_tp, fit_s_tn, fit_s_fp, fit_s_fn)
print(value_e_tp, value_e_tn, value_e_fp, value_e_fn)
print(value_s_tp, value_s_tn, value_s_fp, value_s_fn)
print(style_e_tp, style_e_tn, style_e_fp, style_e_fn)
print(style_s_tp, style_s_tn, style_s_fp, style_s_fn)
print(quality_e_tp, quality_e_tn, quality_e_fp, quality_e_fn)
print(quality_s_tp, quality_s_tn, quality_s_fp, quality_s_fn)
'''

# calculating accuracy
use_e_acc = acc(use_e_tp, use_e_tn, use_e_fp, use_e_fn)
use_s_acc = acc(use_s_tp, use_s_tn, use_s_fp, use_s_fn)
fit_e_acc = acc(fit_e_tp, fit_e_tn, fit_e_fp, fit_e_fn)
fit_s_acc = acc(fit_s_tp, fit_s_tn, fit_s_fp, fit_s_fn)
value_e_acc = acc(value_e_tp, value_e_tn, value_e_fp, value_e_fn)
value_s_acc = acc(value_s_tp, value_s_tn, value_s_fp, value_s_fn)
style_e_acc = acc(style_e_tp, style_e_tn, style_e_fp, style_e_fn)
style_s_acc = acc(style_s_tp, style_s_tn, style_s_fp, style_s_fn)
quality_e_acc = acc(quality_e_tp, quality_e_tn, quality_e_fp, quality_e_fn)
quality_s_acc = acc(quality_s_tp, quality_s_tn, quality_s_fp, quality_s_fn)

# calculating precision
use_e_pre = precision(use_e_tp, use_e_fp)
use_s_pre = precision(use_s_tp, use_s_fp)
fit_e_pre = precision(fit_e_tp, fit_e_fp)
fit_s_pre = precision(fit_s_tp, fit_s_fp)
value_e_pre = precision(value_e_tp, value_e_fp)
value_s_pre = precision(value_s_tp, value_s_fp)
style_e_pre = precision(style_e_tp, style_e_fp)
style_s_pre = precision(style_s_tp, style_s_fp)
quality_e_pre = precision(quality_e_tp, quality_e_fp)
quality_s_pre = precision(quality_s_tp, quality_s_fp)

# calculating recall
use_e_rec = recall(use_e_tp, use_e_fn)
use_s_rec = recall(use_s_tp, use_s_fn)
fit_e_rec = recall(fit_e_tp, fit_e_fn)
fit_s_rec = recall(fit_s_tp, fit_s_fn)
value_e_rec = recall(value_e_tp, value_e_fn)
value_s_rec = recall(value_s_tp, value_s_fn)
style_e_rec = recall(style_e_tp, style_e_fn)
style_s_rec = recall(style_s_tp, style_s_fn)
quality_e_rec = recall(quality_e_tp, quality_e_fn)
quality_s_rec = recall(quality_s_tp, quality_s_fn)

# calculating fmeasures
use_e_f = fmeasure(use_e_pre, use_e_rec)
use_s_f = fmeasure(use_s_pre, use_s_rec)
fit_e_f = fmeasure(fit_e_pre, fit_e_rec)
fit_s_f = fmeasure(fit_s_pre, fit_s_rec)
value_e_f = fmeasure(value_e_pre, value_e_rec)
value_s_f = fmeasure(value_s_pre, value_s_rec)
style_e_f = fmeasure(style_e_pre, style_e_rec)
style_s_f = fmeasure(style_s_pre, style_s_rec)
quality_e_f = fmeasure(quality_e_pre, quality_e_rec)
quality_s_f = fmeasure(quality_s_pre, quality_s_rec)

# output file
output = open("apparel_stat.csv", "w", encoding='utf-8')
columnTitleRow = "stat, theme_exist, theme_sentiment\n"
output.write(columnTitleRow)
output_rows = []
output_rows.append("accuracies.use" + "," + str(use_e_acc) + "," + str(use_s_acc) + "\n")
output_rows.append("accuracies.fit" + "," + str(fit_e_acc) + "," + str(fit_s_acc) + "\n")
output_rows.append("accuracies.value" + "," + str(value_e_acc) + "," + str(value_s_acc) + "\n")
output_rows.append("accuracies.style" + "," + str(style_e_acc) + "," + str(style_s_acc) + "\n")
output_rows.append("accuracies.quality" + "," + str(quality_e_acc) + "," + str(quality_s_acc) + "\n")
output_rows.append("fmeasures.use" + "," + str(use_e_f) + "," + str(use_s_f) + "\n")
output_rows.append("fmeasures.fit" + "," + str(fit_e_f) + "," + str(fit_s_f) + "\n")
output_rows.append("fmeasures.value" + "," + str(value_e_f) + "," + str(value_s_f) + "\n")
output_rows.append("fmeasures.style" + "," + str(style_e_f) + "," + str(style_s_f) + "\n")
output_rows.append("fmeasuress.quality" + "," + str(quality_e_f) + "," + str(quality_s_f) + "\n")
output_rows.append("precisons.use" + "," + str(use_e_pre) + "," + str(use_s_pre) + "\n")
output_rows.append("precisons.fit" + "," + str(fit_e_pre) + "," + str(fit_s_pre) + "\n")
output_rows.append("precisons.value" + "," + str(value_e_pre) + "," + str(value_s_pre) + "\n")
output_rows.append("precisons.style" + "," + str(style_e_pre) + "," + str(style_s_pre) + "\n")
output_rows.append("precisons.quality" + "," + str(quality_e_pre) + "," + str(quality_s_pre) + "\n")
output_rows.append("recalls.use" + "," + str(use_e_rec) + "," + str(use_s_rec) + "\n")
output_rows.append("recalls.fit" + "," + str(fit_e_rec) + "," + str(fit_s_rec) + "\n")
output_rows.append("recalls.value" + "," + str(value_e_rec) + "," + str(value_s_rec) + "\n")
output_rows.append("recalls.style" + "," + str(style_e_rec) + "," + str(style_s_rec) + "\n")
output_rows.append("recalls.quality" + "," + str(quality_e_rec) + "," + str(quality_s_rec) + "\n")
for output_row in output_rows:
    output.write(output_row)