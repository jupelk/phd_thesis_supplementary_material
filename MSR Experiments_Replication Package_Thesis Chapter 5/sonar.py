import pandas as pd
import os

# new_data_df = pd.read_csv('data/sample_main_rows_with_aggregated_data_with_jira.csv')
# new_main_rows = new_data_df[new_data_df['hash'].notna()]

df_359 = pd.read_csv('data/sample_main_rows_with_aggregated_data_with_jira.csv')
df_all = pd.read_csv('data/commits_with_jira.csv')
new_main_rows = df_all.loc[df_all['hash'].notna() & df_all['jira issue key'].notna()][-1000:].loc[~df_all['hash'].isin(df_359['hash'])]


for i, hash in enumerate(new_main_rows['hash']):
    #if i % 500 != 0:
     #   continue    # sonar-scanner -D sonar.login=sqp_0afb5debfd6c509861f92b58fea301eba2f8505f -D sonar.java.binaries=hadoop-annotations%cd hadoop-common-project
    # os.system('cd /home/ubuntu/sq_hadoop/hadoop; git checkout ' + hash + '; cd hadoop-common-project; ~/sonar-scanner-4.8.0.2856/bin/sonar-scanner -D sonar.projectKey=hadoop_common -D sonar.sources=. -D sonar.java.binaries=.  -D sonar.host.url=http://localhost:9000 -D sonar.login=sqp_7032d5b619a58c8216d7f83a01f669011baa5b71 -D sonar.projectVersion=' + hash)
    os.system('cd /home/ubuntu/sq_hadoop/hadoop; git checkout ' + hash + '; cd hadoop-common-project; ~/sonar-scanner-4.8.0.2856/bin/sonar-scanner -D sonar.projectKey=hadoop_common_641 -D sonar.sources=. -D sonar.java.binaries=.  -D sonar.host.url=http://localhost:9000 -D sonar.login=sqp_f3e752081c24bfa82042a1f028d04033eaf73a62 -D sonar.projectVersion=' + hash)


    print('Done', i, 'Hash: ', hash)
