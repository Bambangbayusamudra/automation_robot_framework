from datetime import datetime, timedelta

def get_dates():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=3*30)
    formatted_current_date = current_date.strftime("%m/%d/%Y %I:%M %p")
    formatted_future_date = future_date.strftime("%m/%d/%Y %I:%M %p")
    return formatted_current_date, formatted_future_date


