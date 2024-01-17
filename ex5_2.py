def parse_line(line):
    """Return both the name and value in a line of text of the form name=value."""
    return tuple(line.split("="))
