import pandas as pd
import os

new_data_df = pd.read_csv('data/sample_main_rows_with_aggregated_data_with_jira.csv')
new_main_rows = new_data_df[new_data_df['hash'].notna()]

for i, hash in enumerate(new_main_rows['hash']):
    input = '/home/ubuntu/designite_hadoop/hadoop/hadoop-common-project'
    output = '/home/ubuntu/designite/output' + str(i)
    cmd_cd = 'cd /home/ubuntu/designite_hadoop/hadoop;'
    cmd_checkout = 'git checkout ' + hash + ';'
    cmd_designite = f'java -Xmx2520M -jar /home/ubuntu/designite/DesigniteJava.jar -i {input} -o {output}'
    os.system(cmd_cd + cmd_checkout + cmd_designite)       
    print('Done', i, 'Hash: ', hash)




