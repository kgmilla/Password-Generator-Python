# pylint: disable=unused-variable
from bitsToAscii import bit2BitArr, bitArrToDecimal, decimalToAscii, createAsciiStr
from pytest import raises



def test_returnSevenBitArray():
    '''Checks if the array is 7 bits long'''
    assert len(bit2BitArr()) == 7


def test_throwErrorIfNoInputBitArrToDecimal():
    with raises(Exception) as err_info:
        bitArrToDecimal() #pylint: disable=no-value-for-parameter
    assert err_info.type == TypeError
    assert 'missing 1 required positional argument' in str(err_info)

def test_correctDecimalValReturn():
    '''checks the value of the decimal value returned
    from the converted 7 bit array bitArrToDecimal'''
    assert bitArrToDecimal([0, 1, 1, 0, 1, 0, 1]) == 53
    assert bitArrToDecimal([0, 0, 1, 1, 0, 1, 0]) == 26
    assert bitArrToDecimal([0, 1, 0, 0, 0, 0, 0]) == 32
    assert bitArrToDecimal([1, 1, 0, 0, 0, 1, 1]) == 99

def test_throwErrorIfNoInputDecimalToAscii():
    with raises(Exception) as err_info:
        decimalToAscii() #pylint: disable=no-value-for-parameter
    assert err_info.type == TypeError
    assert 'missing 1 required positional argument' in str(err_info)

def test_correctDecimalToAsciiConversionReturn():
    '''Checks values of the Decimal to Ascii conversion
    with verified values and comparing the output'''
    assert decimalToAscii(70) == 'F'
    assert decimalToAscii(12) == None
    assert decimalToAscii(-4) == None
    assert decimalToAscii(127) == None
    assert decimalToAscii('n') == None

def test_throwErrorIfNoInputCreateAsciiStr():
    with raises(Exception) as err_info:
        createAsciiStr() #pylint: disable=no-value-for-parameter
    assert err_info.type == TypeError
    assert 'missing 1 required positional argument' in str(err_info)

def test_correctLengthStrCreateAsciiStr():
    '''test the length of the string in the return of
    the createAsciiStr function'''
    assert len(createAsciiStr(10)) == 10
    assert len(createAsciiStr(-1)) == 0