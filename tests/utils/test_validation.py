from src.utils.validation import is_valid_pub_line

def test_is_valid_pub_line():
    assert is_valid_pub_line(["id","name"]) == False
    assert is_valid_pub_line(["id","title", "date", "journal"]) == False
    assert is_valid_pub_line(["","", "date", "journal"]) == False
    assert is_valid_pub_line(["id","", "date", "journal"]) == False
    assert is_valid_pub_line(["","", "date", "journal"]) == False
    assert is_valid_pub_line(["id","title", "2020-01-01", "journal"]) == True
    assert is_valid_pub_line(["id","title", "1 jan 2021", "journal"]) == True

