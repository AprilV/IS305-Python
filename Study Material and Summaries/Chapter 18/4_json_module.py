"""
JSON Module - Reading and Writing JSON Data
This demonstrates json.loads() and json.dumps() functions
"""

import json

# READING JSON with loads()
# loads() converts JSON string to Python value
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)

print(jsonDataAsPythonValue)  # Dictionary
print(jsonDataAsPythonValue['name'])  # 'Zophie'
print(jsonDataAsPythonValue['isCat'])  # True
print(jsonDataAsPythonValue['felineIQ'])  # None

# WRITING JSON with dumps()
# dumps() converts Python value to JSON string
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)

print(stringOfJsonData)  # JSON string

# JSON Data Types
# Python -> JSON
# dict -> object
# list -> array
# str -> string
# int/float -> number
# True -> true
# False -> false
# None -> null
