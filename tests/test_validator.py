# tests/test_validator.py
from src.validator import is_number, is_positive_number

def test_is_number():
    # Các số hợp lệ
    assert is_number("123") == True
    assert is_number("-45.6") == True
    assert is_number("0") == True
    assert is_number("0.0") == True
    
    # Văn bản, chuỗi rỗng, khoảng trắng và ký tự đặc biệt
    assert is_number("abc") == False
    assert is_number("") == False
    assert is_number("   ") == False
    assert is_number("12abc") == False
    assert is_number("@#$") == False

def test_is_positive_number():
    # Số dương
    assert is_positive_number("10") == True
    assert is_positive_number("0.5") == True
    
    # Số 0 và số âm
    assert is_positive_number("0") == False
    assert is_positive_number("-5.5") == False
    
    # Văn bản và chuỗi không hợp lệ
    assert is_positive_number("abc") == False
    assert is_positive_number("") == False