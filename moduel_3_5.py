def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) >= 2:
        next_result = get_multiplied_digits(int(str_number[1:]))
        if next_result == 0:
            return first
        return first * next_result
    else:
        return first


result = get_multiplied_digits(40203)
print(result)