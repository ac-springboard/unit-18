def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c"
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if not type(temp) == int and not type(temp) == float:
        return f"Invalid temp {temp}"
    if not unit_in == "f" and not unit_in == "c":
        return f"Invalid unit {unit_in}"
    if not unit_out == "f" and not unit_out == "c":
        return f"Invalid unit {unit_in}"
    if unit_in == unit_out:
        return unit_in
    if unit_in == "c":
        return round(temp * 9 / 5 + 32, 1)
    if unit_in == "f":
        return round((temp - 32) * 5 / 9, 1)


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("c", "f", 100, convert_temp("c", "f", 100), "should be 212.0")
print("c", "f", -273.15, convert_temp("c", "f", -273.15), "should be -459.7 (Absolute Zero, in Kelvin)")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", "x", convert_temp("f", "f", "x"), "should be Invalid temp x")

