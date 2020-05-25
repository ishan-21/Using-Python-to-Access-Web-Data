import xml.etree.ElementTree as ET # importing the library used to make and disfigure xml-tree and aliasing it to ET

# '''text\ntext..''' is used to make data a single string
data='''<stuff>
           <users>
               <user y="7">
                   <name>Ishan</name>
                   <id>2019B3PS0504P</id>
               </user>
               <user y="9">
                   <name>Vansh</name>
                   <id>2019B4PS0621P</id>
               </user>
           </users>
         </stuff>'''

info=ET.fromstring(data) # this function is used to make a tree structure out of a text document if doc follows the rules of xml
tags=info.findall("users/user") # this returns a list, but remember only 2 tags in this form come as parameter otherwise bad
for tag in tags:                # things will happen ex: ("stuff/users/user") will not work
    print("Name:",tag.find("name").text) # notice ''or "" everywhere
    print("ID:",tag.find("id").text)  #.text is used to get the content
    print("Attruibute:",tag.get("y")) #.get("attribute_name") is used to get attribute
    print("/////////////////////////") # also notice in data that attribute value always comes between '' or ""
