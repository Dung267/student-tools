import numbers


def celsius_to_fahrenheit(celsius):
    """Chuyển đổi Celsius sang Fahrenheit. Hỗ trợ int, float/double."""
    if not isinstance(celsius, numbers.Real):
        raise TypeError("Input must be a numeric type (int, float).")
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero (-273.15°C) is invalid.")
    return celsius * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(fahrenheit):
    """Chuyển đổi Fahrenheit sang Celsius. Hỗ trợ int, float/double."""
    if not isinstance(fahrenheit, numbers.Real):
        raise TypeError("Input must be a numeric type (int, float).")
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero (-459.67°F) is invalid.")
    return (fahrenheit - 32.0) * 5.0 / 9.0