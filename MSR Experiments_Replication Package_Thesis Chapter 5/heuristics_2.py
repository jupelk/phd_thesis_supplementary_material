import pandas as pd
from enum import Enum

class ModificationType(Enum):
    MODIFY = 1
    ADD = 2
    DELETE = 3

def get_new_code_and_rework(df):
    # Group the DataFrame by the modified file name
    grouped = df.groupby('modified_java_file_name')

    new_code = []
    rework = []

    # Iterate over each group
    for name, group in grouped:
        # Determine if the change was a modification, addition or deletion
        if ModificationType.MODIFY in group['change_type'].unique():
            # If there was a modification, calculate the rework lines
            rework_lines = group[group['change_type'] == ModificationType.MODIFY]['deleted_lines'].sum()
        else:
            rework_lines = 0
        
        # Calculate the new lines
        new_lines = group[group['change_type'] == ModificationType.ADD]['added_lines'].sum()
        
        new_code.append(new_lines)
        rework.append(rework_lines)
    
    # Create a new DataFrame with the results
    result_df = pd.DataFrame({'modified_java_file_name': grouped.groups.keys(), 'new_code': new_code, 'rework': rework})
    
    return result_df
