import textwrap

def print_list_textwrap(list_str,width=90):
    """
    This prints a list in a way that is clean. \n
    prevents word wrap in console for long text. \n
    example input: ["banana", "apple", "orange"] \n
    example output: banana  apple orange
    """
    raw_text = "  ".join(list_str)  #convert a list of strings to strings seperated by "  "
    wrapped_text = textwrap.fill(raw_text, width)  # prevent word wrap in console
    print(wrapped_text)