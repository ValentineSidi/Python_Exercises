# Program to check baby temperature

# Get temperature from user
temperature = float(input("Enter baby temperature (in degrees Celsius): "))

# Check temperature and display appropriate message
if temperature > 37:
    print("Too high temperature")
elif temperature >= 34 and temperature <= 37:
    print("Normal temperature")
elif temperature < 34:
    print("Very low temperature")
