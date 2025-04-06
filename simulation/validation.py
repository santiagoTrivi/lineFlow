def is_float(value):
    """Check if the input value is a valid float."""
    try:
        float(value)
        return True
    except ValueError:
        return False
    

def is_int(value):
    """Check if the input value is a valid integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False
    

def servers_validation(value):
    if value > 6:
        return False
    else:
        return True