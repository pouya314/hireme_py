def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise Exception("Cannot covert {} to a boolean".format(s))
