from datetime import datetime
def get_days_from_today(date):
    try: 
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        days_from_today = (today - input_date).days
        
        print('days_from_today: ', days_from_today) 
        
        return days_from_today
    
    except ValueError:
        return "Invalid date format. Please use the format 'YYYY-MM-DD'."
    
get_days_from_today("2021-10-09")