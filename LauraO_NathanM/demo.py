import os
import csv

script_folder = os.path.dirname(os.path.abspath(__file__))
csv_name = os.path.join(script_folder, 'test_w.csv')

header = ['column 1', 'column 2']

rows = [['r1,c1', 'r1,c2', 'r1,c3'],
        ['r2,c1', 'r2,c2', 'r2,c3'],
        ['r3,c1', 'r3,c2', 'r3,c3']]

print('Write header and rows to test_w.csv ...\n')
csv_name = os.path.join(script_folder, 'test_w.csv')
with open(csv_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)

rows = [{'Col 1': 'r1,c1', 'Col 1': 'r1,c2'},
        {'Col 2': 'r2,c2', 'Col 2': 'r2,c2'}]

print('Write header and rows to test_dw.csv ...\n')
csv_name = os.path.join(script_folder, 'test_dw.csv')
with open(csv_name, 'w', newline='') as f:
    writer = csv.DictWriter(f, ['Col 1', 'Col 2'])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(os.getcwd()) 
os.chdir('..')
print(os.getcwd())
os.chdir('..\\')
print(os.getcwd())
os.chdir('\\')
print(os.getcwd())