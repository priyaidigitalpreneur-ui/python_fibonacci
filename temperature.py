import re


class Temperature:
    """Represents a temperature value and its unit."""

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


class TemperatureParser:
    """Validates and interprets user input."""

    def parse(self, user_input):
        user_input = user_input.strip()

        # Input must start with uppercase C or F
        # followed by a valid number.
        pattern = r"^([CF])([-+]?(?:\d+(?:\.\d*)?|\.\d+))$"

        match = re.fullmatch(pattern, user_input)

        if not match:
            raise ValueError(
                "Invalid input. Please enter the temperature "
                "with the correct 'C' or 'F' prefix."
            )

        unit = match.group(1)
        value = float(match.group(2))

        return Temperature(value, unit)


class TemperatureConverter:
    """Converts temperatures between Fahrenheit and Celsius."""

    def convert(self, temperature):

        if temperature.unit == "F":
            # Fahrenheit to Celsius
            celsius = (temperature.value - 32) * 5 / 9
            return Temperature(celsius, "C")

        elif temperature.unit == "C":
            # Celsius to Fahrenheit
            fahrenheit = (temperature.value * 9 / 5) + 32
            return Temperature(fahrenheit, "F")


class TemperatureFormatter:
    """Formats the conversion result."""

    def format(self, original, converted):

        # Display input without .0 when it is a whole number
        if original.value.is_integer():
            original_value = int(original.value)
        else:
            original_value = original.value

        if original.unit == "F":
            return (
                f"F{original_value} degrees Fahrenheit "
                f"is converted to {converted.value:.2f} degrees Celsius"
            )

        else:
            return (
                f"C{original_value} degrees Celsius "
                f"is converted to {converted.value:.2f} degrees Fahrenheit"
            )


class TemperatureConverterApp:
    """Controls the temperature converter application."""

    def __init__(self):
        self.parser = TemperatureParser()
        self.converter = TemperatureConverter()
        self.formatter = TemperatureFormatter()

    def run(self):

        print("Temperature Converter")
        print("=====================")
        print("Enter a temperature such as F51 or C11.")
        print("Type Q to quit.")

        while True:

            user_input = input("\nEnter temperature: ").strip()

            # Exit the program
            if user_input == "Q":
                print("Goodbye!")
                break

            try:
                # Validate and interpret input
                temperature = self.parser.parse(user_input)

                # Convert temperature
                converted = self.converter.convert(temperature)

                # Format and display result
                result = self.formatter.format(
                    temperature,
                    converted
                )

                print(result)

            except ValueError as error:
                print(error)


# Program entry point
if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.run()