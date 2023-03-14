class CalculatorService:
    def add(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> float:
        return x / y


class CalculatorServiceWithStatic:
    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y

    @staticmethod
    def subtract(x: int, y: int) -> int:
        return x - y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        return x * y

    @staticmethod
    def divide(x: int, y: int) -> float:
        return x / y


if __name__ == "__main__":
    my_calculator_service: CalculatorService = CalculatorService()
    print(my_calculator_service.add(1, 2))
    print(my_calculator_service.subtract(1, 2))
    print(my_calculator_service.multiply(1, 2))
    print(my_calculator_service.divide(1, 2))

    print(CalculatorServiceWithStatic.add(1, 2))
    print(CalculatorServiceWithStatic.subtract(1, 2))
    print(CalculatorServiceWithStatic.multiply(1, 2))
    print(CalculatorServiceWithStatic.divide(1, 2))
