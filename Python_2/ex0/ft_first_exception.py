def check_temperature(temp_str):
    temp = None
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}ºC is too hot for plants (max 40ºC)\n")
        elif temp < 0:
            print(f"Error: {temp}ºC is too cold for plants (min 0ºC)\n")
        else:
            print(f"Temperature {temp}ºC is perfect for plants!\n")
            return temp
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")
