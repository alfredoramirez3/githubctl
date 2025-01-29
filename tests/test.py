import jmespath
import json
from rich import print

with open('people.json') as f:
    people = json.load(f)
    
print(people)
print()

def print_search(search, data):
    print(search)
    print(jmespath.search(search, data))
    print()
    
# search = "people[0].name"
# # print(jmespath.search(search_1, people))
# print_search(search, people)

# search = "people[*].name"
# # print(jmespath.search(search, people))
# print_search(search, people)

# search = "people[*].address.city"
# # print(jmespath.search(search, people))
# print_search(search, people)

search = "people[?name=='Bob']"
print_search(search, people)

search = "people[?age=='28']"
print_search(search, people)

search = "people[?age==`28`]"
print_search(search, people)