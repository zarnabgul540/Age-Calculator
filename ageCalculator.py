from datetime import date
from calendar import isleap

def is_leap_year(year):
    return isleap(year)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def get_valid_year():
    while True:
        try:
            year = int(input("Enter birth year (YYYY): "))
            if year <= date.today().year:
                return year
            else:
                print("❌ Year cannot be in the future. Try again.")
        except ValueError:
            print("❌ Please enter a valid year.")

def get_valid_month():
    while True:
        try:
            month = int(input("Enter birth month (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("❌ Month must be between 1 and 12.")
        except ValueError:
            print("❌ Please enter a valid month.")

def get_valid_day(year, month):
    while True:
        try:
            day = int(input("Enter birth day: "))
            if 1 <= day <= days_in_month(year, month):
                return day
            else:
                print("❌ Invalid day for the given month/year.")
        except ValueError:
            print("❌ Please enter a valid day.")

def calculate_age(birth_date, current_date):
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if days < 0:
        months -= 1
        prev_month = current_date.month - 1 or 12
        prev_year = current_date.year if current_date.month != 1 else current_date.year - 1
        days += days_in_month(prev_year, prev_month)

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def total_days_lived(birth_date, current_date):
    return (current_date - birth_date).days


# ---------------- MAIN PROGRAM ---------------- #

print("📅 AGE CALCULATOR (Advanced with Validation)\n")

name = input("Enter your name: ")

year = get_valid_year()
month = get_valid_month()
day = get_valid_day(year, month)

birth_date = date(year, month, day)
today = date.today()

years, months, days = calculate_age(birth_date, today)
total_months = years * 12 + months
total_days = total_days_lived(birth_date, today)

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"👤 Name: {name}")
print(f"🎂 Exact Age: {years} years, {months} months, {days} days")
print(f"📆 Total Months Lived: {total_months}")
print(f"⏳ Total Days Lived: {total_days}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
