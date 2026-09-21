# src/validator.py

def is_number(input_string):
    """Kiểm tra xem chuỗi đầu vào có phải là một số hợp lệ không."""
    try:
        float(input_string)
        return True
    except (ValueError, TypeError):
        return False

def is_positive_number(input_string):
    """Kiểm tra xem chuỗi đầu vào có phải là số lớn hơn 0 không."""
    if is_number(input_string):
        return float(input_string) > 0
    return False