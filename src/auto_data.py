import random
import random
from khayyam import JalaliDatetime
from irani_dataset_list import *

def natinal_id():
    number = "6580"
    natinal_id = random.randint(100000, 999999)
    return number + str(natinal_id)

def email(index_1, index_2):
    first_part = english_fname[index_1]
    last_part = english_lname[index_2]
    number = random.randint(1, 999)
    
    full_email = first_part + last_part + str(number) + "@gmail.com"
    print(full_email)
    return str(full_email)

def telephone():
    code = "021"
    number = random.randint(00000000, 90000000)
    return code+str(number)

def phone_number():
    code_list = [
        "0910",
        "0919",
        "0937",
        "0922"
    ]
    code = random.choice(code_list)
    phone_number = code + str(random.randint(0000000, 9000000))
    return {"code": code, "phone_number":phone_number}

def Postal_Code():
    return str(random.randint(10000000, 90000000))

def generate_random_jalali_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    
    # تعداد روزهای هر ماه (29 روز برای اسفند در سال کبیسه)
    days_in_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

    # اگر ماه اسفند (ماه 12) است
    if month == 12:
        # بررسی سال کبیسه
        if (year % 4 == 3):
            day = random.randint(1, 29)  # سال کبیسه: 30 روز برای اسفند
        else:
            day = random.randint(1, 29)  # سال غیر کبیسه: 29 روز برای اسفند
    else:
        day = random.randint(1, days_in_month[month - 1])

    random_date = JalaliDatetime(year, month, day)
    return random_date.strftime('%Y-%m-%d')

def generate_random_time():

    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    
    return str(hour)+":"+str(minute)

def Flight_Number():
    return random.randint(10000000000, 9000000000)

def generate_random_plate():
    # تولید دو رقم اول
    letters = ['الف', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ط', 'ع', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

    first_two_digits = random.randint(10, 99)
    
    # تولید سه رقم میانی
    middle_three_digits = random.randint(100, 999)
    
    # انتخاب یک حرف رندوم
    letter = random.choice(letters)
    
    # تولید دو رقم آخر
    last_two_digits = random.randint(10, 99)
    
    # فرمت پلاک
    plate = f"{first_two_digits} {middle_three_digits} {letter} {last_two_digits}"
    
    return plate


def telegram_id(index_1, index_2):
    first_part = english_fname[index_1]
    last_part = english_lname[index_2]
    number = random.randint(1, 999)
    
    tel_id = "tel-"+first_part + last_part + str(number)
    return tel_id

def instagram_id(index_1, index_2):
    first_part = english_fname[index_1]
    last_part = english_lname[index_2]
    number = random.randint(1, 999)
    
    ins_id = "ins-"+first_part + last_part + str(number)
    
    return ins_id
    

