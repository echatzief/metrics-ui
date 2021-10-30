import pandas as pd
from collections import Counter
import numpy as np

file_input = 'E:\\dataReconstruction\\Resultsprel.csv'
file_output = 'E:\\dataReconstruction\\Generated_dataset.xlsx'

df = pd.read_csv(file_input)


columns = df['ParameterName'].unique().tolist()

subjects = df['SubjectName'].unique().tolist()

column_names = ['SubjectName', 'TrialName'] + columns

df_new = pd.DataFrame(columns=column_names)

index = 0
for subject in subjects:
    trial_names = df.loc[df['SubjectName']==subject, 'TrialName'].unique().tolist()
    for trial in trial_names:
        temp_subject = {'SubjectName': subject, 'TrialName': trial}
        df_new = df_new.append(temp_subject, ignore_index=True)

        for param in columns:
            temp_param_value = df.loc[(df['SubjectName']==subject) & (df['TrialName']==trial) &
                                      (df['ParameterName']==param), 'Value'].to_list()

            if not temp_param_value:
                temp_param_value = np.nan
            else:
                temp_param_value = temp_param_value[0]

            df_new.loc[index, param] = temp_param_value

        index = index + 1


df_new.to_excel(file_output, index=False)
