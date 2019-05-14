import re, csv

# construct three types of regex
# 1. start with "lauren"
# 2. start with "polo"
# 3. start with "ralph"
regexList = ["lauren.*ralph", "polo.*(ralph.*lauren|lauren.*ralph)", "ralph.*lauren"]
formatted_brand = "Ralph Lauren"

csv = open("brand cleaning regex.csv", "w", encoding='utf-8')
columnTitleRow = "Brand, Brand_formatted\n"
csv.write(columnTitleRow)


fp = list(open("Distinct_Brands.txt", encoding='utf-8'))
for line in fp:
    line = line.strip()
    line = line.replace(",", "")
    line = line.lstrip('\"')
    line = line.rstrip('\"')
    for regex in regexList:
        match = re.search(regex, line, re.IGNORECASE)
        if match:
            row = line + "," + formatted_brand + "\n"
            csv.write(row)

