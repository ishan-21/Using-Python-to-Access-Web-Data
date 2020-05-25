import json  # imports json library
data='''[
      {"name":"Ishan",
      "Id":"2019B3PS0504P",
      "y":"2"},
            {"name":"Vansh",
            "Id":"2019B4PS0621P",
            "y":"2"}]'''
# data in json is stored in the form of dictionaries and lists, since such data structures are available in all programming language
# -s it's easier to transfer data through json. Notice there's no step such as creating a xml tree.
info=json.loads(data) # similar to fromstring() in xml, intresting thing is that info is a python dictionary
for item in info:
    print("Name:",item["name"])
    print("Item:",item["Id"])
    print("Y:",item["y"])
    print("////////////////////")
# naturally there is no such thing as attribute in json notation
