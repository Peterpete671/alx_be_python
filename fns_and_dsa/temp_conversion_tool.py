# ==== Global Conversion Factors ====
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
KELVIN_OFFSET = 273.15


# ==== Conversion Functions ====
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def convert_to_kelvin(celsius):
    """Convert Celsius to Kelvin using the global factor."""
    return celsius + KELVIN_OFFSET


def convert_from_kelvin(kelvin):
    """Convert Kelvin to Celsius using the global factor."""
    return kelvin - KELVIN_OFFSET


def convert_fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin using intermediate Celsius."""
    return convert_to_kelvin(convert_to_celsius(fahrenheit))


def convert_kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit using intermediate Celsius."""
    return convert_to_fahrenheit(convert_from_kelvin(kelvin))


# ==== Main Program ====
def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()

        # Validate numeric input
        if not temp_input.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)
        unit = input("Is this temperature in Celsius, Fahrenheit, or Kelvin? (C/F/K): ").strip().upper()

        if unit == "F":
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
            print(f"{temperature}°F is {convert_fahrenheit_to_kelvin(temperature)}K")
        elif unit == "C":
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
            print(f"{temperature}°C is {convert_to_kelvin(temperature)}K")
        elif unit == "K":
            print(f"{temperature}K is {convert_from_kelvin(temperature)}°C")
            print(f"{temperature}K is {convert_kelvin_to_fahrenheit(temperature)}°F")
        else:
            raise ValueError("Invalid unit. Please enter C, F, or K.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
