import pytest
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit_standard():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(37.0) == 98.6


def test_fahrenheit_to_celsius_standard():
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0


def test_negative_temperatures_and_edge_cases():
    # Điểm giao nhau giữa thang C và F là -40 độ
    assert celsius_to_fahrenheit(-40) == -40.0
    assert fahrenheit_to_celsius(-40) == -40.0
    assert celsius_to_fahrenheit(-17.7778) == pytest.approx(0.0, abs=0.01)


def test_invalid_input_types():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("abc")
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)