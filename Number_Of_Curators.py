import json
import requests

url = "https://api.scratch.mit.edu/studios/31186993/curators"

result = requests.get(url)
curator_data_json = result.text
curator_data = json.loads(curator_data_json)
amount_of_curators = len(curator_data)
target_amount = 1000
print("There are currently " + str(amount_of_curators) + " curators. " + str(target_amount - amount_of_curators) + " to go!")
input()