try:
    foo()
except ZeroDivisionError as error:
    print("ZeroDivisionError")
except ArithmeticError as error:
    print("ArithmeticError")
except AssertionError as error:
    print("AssertionError")
