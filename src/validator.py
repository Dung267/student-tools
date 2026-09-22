# src/validator.py
import math

def is_number(input_string):
    """Kiểm tra xem chuỗi đầu vào có phải là một số hợp lệ không."""
    try:
        val = float(input_string)
        # Loại bỏ giá trị NaN (Not a Number) và vô cực (Infinity)
        if math.isnan(val) or math.isinf(val):
            return False
        return True
    except (ValueError, TypeError):
        return False

def is_positive_number(input_string):
    """Kiểm tra xem chuỗi đầu vào có phải là số lớn hơn 0 không."""
    if is_number(input_string):
        return float(input_string) > 0
    return False