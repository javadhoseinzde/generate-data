from irani_dataset_list import *
from auto_data import *
import pandas as pd
import argparse
import random

parser = argparse.ArgumentParser(description="Generate Random Data with Custom Columns")
parser.add_argument('--columns', nargs='+', choices=['First Name', 'Last Name FA', 'Last Name EN', 'Job', 'Email', 'Travel Date', 'Travel Time', 'Country', 'Airline', 'Cities', 'Vehicel', "Vehicel Color", "Vehicel Plate", 'Gender', 'Martial', 'Payment Status', 'Salary', "City_y", "City_x", "Instagram Id", "Telegram Id", "Postal Code", "Telephone", "Phone Number", "Price"], required=True, help="Select columns to include in the generated data")
args = parser.parse_args()

class GenerateData:
    def generate_data(self):
        data = []
        file_name = input("file name without .csv: ")
        lengh = int(input("How much data should I create? "))

        for _ in range(lengh):
            farsi_name = random.choice(range(len(fname)))
            farsi_lname = random.choice(range(len(lname)))
            job = random.choice(jobs)
            travel_date = generate_random_jalali_date(1360, 1403)
            travel_time = generate_random_time()
            natinalid = natinal_id()
            email_list = email(farsi_name, farsi_lname)
            country_list = random.choice(country)
            airlines_list = random.choice(airlines)
            cities_list = random.choice(cities)
            vehicles_list = random.choice(vehicles)
            gender_list = random.choice(gender)
            marital_list = random.choice(Marital)
            payment_status_list = random.choice(payment_status)
            salary_list = random.choice(salary)
            city_y = random.choice(cities)
            city_x = random.choice(cities)
            vehic_color = random.choice(vehicle_color)
            prices = random.choice(price)

            # Dictionary to map each column to its respective data
            column_data = {
                'First Name': fname[farsi_name],
                'Last Name FA': lname[farsi_lname],
                'Last Name EN': english_lname[farsi_lname],
                'Job': job,
                'Email': email_list,
                'Travel Date': travel_date,
                'Travel Time': travel_time,
                'Natinal ID': natinalid,
                'Country': country_list,
                'Airline': airlines_list,
                'Cities': cities_list,
                'Vehicel': vehicles_list,
                'Vehicel Color': vehic_color,
                'Vehicel Plate': generate_random_plate(),
                'Gender': gender_list,
                'Martial': marital_list,
                'Payment Status': payment_status_list,
                'Salary': salary_list,
                'City_y': city_y,
                'City_x': city_x,
                'Telegram Id': telegram_id(farsi_name, farsi_lname),
                'Instagram Id': instagram_id(farsi_name, farsi_lname),
                'Postal Code': Postal_Code(),
                'Telephone': telephone(),
                'Phone Number': phone_number(),
                "Price": prices
            }

            # Generate a row based on the columns selected
            row = [column_data[col] for col in args.columns]

            data.append(row)

        df = pd.DataFrame(data, columns=args.columns)

        df.to_csv(f"{file_name}.csv", index=False, encoding='utf-8-sig')


GenerateData().generate_data()
