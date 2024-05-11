import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os  # Import the 'os' module for file operations

def txt_to_csv(data_path, s_class, i):
    ''' 
    Arguments:
        data_path = path to txt file
        s_class = Sleep category, one of [n, brux, ins, narco, nfle, plm, rbd, sdb]
        i = denotes recording number
    '''
    try:
        # Create the directory for CSV files if it doesn't exist
        csv_directory = '/home/Duchuy220602/thesis/bosungfile'
        os.makedirs(csv_directory, exist_ok=True)

        with open(os.path.join(data_path, f"{s_class}{i}.txt"), "r") as fp:
            # Looping until buffer text ends
            str_point = ['Sleep Stage','Time [hh:mm:ss]', 'Event', 'Duration[s]', 'Location']
            for _ in range(30):
                x = fp.readline().strip().split("\t")
                if x == str_point:
                    break
            
            # Creating an empty DataFrame
            df_temp = pd.DataFrame(columns=str_point)

            idx = 0
            # Looping until the end of the file
            while True:
                temp_line = fp.readline().strip().split("\t")
                if len(temp_line) == len(str_point):
                    df_temp.loc[idx] = temp_line
                    idx += 1
                else:
                    # Save the DataFrame as a CSV file
                    df_temp.to_csv(os.path.join(csv_directory, f"{s_class}{i}.csv"), index=False)
                    break
    except Exception as e:
        print('Error:', e)
        print("Recheck file name!")
        
data_path = r"/mnt/data_lab513/data_thesis_duchuy/physionet.org/files/capslpdb/1.0.0/"
s_class = ['n', 'brux', 'ins', 'narco', 'nfle', 'plm', 'rbd', 'sdb']

# Iterate over sleep categories and recording numbers
for category in s_class:
    for i in range(40):  # Assuming you want to process 10 files for each category (adjust as needed)
        txt_to_csv(data_path, category, i)