import xml.etree.ElementTree
from displayContent import displayHead, displyContent

try:
    stocks = xml.etree.ElementTree.parse("nyse.xml")
    displayHead()
    for stock in stocks.findall("quote"):
        print(stock.text.ljust(46), end=" |")
        displyContent(stock.attrib)


except FileNotFoundError:
    print("Can't found xml file in the directory!")
