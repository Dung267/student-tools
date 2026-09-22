# tests/test_validator.py
from src.validator import is_number, is_positive_number

def test_is_number():
    # Số hợp lệ thông thường
    assert is_number("123") == True
    assert is_number("-45.6") == True
    assert is_number("0") == True
    
    # Ký hiệu số mũ (exponential notations)
    assert is_number("1e-4") == True
    assert is_number("-2.5e3") == True
    
    # NaN và Infinity (Cần trả về False theo logic mới)
    assert is_number("nan") == False
    assert is_number("inf") == False
    assert is_number("-inf") == False
    
    # Văn bản, chuỗi rỗng và kiểu dữ liệu khác
    assert is_number("abc") == False
    assert is_number("") == False
    assert is_number(None) == False

def test_is_positive_number():
    assert is_positive_number("10") == True
    assert is_positive_number("1e-4") == True
    
    assert is_positive_number("0") == False
    assert is_positive_number("-5.5") == False
    assert is_positive_number("nan") == False
    assert is_positive_number(None) == False