from src.utils.nltk_helper import get_tokens_from_sentence, extract_keywords_from_sentence

def test_get_tokens_from_sentence():
    assert get_tokens_from_sentence("we have a nice dream") == ["nice", "dream"]

def test_extract_keywords_from_sentence():
    assert extract_keywords_from_sentence("we have a dream", ["dream", "hello"]) == ["dream"]
