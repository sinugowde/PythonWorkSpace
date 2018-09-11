import json


people_string = '''
{
    "people": [
    {
        "name": "John Smith",
        "phone": "615-555-7164",
        "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
        "has_license": false
    },
    {
        "name": Jane Doe",
        "phone": "560-555-5153",
        "emails": null,
        "has_license": true
    }]
}
'''

json_data = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  },
  {
    "userId": 1,
    "id": 4,
    "title": "eum et est occaecati",
    "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
  },
  {
    "userId": 1,
    "id": 5,
    "title": "nesciunt quas odio",
    "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
  }]

# print(json_data)
# print(type(json_data))
str = {'one': 1}
# json_data = {}
# json_data['data'] = []
# json_data['data'].append(str)
# with open('data.json', 'w+') as data_file:
#     json.dump(json_data, data_file)

with open('data.json', 'r') as data_file:
    file_output = json.load(data_file)
print(file_output[0])
print(type(file_output[0]))

if 'id' in file_output[0].keys():
    print('found it')
else:
    print('not there')
