import unittest

from parameterized import parameterized
from moneyed import Money

from carys_cars.pricing_engine.duration_in_minutes import DurationInMinutes


class PricingEngine:
    def __init__(self, price_per_minute: Money) -> None:
        self.__price_per_minute = price_per_minute

    def calculate_price(self, duration: DurationInMinutes) -> Money:
        return self.__price_per_minute * duration.duration_in_minutes


class PricingEngineTest(unittest.TestCase):
    @parameterized.expand([
        [Money(0.24, "EUR"), DurationInMinutes(1), Money(0.24, "EUR")],
        [Money(0.24, "EUR"), DurationInMinutes(3), Money(0.72, "EUR")],
        [Money(0.36, "EUR"), DurationInMinutes(1), Money(0.36, "EUR")],
    ])
    def test_it_calculates_price_based_on_duration(
            self,
            price_per_minute: Money,
            trip_duration: DurationInMinutes,
            total_price: Money
    ):
        # Act
        actual = PricingEngine(price_per_minute).calculate_price(trip_duration)

        # Assert
        expected = total_price
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
