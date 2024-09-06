#generate csv file with smell results from designite

import pandas as pd
import csv

main_data_df = pd.read_csv('c:\\CodeBook\\new_code_rework_TD\\sample_main_rows_with_aggregated_data_and_sq_code_smells.csv')
main_data_df['design_smells'] = ''
main_data_df['design_smell_diff'] = ''

#method to get design smells
def get_design_smells(csv_path):
    print(csv_path)
    with open(csv_path, 'r') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        header = next(reader)  # skip header row
        #design_smells = []
        count = 0
        for row in reader:
            if len(row) < 2:
                continue  # skip rows with fewer than two elements
            count += 1
            elements = row[1].split(',')
            if len(elements) < 4:
                continue  # skip rows with fewer than four comma-separated elements
            print(elements[3])
        print(csv_path + f"Number of rows: {count}")
    return count


indices = main_data_df.index.to_list()
csv_paths = []

for i in range(len(indices)):      
    if i % 10 == 0:
        print(i)
        csv_path = 'C:\Tools\Designite\Output' + str(i)  
        csv_paths.append(csv_path)
    if i == 10:
        break


for path in csv_paths:
    print(path)
    get_design_smells(path)