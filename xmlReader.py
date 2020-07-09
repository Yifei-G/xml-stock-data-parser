import xml.etree.ElementTree
from displayContent import displayHead, displyContent

try:
    stocks = xml.etree.ElementTree.parse("nyse.xml")
    # print a header of the table
    displayHead()
    for stock in stocks.findall("quote"):
        print(stock.text.ljust(46), end=" |")
        # stock.attrib is a dict
        displyContent(stock.attrib)

except FileNotFoundError:
    print("Can't found xml file in the directory!")
    exit(1)

except xml.etree.ElementTree.ParseError:
    print("Can't parse the xml data!")
    exit(2)
