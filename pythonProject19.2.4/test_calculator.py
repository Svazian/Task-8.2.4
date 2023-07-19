from calculator import Calculator


class TestCalc:
    def setup(self):
        self.calculator = Calculator()

    def test_adding_success(self):
        assert self.calculator.adding(1, 1) == 2

    def test_multiply_success(self):
        assert self.calculator.multiply(1, 1) == 1

    def test_division_success(self):
        assert self.calculator.division(6, 2) == 3

    def test_subtraction_success(self):
        assert self.calculator.subtraction(3, 2) == 1

    def teardown(self):
        print("Выполнение метода Teardown")