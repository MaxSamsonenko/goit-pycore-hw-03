from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    today = datetime.today().date()
    end_date = today + timedelta(days=7)  
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= end_date:
            if birthday_this_year.weekday() in (5, 6):  # 5 - субота, 6 - неділя
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.12.03"},
    {"name": "Alice Johnson", "birthday": "1987.01.28"},
    {"name": "Bob Brown", "birthday": "1992.11.30"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

