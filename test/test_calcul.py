import pytest
from calcul import text_to_stack
from calcul import check_element
from calcul import make_operation_from_stack
from calcul import make_operation


def test_text_to_stack():
    assert text_to_stack("10 12 +") == ['10', '12', '+']
    assert text_to_stack("10 -12 +") == ['10', '-12', '+']
    assert text_to_stack("") == []
    assert text_to_stack("            ") == []
    assert text_to_stack("      1         + 2390      ") == ['1', '+', '2390']
    assert text_to_stack("10 -12 +*") == ['10', '-12', '+', '*']
    assert text_to_stack("10 -12/+23*-4") == ['10', '-12', '/', '+', '23', '*', '-4']
    assert text_to_stack("-4-9-") == ['-4', '-9', '-']
    assert text_to_stack("1.5 1+") == ['1.5', '1', '+']


def test_check_element():
    assert check_element("12") == 12
    assert check_element("0") == 0
    assert check_element("-12") == -12
    assert check_element("+") == '+'
    assert check_element("-") == '-'
    assert check_element("*") == '*'
    assert check_element("/") == '/'
    with pytest.raises(Exception):
        assert check_element("12+")
        assert check_element("1+2")
        assert check_element(".")
        assert check_element("1 12 .")



def test_make_operation_from_stack():
    assert make_operation_from_stack(['10', '12', '+']) == 22
    assert make_operation_from_stack(['10', '12', '+', '2', '*']) == 44
    assert make_operation_from_stack(['3', '2', '/']) == 1.5
    # (1+2) - (3+4)*5 = 3 - 35 = -32
    assert make_operation_from_stack(['1', '2', '+', '3', '4', '+', '5', '*', '-']) == -32
    assert make_operation_from_stack(['-4', '-9', '-']) == 5
    assert make_operation_from_stack(['1.5', '1', '+']) == 2.5

    with pytest.raises(Exception):
        assert make_operation_from_stack(['10', '12+'])
        assert make_operation_from_stack(['10', '12', '1', '+'])
        assert make_operation_from_stack(['10', '-'])
        assert make_operation_from_stack([])
        assert make_operation_from_stack(['1', '2', '+', '3', '4', '+', '5', '*', '-', '-'])

def test_make_operation():
    assert make_operation(" 10 12  +  ") == 22
    assert make_operation("10 12 + 2 *") == 44
    assert make_operation("3 2 /") == 1.5
    assert make_operation("1 2 + 3 4 + 5 * -") == -32
    assert make_operation("1 2+3 4+5*-") == -32
    assert make_operation("  1 2   +    3  4 +    5 * -        ") == -32
    assert make_operation("-4-9-") == 5
    assert make_operation("1.5 1+") == 2.5

    with pytest.raises(Exception):
        assert make_operation("10 12+")
        assert make_operation("10 12 1 +")
        assert make_operation("10 -")
        assert make_operation("")
        assert make_operation("1 2 + 3 4 + 5 * - -")