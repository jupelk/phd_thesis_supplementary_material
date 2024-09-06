import pandas as pd
from enum import Enum

class ModificationType(Enum):
    MODIFY = 1
    ADD = 2
    DELETE = 3

dataset_s500 = pd.read_csv('c:\\CodeBook\\new_code_rework_TD\\commits_with_jira_sample_concsecutive_500_aggregated.csv')
dataset_s500['new_code'] = ''
dataset_s500['rework'] = ''

def calculate_new_code_and_rework(row):
    new_code = 0
    rework = 0
    
    for col in row.iterrows():
        change_type = col['change_type']
        added_lines = col['added_lines']
        deleted_lines = col['deleted_lines']        
        
        if change_type == ModificationType.ADD: # everything is new code because deleted lines are zero
            new_code += added_lines
        elif change_type == ModificationType.DELETE: # everything is rework because added lines are zero
            rework += deleted_lines
        elif change_type == ModificationType.MODIFY: # there can be both new code and rework 
            # check if added lines are zero
            if added_lines == 0:
                rework += deleted_lines
                continue
            #check if deleted lines are zero
            if deleted_lines == 0:
                new_code += added_lines
                continue
            elif added_lines == deleted_lines:
                pass # pass because added lines cancells deleted lines
            elif added_lines > deleted_lines:
                new_code += added_lines - deleted_lines
            elif added_lines < deleted_lines:
                rework += deleted_lines - added_lines
                
    return new_code, rework

for row in dataset_s500.iterrows():
    #if dataset_s500['change_type'] is not empty
    if row['change_type'] is not None:
        new_code, rework = calculate_new_code_and_rework(row)
        dataset_s500.at[row.Index, 'new_code'] = new_code
        dataset_s500.at[row.Index, 'rework'] = rework
    if row.Index == 5:
        break