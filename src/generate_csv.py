from irani_dataset_list import *
from auto_data import *
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Generate Random Data with Custom Columns")
parser.add_argument('--columns', nargs='+', choices=['First Name', 'Last Name FA', 'Last Name EN', 'Occupation', 'Email', 'Travel Date', 'Travel Time', 'Country', 'Airline', 'Cities', 'Vehicel', "Vehicel Color", "Vehicel Plate", 'Gender', 'Martial', 'Payment Status', 'Salary', "City_y", "City_x", "Instagram Id", "Telegram Id", "Postal Code", "Telephone", "Phone Number"], required=True, help="Select columns to include in the generated data")
args = parser.parse_args()

class GenerateData:
    def generate_data(self):
        data = []
        file_name = input("file name without .csv: ")
        for _ in range(1000):  # تولید 10 ردیف از داده‌ها
            farsi_name = random.choice(range(len(fname)))
            farsi_lname = random.choice(range(len(lname)))
            occupation = random.choice(Occupation)
            travel_date = generate_random_jalali_date(1360, 1403)
            travel_time = generate_random_time()
            natinalid = natinal_id()
            email_list = email(farsi_name, farsi_lname)
            country_list = random.choice(country)
            airlines_list = random.choice(airlines)
            cities_list = random.choice(cities)
            vehicles_list = random.choice(vehicles)
            gender_list = random.choice(gender)
            Marital_list = random.choice(Marital)
            payment_status_list = random.choice(payment_status)
            salary_list = random.choice(salary)
            city_y = random.choice(cities)
            city_x = random.choice(cities)
            vehic_color = random.choice(vehicle_color)
            # vehicel_plate = generate_random_plate()
            # insta_id = instagram_id()
            # tel_id = telegram_id()
            # postal_code = Postal_Code()
            # telephone_num = telephone
            
            
            row = []

            if 'First Name' in args.columns:
                row.append(fname[farsi_name])
            if 'Last Name FA' in args.columns:
                row.append(lname[farsi_lname])
            if 'Last Name EN' in args.columns:
                row.append(english_lname[farsi_lname])
            if 'Occupation' in args.columns:
                row.append(occupation)
            if 'Email' in args.columns:
                row.append(email_list)
            if 'Travel Date' in args.columns:
                row.append(travel_date)
            if 'Travel Time' in args.columns:
                row.append(travel_time)
            if "Natinal ID" in args.columns:
                row.append(natinalid)
            if "Country" in args.columns:
                row.append(country_list)
            if "Airline" in args.columns:
                row.append(airlines_list)
            if "Cities" in args.columns:
                row.append(cities_list)
            if "Vehicel" in args.columns:
                row.append(vehicles_list)
            if "Gender" in args.columns:
                row.append(gender_list)
            if "Martial" in args.columns:
                row.append(Marital_list)
            if "Payment Status" in args.columns:
                row.append(payment_status_list)
            if "Salary" in args.columns:
                row.append(salary_list)
            if "City_y" in args.columns:
                row.append(city_y)             
            if "City_x" in args.columns:
                row.append(city_x)             
            if "Vehicel Color" in args.columns:
                row.append(vehic_color)             
            if "Vehicel Plate" in args.columns:
                row.append(generate_random_plate())  

            if "Telegram Id" in args.columns:
                row.append(telegram_id(farsi_name, farsi_lname))
            if "Instagram Id" in args.columns:
                row.append(instagram_id(farsi_name, farsi_lname))       
            if "Postal Code" in args.columns:
                row.append(Postal_Code())
            if "Telephone" in args.columns:
                row.append(telephone())
            if "Phone Number" in args.columns:
                row.append(phone_number())

            data.append(row)

        df = pd.DataFrame(data, columns=args.columns)

        df.to_csv(f"{file_name}.csv", index=False, encoding='utf-8-sig')
        
        
GenerateData().generate_data()