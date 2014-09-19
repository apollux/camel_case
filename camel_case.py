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
    for c in data:
        if c.isupper():
            result += '_'
            result += c.lower()
        else:
            result += c
    return result

