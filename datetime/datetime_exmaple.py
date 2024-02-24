from datetime import datetime, timedelta

specific_date_time = datetime(2023, 5, 17, 15, 30, 0)
print("Specific Date : ", specific_date_time)


formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date: ", formatted_date)

date_string = "2024-01-03 18:45:30"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print('Parsed Date: ', parsed_date)

current_date = datetime.now().date()
future_date = current_date + timedelta(days=7)
past_date = current_date - timedelta(days=7)
print("current date: ", current_date)
print("future date: ", future_date)
print("future date: ", future_date+timedelta(days=1))
print("past date: ", past_date)

date1 = datetime(2024, 1, 15, 10, 30, 00)
date2 = datetime(2024, 1, 20, 11, 30, 00)
print("Time Difference: ", date2 - date1)

