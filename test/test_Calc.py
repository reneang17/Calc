import numpy as np
import numpy.testing as npt
import pytest

import Calc

def test_Calc_smoke():
    #Smoke_test
    obt = Calc.Calc_object()

def test_Calc_object_fizz():
    #test the fizz_function
    obj = Calc.Calc_object()
    output = obj.fizz()
    npt.assert_equal(output, "buzz")

def test_add():
    result = Calc.add(3, 4)
    assert result == 7
    print('marker')

def test_add_string():
    with pytest.raises(TypeError):
        Calc.add("string", 4)

def test_add_float():
    with pytest.raises(TypeError):
        Calc.add(1.1, 4)

def test_mult():
    result = Calc.mult(3, 4)
    assert result == 12

def test_mult_string():
    with pytest.raises(TypeError):
        Calc.mult("string", 4)

def test_mult_float():
    with pytest.raises(TypeError):
        Calc.mult(1.1, 4)




