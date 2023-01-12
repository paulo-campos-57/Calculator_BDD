import numbers


class operationError(Exception):
    pass


class Somator:
    def sum(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 + op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral):
            raise operationError(f"{op} is not a number!")


class Subtractor:
    def sub(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 - op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral):
            raise operationError(f"{op} is not a number!")


class Multiplier:
    def mult(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 * op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral):
            raise operationError(f"{op} is not a number!")


class Divider:
    def div(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 / op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral):
            raise operationError(f"{op} is not a number!")

    def _check_zero_(self, op):
        if op == 0:
            raise operationError("Unable to perform division by zero")
