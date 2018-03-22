
import csv



wiki = open("wiki_extract08.txt",'r', encoding = 'utf8')


with open("wiki_extract08.csv", 'w', encoding = 'utf8', newline='') as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(('Name','Summary','Content'))
    for row in wiki:
        columns = [c.strip() for c in row.strip(', ').split(',')]
        writer.writerow(columns)