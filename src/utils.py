from datetime import datetime

def format_date(date_str, format_str = '%d/%m/%Y'):
    formatted_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime(format_str)
    return formatted_date
