def underscore_to_camel_case(data, start_with_capital=False,
                             keep_upper_case=False):
    next_to_upper = False
    result = ""
    first_non_underscore_handled = False
    if not keep_upper_case:
        data = data.lower()

    for i, c in enumerate(data):
        if start_with_capital and i == 0:
            c = c.upper()
        if c == '_':
            if first_non_underscore_handled:
                next_to_upper = True
        else:
            first_non_underscore_handled = True
            if next_to_upper:
                c = c.upper()
                next_to_upper = False
            result += c
    return result