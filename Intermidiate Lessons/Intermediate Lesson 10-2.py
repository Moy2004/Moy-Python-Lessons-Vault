"""
2023 1/6 ~ 2023 1/7
1444  جُمَادَىٰ ٱلثَّانِي 13 ~ 1444  جُمَادَىٰ ٱلثَّانِي 14

XML Processing - DOM
"""
import xml.dom.minidom  # minimum implementation of dom module

# printing same thing as SAX using DOM module

domtree = xml.dom.minidom.parse('PersonData.xml')  # domtree is a way DOM view the files in a structure called tree
# Every element is branch of the dom tree ++ The whole xml/tree is loaded in a ram (prepared in script)

group = domtree.documentElement # finding Document element (main object) - group in this case

persons = group.getElementsByTagName('person')  # reading person from the group

# printing data
for person in persons:
    print('----------------')
    if person.hasAttribute('id'):
        print(f'id: {person.getAttribute("id")}')

    print(f'name: {person.getElementsByTagName("name")[0].childNodes[0].data }')
    # explain: from person, go to name element,0 = get first one,reading data, extracting data
    print(f'age: {person.getElementsByTagName("age")[0].childNodes[0].data}')
    print(f'weight: {person.getElementsByTagName("weight")[0].childNodes[0].data}')
    print(f'height: {person.getElementsByTagName("height")[0].childNodes[0].data}')

# manipulating/editing the xml file using DOM

persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Baby BuBu" # changing name

# this way it is only chaneged for this script not for XML so u have to commit to change the data in XML

domtree.writexml(open('PersonData.xml','w'))  # changing the data in the XML file

# creating + adding new elements to XML

newperson = domtree.createElement('person') # created person
newperson.setAttribute('id','4') # set Attribute as id and gave 4

name = domtree.createElement('name')  # create name element
name.appendChild(domtree.createTextNode('bobo')) # append bobo(name) into name element, it is independent from person

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('18'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('52'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('165'))

# adding it to person element
newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

# adding person in to group (document element)
group.appendChild(newperson)

domtree.writexml(open('PersonData.xml', 'w'))

"""
Quick 日記
今日の昼にボストンの韓国タウンで
라볶이を食べました
へっ、美味しいですよ
"""