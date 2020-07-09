# Header titles
key_header_names = ["Company", "Last", "Change", "Min", "Max"]

# space between each title
key_header_width = [47, 9, 10, 10, 10]

# all the keys of the attribute
key_content_names = ["last", "change", "min", "max"]

# space between each value
key_content_width = [10, 10, 10, 10, 10]

# build a header of the table


def displayHead():
    for (name, width) in zip(key_header_names, key_header_width):
        print(name.ljust(width), end="| ")
    print()


def displyContent(stock):
    for (name, width) in zip(key_content_names, key_content_width):
        print(str(stock[name].ljust(width)), end="| ")
    print()
