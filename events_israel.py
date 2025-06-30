<<<<<<< HEAD
import pandas as pd
import csv

path_source = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
# df = pd.read_csv(path_source + '2022-06-14-2025-06-18.csv')
# data_dict = df.to_dict(orient='records')
# fieldnames = ['event_date','year', 'source', 'notes']
#
#
# def create_file_filtered_data(data):
#     with open(path_source + 'filtered_data_israel.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for row in data:
#             info = {'event_date': row['event_date'], 'year': str(row['year']), 'source': row['source'], 'notes': row['notes']}
#             writer.writerow(info)
#
# create_file_filtered_data(data_dict)

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# df = pd.read_csv(path_source + 'filtered_data_israel.csv')
df = pd.read_csv(r'C:\Users\khrystynad\Downloads\da_pet_project\israel_palestin_csv\filtered_data_israel.csv')
data_dict = df.to_dict(orient='records')
fieldnames = ['event_date', 'year', 'source', 'notes']

with open(path_source + r'\israel_palestin_csv\new_filtered_correct_date_format.csv', 'w', newline='',
          encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in data_dict:
        date = i['event_date'].split(' ')
        month = str((months.index(date[1])) + 1)
        if len(month) == 1:
            month = '0' + month
        # day = str(date[2])
        date = str(date[2]) + '-' + month + '-' + str(date[0])
        i['event_date'] = date
        print(i)
        writer.writerow(i)
=======
import pandas as pd
import csv

from analytics import event_file

path_source = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
# df = pd.read_csv(path_source + '2022-06-14-2025-06-18.csv')
# data_dict = df.to_dict(orient='records')
# fieldnames = ['event_date','year', 'source', 'notes']
#
#
# def create_file_filtered_data(data):
#     with open(path_source + 'filtered_data_israel.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for row in data:
#             info = {'event_date': row['event_date'], 'year': str(row['year']), 'source': row['source'], 'notes': row['notes']}
#             writer.writerow(info)
#
# create_file_filtered_data(data_dict)

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# df = pd.read_csv(path_source + 'filtered_data_israel.csv')
# df = pd.read_csv(r'C:\Users\khrystynad\Downloads\da_pet_project\israel_palestin_csv\filtered_data_israel.csv')
# data_dict = df.to_dict(orient='records')
# fieldnames = ['event_date', 'year', 'source', 'notes']

# with open(path_source + r'\israel_palestin_csv\new_filtered_correct_date_format.csv', 'w', newline='',
#           encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for i in data_dict:
#         date = i['event_date'].split(' ')
#         month = str((months.index(date[1])) + 1)
#         if len(month) == 1:
#             month = '0' + month
#         # day = str(date[2])
#         date = str(date[2]) + '-' + month + '-' + str(date[0])
#         i['event_date'] = date
#         print(i)
#         writer.writerow(i)



>>>>>>> master
