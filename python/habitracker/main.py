import requests
from datetime import datetime
USERNAME="eligrimaldi"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "jwskdalksdhaljdasdlkj"
today = datetime.now()
date = today.strftime("%Y%m%d")
user_param = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}


pixel_post_config={
    "date" : date,
    "quantity" : "5.5",
}
pixel_put_config={
    "quantity" : "3.24"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text
#pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
# pixel_put_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230520"
# response = requests.put(url=pixel_put_endpoint,json=pixel_put_config,headers=headers)
# print(response.text)
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
response = requests.delete(url=pixel_delete_endpoint,headers=headers)