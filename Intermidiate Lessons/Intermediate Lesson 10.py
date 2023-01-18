"""
2023 1/6 ~ 2023 1/7
1444  جُمَادَىٰ ٱلثَّانِي 13 ~ 1444  جُمَادَىٰ ٱلثَّانِي 14

XML Processing - SAX
"""

# structured way to safe file on lower level (Locally not professional)

# XML (extensible markup language)
# build graphical user interface and more
# going to structure data - Platform independent

# for python, we have two different way to works with XML
# SAX - Simple Api for XML = USEFUL FOR LARGE, Work done top to bottom, requires less memory
# DOM - Document Object Module = USEFUL FOR SMALL, Work one any direction, requires more memory

import xml.sax

# content handler = handles the XML file = can do S = xml.sax.ContentHandler() but we're customizing this case
class GroupHandler(xml.sax.ContentHandler):

    # these method have these name, so we have to use specific name here - for xml

    # stating
    def startElement(self, nameElement, attributes):  #This function is called when handler process the element
        self.current = nameElement  #  getting to know what element im processing
        if self.current == "person": # pulling the data out from element person
            print("----------------")
            print(f'id: {attributes["id"]}')

    # reading
    def characters(self, content):  # reading data in the
        if self.current == "name":  # when element is <name>
            self.name = content  # saving the data in <name> as a content

        elif self.current == "age":
            self.age = content

        elif self.current == "weight":
            self.weight = content

        elif self.current == "height":
            self.height = content

    # printing
    def endElement(self, name):
        if self.current == "name":
            print(f'name:   {self.name}')  # used self.var cause it is not defined, so we're pulling from up

        elif self.current == "age":
            print(f'age:    {self.age}')

        elif self.current == "weight":
            print(f'weight: {self.weight}')

        elif self.current == "height":
            print(f'height: {self.height}')

        self.current = ""  # initializing the data after printing so it can process other person data




read = GroupHandler()

parser = xml.sax.make_parser()    # parser = Translate the file
parser.setContentHandler(read)
parser.parse('PersonData.xml')  # it starts getting all the <elements>,
                                # we need to process like line 25 to print data in the element

"""
This Lesson continues to file Intermediate Lesson 10-2.py
"""
