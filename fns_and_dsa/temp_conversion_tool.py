# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    try:
        # Get temperature input from user
        temp_input = input("Enter temperature (e.g., 32C or 89F): ").strip().upper()
        
        if not temp_input:
            raise ValueError("Empty input. Please enter a temperature.")
        
        # Extract numerical value and unit
        try:
            temp_value = float(temp_input[:-1])
            temp_unit = temp_input[-1]
        except (ValueError, IndexError):
            raise ValueError("Invalid temperature format. Please use format like 32C or 89F.")
        
        # Perform conversion based on unit
        if temp_unit == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp:.2f}°F")
        elif temp_unit == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please use C for Celsius or F for Fahrenheit.")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()