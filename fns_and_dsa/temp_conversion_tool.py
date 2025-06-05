# temp_conversion_tool.py

# 1. Define Global Conversion Factors
# Factors for converting Fahrenheit to Celsius: (F - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

# Factors for converting Celsius to Fahrenheit: (C * 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Accessing the global FAHRENHEIT_TO_CELSIUS_FACTOR for conversion
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Accessing the global CELSIUS_TO_FAHRENHEIT_FACTOR for conversion
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction for temperature conversion.
    Prompts for temperature and unit, performs conversion, and displays result.
    Handles non-numeric input by raising a ValueError.
    """
    # Prompt for temperature and handle non-numeric input by raising an error
    try:
        temp_input_str = input("Enter the temperature to convert: ").strip()
        # Attempt to convert to float. If it fails, ValueError is raised by float()
        temperature = float(temp_input_str)
    except ValueError:
        # Catch the ValueError from float() and re-raise with the specific message
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit and ensure valid input (C/F)
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break # Valid unit, exit loop
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Perform the conversion based on the chosen unit and display the result
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")

# Ensure main() is called when the script is executed directly
if __name__ == "__main__":
    main()