import datetime
import calendar
from datetime import datetime


days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days_dict = {
    '월': 'Monday',
    '화': 'Tuesday',
    '수': 'Wednesday',
    '목': 'Thursday',
    '금': 'Friday',
    '토': 'Saturday',
    '일': 'Sunday'
}

    
# 현재 날짜와 시간을 원하는 형식으로 포맷
current_time = datetime.now().strftime("%Y-%m-%d-%H")


# 월
def get_month_name(month_number):
    
    if 1 <= int(month_number) <= 12:
        return calendar.month_name[int(month_number)]
    else:
        raise ValueError("Month number must be between 1 and 12.")