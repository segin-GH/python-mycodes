#! /usr/bin/python3

import csv
import os


def log_data_to_csv(data, filename):
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the data to the CSV file
        writer.writerow(data)


def read_data_from_csv(filename):
    # Open the CSV file in read mode
    with open(filename, 'r') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)

        # Read the data from the CSV file
        data = list(reader)

    return data

#function the clean the csv file
def delete_csv_file(filename):
    if filename.endswith('.csv'):
        os.remove(filename)
    else:
        print("The provided file is not a CSV file.")

delete_csv_file('log.csv')

# add test info to csv file
data_to_log = ["TESTBENCH LOG RAW"]
log_data_to_csv(data_to_log, 'log.csv')

# Example usage
data_to_log = ['John Smith', '30', 'New York']
log_data_to_csv(data_to_log, 'log.csv')

data_from_file = read_data_from_csv('log.csv')
print(data_from_file)