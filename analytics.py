import csv
import os
import pandas as pd
import datetime
from datetime import datetime, timedelta

path_source = r'C:\Users\khrystynad\Downloads\da_pet_project\\'
another_folder = 'israel_palestin_csv'
year_list = [2020, 2021, 2022, 2023, 2024, 2025]


# list of all files in the folder:
def find_all_files(year):
    files = []
    event_files = os.listdir(path_source + another_folder)

    # get all files based on year for Wix, Shopify, GoDaddy
    for file in os.listdir(path_source):
        if str(year) in file:
            files.append(file)

    # get file with events Israel-Palestine of that year
    for event_file in event_files:
        if str(year) in event_file:
            file_event_name = another_folder +r"\\" + event_file
    return files, file_event_name

def convert_to_date_type(source):
    source['Date'] = pd.to_datetime(source['Date'], format="%m/%d/%Y", errors='coerce')
    return source


def convert_to_date_type_events(source):
    source['Date'] = pd.to_datetime(source['Date'])
    return source

# Load the files
def open_files(files, event):
    wix, godaddy, shopify = None, None, None
    columns_to_keep = ['Date', 'Change %']
    for file in files:
        if 'wix' in file:
            wix = pd.read_csv(path_source + file, usecols=columns_to_keep)
        elif 'godaddy' in file:
            godaddy = pd.read_csv(path_source + file, usecols=columns_to_keep)
        elif 'shopify' in file:
            shopify = pd.read_csv(path_source + file, usecols=columns_to_keep)
    events = pd.read_csv(path_source + event)
    return wix, godaddy, shopify, events

    # Rename columns for consistency
def rename_fields(wix, godaddy, shopify, events):
    wix.rename(columns={'Change %': 'wix_Change %'}, inplace=True)
    wix = convert_to_date_type(wix)
    shopify.rename(columns={'Change %': 'shopify_Change %'}, inplace=True)
    shopify = convert_to_date_type(shopify)
    godaddy.rename(columns={'Change %': 'godaddy_Change %'}, inplace=True)
    godaddy = convert_to_date_type(godaddy)

    events.rename(columns={'event_date': 'Date'}, inplace=True)
    convert_to_date_type_events(events)
    return wix, godaddy, shopify, events

def merge_data(wix, godaddy, shopify, events):
    # Merge all files on 'date'
    merged = wix.merge(shopify, on='Date', how='outer')
    merged = merged.merge(godaddy, on='Date', how='outer')
    merged = merged.merge(events, on='Date', how='outer')
    # merged.to_csv(path_source + 'aggregate_data_final_test1.csv', index=False)
    return merged
# ---------------------------------------------------------------------

def compare_data(final_file):
    data_dict = final_file.to_dict('records')
    prev_value = None
    for i in range(len(data_dict)):
        try:
            percentage = float(data_dict[i]['wix_Change %'].strip('%'))
            # data_dict[i]['wix_Change %'] = percentage
            # print(type(data_dict[i]['wix_Change %']))
            # print(data_dict[i]['wix_Change %'])
        except AttributeError:
            print("It seems that there is no value")
        else:
            pass
        finally:
            data_dict[i]['wix_Change %'] = percentage
            try:
                if i == 0:
                    prev_value = data_dict[i]['wix_Change %']
                else:
                    if abs(prev_value - data_dict[i]['wix_Change %']) > 10:
                        print("Huge", data_dict[i]['Date'], data_dict[i - 1]['Date'], prev_value - data_dict[i]['wix_Change %'], data_dict[i]['notes'])
            except AttributeError:
                print("It seems that there is no value")


# ----------------------- TEST CODE -----------------------
stock_files_of_year, event_file = find_all_files(2022)
wix, godaddy, shopify, events = open_files(stock_files_of_year, event_file)
wix, godaddy, shopify, events = rename_fields(wix, godaddy, shopify, events)
merged = merge_data(wix, godaddy, shopify, events)
compare_data(merged)

#------------------------------------------------------------



'''
# ------------------------ LOOP FOR YEARS -------------------------
# for year in year_list:
#     stock_files_of_year, event_file = find_all_files(year)
#     wix, godaddy, shopify, events = open_files(stock_files_of_year, event_file)
#     wix, godaddy, shopify, events = rename_fields(wix, godaddy, shopify, events)
#     merged = merge_data(wix, godaddy, shopify, events)
'''

'''
date_info = []
date_details = {}
def convert_to_date_type(source):
    percentage = 0
    for row in range(len(source)):
        date_str = source[row]['Date']
        date_date_type = datetime.strptime(date_str, "%m/%d/%Y").date()
        percentage = float(data_dict[row]['Change %'].strip('%'))
        data_dict[row]['Date'] = date_date_type
        data_dict[row]['Change %'] = percentage
        # print(type(data_dict[row]['Date']), type(data_dict[row]['Change %']))
    return data_dict

def compare_info(source):
    prev_value = None
    for i in range(len(data_dict)):
        if i == 0:
            prev_value = data_dict[i]['Change %']
        else:
            if abs(prev_value - data_dict[i]['Change %']) > 10:
                print("Huge", data_dict[i]['Date'], data_dict[i-1]['Date'], prev_value - data_dict[i]['Change %'])
# if I can find the dependicies, but how to understand that in other days when the % was not huge, israel did not do anything huge?
# how to force chatgpt or something shows the news about those dates?
# divide + >10 and - > 10 groups
convert_to_date_type(data_dict)
compare_info(data_dict)
'''
