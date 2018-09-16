import json
import os

dict = {'two': 2}
datastore = {"office": {
    "medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
  }
}

if os.stat('data.json').st_size == 0:
    json_data = []
json_data.append(datastore)
with open('data.json', 'w') as data_file:
    json.dump(json_data, data_file, indent=4)
    # json.dump(data_file, json_data, indent=4)

with open('data.json', 'r') as data_file:
    json_data = json.load(data_file)
    # print(json_data)

with open('data.json', 'w') as data_file:
    json_data.append(dict)
    json.dump(json_data, data_file, indent=4)

print("json_data[0]: {}\njson_data[1]: {}\n".format(json_data[0], json_data[1]))
