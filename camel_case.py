def underscore_to_camel_case(data, start_with_capital=False,
                             keep_upper_case=False):
    next_to_upper = False
    result = ""
    first_non_underscore_handled = False
    if not keep_upper_case:
        data = data.lower()

    for c in data:
        if c == '_':
            if first_non_underscore_handled:
                next_to_upper = True
        else:
            if not first_non_underscore_handled:
                if start_with_capital:
                    c = c.upper()

            first_non_underscore_handled = True
            if next_to_upper:
                c = c.upper()
                next_to_upper = False
            result += c
    return result


def camel_case_to_underscore(data):
    result = ""
    previous_was_capital = False
    consecutive_capitals = False

    for i, c in enumerate(data):
        if c.isupper():
            if previous_was_capital:
                consecutive_capitals = True
            else:
                if i != 0:
                    result += '_'

            if consecutive_capitals:
                try:
                    if data[i + 1].islower():
                        result += '_'
                except IndexError:
                    pass
            result += c.lower()

            previous_was_capital = True
        else:
            result += c

            previous_was_capital = False
            consecutive_capitals = False
    return result

