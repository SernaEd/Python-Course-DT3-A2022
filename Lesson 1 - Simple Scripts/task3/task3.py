def compare_two_variables(var_a, var_b):
    if type(var_a) == str or type(var_b) == str:
        return "string involved"
    elif var_a == var_b:
        return "equal"
    elif var_a > var_b:
        return "bigger"
    else:
        return "smaller"
