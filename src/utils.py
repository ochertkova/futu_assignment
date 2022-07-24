from datetime import datetime

def format_date(date_str, format_str = '%d/%m/%Y'):
    """Reformat GitHub provided date using format_str for user representation"""
    try:
        formatted_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime(format_str)
        return formatted_date
    except: # date_str was not a date string
        return None