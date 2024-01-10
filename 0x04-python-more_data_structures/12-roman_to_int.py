def to_subtract(subtract_list):
    to_subtract_value = 0
    max_value = max(subtract_list)

    for n in subtract_list:
        if max_value > n:
            to_subtract_value += n

    return max_value - to_subtract_value

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_keys = list(roman_numerals.keys())

    result = 0
    last_roman_value = 0
    subtract_list = [0]

    for char in roman_string:
        for roman_numeral in roman_keys:
            if roman_numeral == char:
                if roman_numerals.get(char) <= last_roman_value:
                    result += to_subtract(subtract_list)
                    subtract_list = [roman_numerals.get(char)]
                else:
                    subtract_list.append(roman_numerals.get(char))

                last_roman_value = roman_numerals.get(char)

    result += to_subtract(subtract_list)

    return result
