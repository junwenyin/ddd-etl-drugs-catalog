from datetime import datetime

def try_parsing_date(text, new_format='%Y-%m-%d'):
    for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d', '%d %B %Y', '%d %b %Y', '%d-%m-%Y'):
        try:
            return datetime.strptime(text, fmt).strftime(new_format)
        except ValueError:
            pass
    return None

def get_no_event_from_date(text, new_format='%Y%m%d'):
    return try_parsing_date(text, new_format)    