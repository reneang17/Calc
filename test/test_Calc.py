import numpy as np
import numpy.testing as npt

import Calc

def test_Calc_smoke():
    #Smoke_test
    obt = Calc.Calc_object()

def test_Calc_object_fizz():
    #test the fizz_function
    obj = Calc.Calc_object()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")
