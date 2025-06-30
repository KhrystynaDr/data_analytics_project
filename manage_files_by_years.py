<<<<<<< HEAD
import pandas as pd
import os
from datetime import datetime, timedelta

folder_path = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
year_list = [2020, 2021, 2022, 2023, 2024, 2025]
files = set()
# List matching filenames
for filename in os.listdir(folder_path):
    if 'stock' in filename:
        files.add(filename.split('_')[0])
print(files)

# for name in files:
#     for filename in os.listdir(folder_path):
#         if name in filename:
#             df = pd.read_csv(folder_path + filename)
#             data_dict = df.to_dict(orient='records')

def match_data(source_list):
    for parameter in source_list:
        for filename in os.listdir(folder_path):
            if str(parameter) in filename:
                df = pd.read_csv(folder_path + filename)
                data_dict = df.to_dict(orient='records')
                for row in range(len(data_dict)):
                    print(type(data_dict[row]['Date']))
                    date_str = data_dict[row]['Date']
                    # convert date string to date (date type)
                    date_date_type = datetime.strptime(date_str, "%m/%d/%Y").date()
                    print(date_date_type)
                    data_dict[row]['Date'] = date_date_type
                    print(type(data_dict[row]['Date'] ))
                    print(data_dict[row])

# match_data(year_list)
match_data(files)


=======
import pandas as pd
import os
from datetime import datetime, timedelta

folder_path = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
year_list = [2020, 2021, 2022, 2023, 2024, 2025]
files = set()
# List matching filenames
for filename in os.listdir(folder_path):
    if 'stock' in filename:
        files.add(filename.split('_')[0])
print(files)

# for name in files:
#     for filename in os.listdir(folder_path):
#         if name in filename:
#             df = pd.read_csv(folder_path + filename)
#             data_dict = df.to_dict(orient='records')

def match_data(source_list):
    for parameter in source_list:
        for filename in os.listdir(folder_path):
            if str(parameter) in filename:
                df = pd.read_csv(folder_path + filename)
                data_dict = df.to_dict(orient='records')
                for row in range(len(data_dict)):
                    print(type(data_dict[row]['Date']))
                    date_str = data_dict[row]['Date']
                    # convert date string to date (date type)
                    date_date_type = datetime.strptime(date_str, "%m/%d/%Y").date()
                    print(date_date_type)
                    data_dict[row]['Date'] = date_date_type
                    print(type(data_dict[row]['Date'] ))
                    print(data_dict[row])

match_data(year_list)
# match_data(files)


>>>>>>> master
