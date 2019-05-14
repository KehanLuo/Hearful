import csv

# get possible brand name combinations from a text file
brands = []
def getBrands(file):
    f = open(file)
    for line in f:
        line = line.strip()
        brands.append(line)


getBrands("ralph lauren.txt")
formatted_brand = "Ralph Lauren"

csv = open("brand cleaning brandlist.csv", "w", encoding='utf-8')
columnTitleRow = "Brand, Brand_formatted\n"
csv.write(columnTitleRow)


fp = list(open("Distinct_Brands.txt", encoding='utf-8'))
for line in fp:
    line = line.strip()
    line = line.replace(",", "")
    line = line.lstrip('\"')
    line = line.rstrip('\"')
    for brand in brands:
        if brand in line:
            row = line + "," + formatted_brand + "\n"
            csv.write(row)

