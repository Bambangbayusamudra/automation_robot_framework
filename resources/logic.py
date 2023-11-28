import random
import string
import re
from faker import Faker
from datetime import datetime, timedelta

def formated_get_dates_past():
    current_date = datetime.now()
    past_date = current_date - timedelta(days=3 * 30)

    formatted_past_date = past_date.strftime("%m/%d/%Y %I:%M:%S.%f %p")[:-3]
    return formatted_past_date

def formated_get_dates_current():
    current_date = datetime.now()

    formatted_current_date = current_date.strftime("%m/%d/%Y %I:%M %p")
    formatted_current_date_2 = current_date.strftime("%m/%d/%Y %I:%M:%S.%f %p")
    formatted_current_date_3 = current_date.strftime("%m/%d/%Y %I:%M:%S.%f %p")[:-3]

    return formatted_current_date, formatted_current_date_2, formatted_current_date_3

def formated_get_dates_future():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=3 * 30)

    formatted_future_date = future_date.strftime("%m/%d/%Y %I:%M %p")
    return formatted_future_date

formatted_past_date = formated_get_dates_past()
formatted_current_date, formatted_current_date_2, formatted_current_date_3 = formated_get_dates_current()
formatted_future_date = formated_get_dates_future()

def generate_biodata():
    fake = Faker()

    max_age = 50
    max_birth_date = datetime.now() - timedelta(days=365 * max_age)

    date_of_birth = fake.date_of_birth()
    while datetime.combine(date_of_birth, datetime.min.time()) < max_birth_date:
        date_of_birth = fake.date_of_birth()

    # Menghitung usia dengan menghitung selisih tahun antara tanggal lahir dan tanggal saat ini
    age = datetime.now().year - date_of_birth.year

    random_number = random.randint(15000000, 85000000)
    salary_value = f'{random_number}'

    occupation = ' '.join(fake.words(nb=2))

    biodata = {
        'Name': fake.first_name(),
        'Last Name': fake.last_name(),
        'Full Name': fake.name(),
        'Address': fake.address(),
        'Date of Birth': date_of_birth,
        'Age': age,
        'Email': fake.email(),
        'Salary': salary_value,
        'Phone Number': ''.join(filter(str.isdigit, fake.phone_number())),
        'Occupation': occupation,
        'Company': fake.company(),
        'Country': fake.country(),
        'Blood Type': random.choice(['A', 'B', 'AB', 'O']),
        'Hobbies': ', '.join(fake.words(nb=3)),
    }

    for key, value in biodata.items():
        globals()[key.replace(' ', '_')] = value

    return biodata

def generate_password():
    uppercase_alphabet = random.choice(string.ascii_uppercase)
    lowercase_alphabet = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    numeric = ''.join(random.choice(string.digits) for _ in range(3))
    special_characters = ''.join(random.choice(string.punctuation) for _ in range(2))
    random_string = uppercase_alphabet + lowercase_alphabet + numeric + special_characters
    return random_string


generated_biodata = generate_biodata()
print("Generated Biodata:")
print(generated_biodata)

generated_string = generate_password()
print(generated_string)
