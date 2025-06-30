<<<<<<< HEAD
import csv
import pandas as pd
import datetime
from datetime import datetime, timedelta

year_list = [2020, 2021, 2022, 2023, 2024, 2025]
source_list = ['wix_stock_historical_data', 'godaddy_stock_price_history', 'shopify_stock_price_history']
path_source = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
# main resource of info >> wix stock price > historical data /  https://www.investing.com/
miss_dates = {}

def prepare_file(source):
    df = pd.read_csv(path_source + source + '.csv')
    data_dict = df.to_dict(orient='records')
    fieldnames = df.columns.tolist()
    return data_dict, fieldnames

def data_check(data, source):
    count_dates = 0
    count_rows = 0
    previous_date = None
    miss_dates[source] = []
    for row in range(len(data)):
        date_str = data[row]['Date']
        # convert date string to date (date type)
        date_date_type = datetime.strptime(date_str, "%m/%d/%Y").date()
        count_rows += 1
        # we do not need to compare the first row as we do not have anything to compare with and the last with higher
        # for the same reason
        if len(data) - 1 > row > 0:
            # check if the data is correct and the previous data is bigger than the current one, so they are in order
            if date_date_type < previous_date:
                count_dates += 1
            else:
                print("Bigger than previous ", data[row]['Date'], data[row+1]['Date'])
            if abs(previous_date - date_date_type) > timedelta(days=1):
                # print("Miss info for more than 1 day ", previous_date, date_date_type)
                miss_dates[source].append((previous_date, date_date_type))
        previous_date = date_date_type
    return count_dates, count_rows

def create_file_data_year(year, file_name, data_dict):
    file_path = path_source + file_name + '_' + str(year) + '.csv'
    count = 0
    # divide the file according to a year from 2020 to 2025 (18th of May)
    with open(file_path, 'a') as f:
        write = csv.DictWriter(f, fieldnames=fieldnames)
        write.writeheader()
        for i in data_dict:
            # print(i)
            date_original = i['Date']
            if str(year) in date_original:
                # count days to check if I have full data about 365 days a year
                count += 1
                # update the file according to the year
                # with open(file_path, 'a') as f:
                #     write = csv.DictWriter(f, fieldnames=fieldnames)
                #     write.writeheader()
                write.writerow(i)
    print(count)

for file in source_list:
    data_dict, fieldnames = prepare_file(file)
    current_date, total_dates = data_check(data_dict, file)
    if total_dates - current_date == 2:
        print("Success")
    for year in year_list:
        create_file_data_year(year, file, data_dict)

## example for testing purpose with one file only
# data_dict, fieldnames = prepare_file(source_list[0])
# data_check(data_dict)
# print(miss_dates)

# just for organizing them in simple manner >> missed_dates.txt file created
# for key, date_pairs in miss_dates.items():
#     print(f"{key}:")
#     for start_date, end_date in date_pairs:
#         print(f"  ({start_date}, {end_date})")




=======
import csv
import pandas as pd
import datetime
from datetime import datetime, timedelta

year_list = [2020, 2021, 2022, 2023, 2024, 2025]
source_list = ['wix_stock_historical_data', 'godaddy_stock_price_history', 'shopify_stock_price_history']
path_source = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
# main resource of info >> wix stock price > historical data /  https://www.investing.com/
miss_dates = {}

def prepare_file(source):
    df = pd.read_csv(path_source + source + '.csv')
    data_dict = df.to_dict(orient='records')
    fieldnames = df.columns.tolist()
    return data_dict, fieldnames

def data_check(data, source):
    count_dates = 0
    count_rows = 0
    previous_date = None
    miss_dates[source] = []
    for row in range(len(data)):
        date_str = data[row]['Date']
        # convert date string to date (date type)
        date_date_type = datetime.strptime(date_str, "%m/%d/%Y").date()
        count_rows += 1
        # we do not need to compare the first row as we do not have anything to compare with and the last with higher
        # for the same reason
        if len(data) - 1 > row > 0:
            # check if the data is correct and the previous data is bigger than the current one, so they are in order
            if date_date_type < previous_date:
                count_dates += 1
            else:
                print("Bigger than previous ", data[row]['Date'], data[row+1]['Date'])
            if abs(previous_date - date_date_type) > timedelta(days=1):
                # print("Miss info for more than 1 day ", previous_date, date_date_type)
                miss_dates[source].append((previous_date, date_date_type))
        previous_date = date_date_type
    return count_dates, count_rows

def create_file_data_year(year, file_name, data_dict):
    file_path = path_source + file_name + '_' + str(year) + '.csv'
    count = 0
    # divide the file according to a year from 2020 to 2025 (18th of May)
    with open(file_path, 'a') as f:
        write = csv.DictWriter(f, fieldnames=fieldnames)
        write.writeheader()
        for i in data_dict:
            # print(i)
            date_original = i['Date']
            if str(year) in date_original:
                # count days to check if I have full data about 365 days a year
                count += 1
                # update the file according to the year
                # with open(file_path, 'a') as f:
                #     write = csv.DictWriter(f, fieldnames=fieldnames)
                #     write.writeheader()
                write.writerow(i)
    print(count)

for file in source_list:
    data_dict, fieldnames = prepare_file(file)
    current_date, total_dates = data_check(data_dict, file)
    if total_dates - current_date == 2:
        print("Success")
    for year in year_list:
        create_file_data_year(year, file, data_dict)

## example for testing purpose with one file only
# data_dict, fieldnames = prepare_file(source_list[0])
# data_check(data_dict)
# print(miss_dates)

# just for organizing them in simple manner >> missed_dates.txt file created
# for key, date_pairs in miss_dates.items():
#     print(f"{key}:")
#     for start_date, end_date in date_pairs:
#         print(f"  ({start_date}, {end_date})")




>>>>>>> master
