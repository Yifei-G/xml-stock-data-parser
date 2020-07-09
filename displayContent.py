key_header_names = ["Company", "Last", "Change", "Min", "Max"]
key_content_names = ["last", "change", "min", "max"]
key_header_width = [47, 9, 10, 10, 10]
key_content_width = [10, 10, 10, 10, 10]


def displayHead():
    for (name, width) in zip(key_header_names, key_header_width):
        print(name.ljust(width), end="| ")
    print()


def displyContent(stock):
    for (name, width) in zip(key_content_names, key_content_width):
        print(str(stock[name].ljust(width)), end="| ")
    print()
