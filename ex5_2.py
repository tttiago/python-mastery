def parse_line(line):
    """Return both the name and value in a line of text of the form name=value."""
    try:
        name, value = line.split("=")
        return name, value  # Return a tuple
    except ValueError:
        return None
