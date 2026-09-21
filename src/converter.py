def celsius_to_fahrenheit(celsius):
    """Chuyển đổi nhiệt độ từ Celsius sang Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be an integer or float.")
    return celsius * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(fahrenheit):
    """Chuyển đổi nhiệt độ từ Fahrenheit sang Celsius."""
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be an integer or float.")
    return (fahrenheit - 32.0) * 5.0 / 9.0