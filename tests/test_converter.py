import pytest
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_standard_conversions():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0)
    assert fahrenheit_to_celsius(32) == pytest.approx(0.0)
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0)


def test_negative_temperature_conversions():
    # Điểm giao thoa tại -40 độ
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)
    assert fahrenheit_to_celsius(-40) == pytest.approx(-40.0)


def test_exception_negative_number_below_absolute_zero():
    """Kiểm tra ngoại lệ nhiệt độ âm dưới độ không tuyệt đối."""
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(-300)
    with pytest.raises(ValueError):
        fahrenheit_to_celsius(-500.0)


def test_type_exceptions():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("abc")
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)