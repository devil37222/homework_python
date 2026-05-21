import pytest
from string_utils import StringUtils


utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected



#Тестовые сценарии:

#Тестовый сценарий 1:

@pytest.mark.positive
@pytest.mark.parametrize("input_str", [
    ("   Test"),
    ])

def test_trim_positive(input_str):
    assert utils.trim(input_str)

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    (""),
    (" "),
    (),
    ])

def test_trim_negative(input_str):
    assert utils.trim(input_str)

#Тестовый сценарий 2:

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol", [
    ("Test","T"),
    ("123","2"),
    ])

def test_contains_positive(input_str, input_symbol):
    assert utils.contains(input_str, input_symbol)

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("Test","n"),
    ("123","4"),
    ])

def test_contains_negative(input_str, input_symbol):
    assert utils.contains(input_str, input_symbol)

#Тестовый сценарий 3:

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol", [
    ("Test","T"), 
    ("123","2"),
    ])

def test_delete_symbol_positive(input_str, input_symbol):
    assert utils.delete_symbol(input_str, input_symbol)

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("Test","n"),
    ("123","4"),
    ])

def test_delete_symbol_negative(input_str, input_symbol):
    assert utils.delete_symbol(input_str, input_symbol)