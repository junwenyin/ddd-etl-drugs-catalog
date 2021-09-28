from src.utils.date_utils import try_parsing_date, get_no_event_from_date

def test_try_parsing_date():
    assert try_parsing_date("2020/01/01") == "2020-01-01"
    assert try_parsing_date("1 Jan 2020") == "2020-01-01"
    assert try_parsing_date("01/01/2020") == "2020-01-01"
    assert try_parsing_date("2020-01-01") == "2020-01-01"

def test_get_format_date_for_path():
    assert get_no_event_from_date("2020/01/01") == "20200101"

