import logging
import string, random
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = 
key = 

client = CosmosClient(endpoint, key)

database = client.create_database_if_not_exists(id="randomusernames")
container = database.create_container_if_not_exists(
    id="randomusernames",
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    numbers = requests.get('https://dpusernamegen2446.azurewebsites.net/api/service2?code=bDCVOfVwlXd7ryoZt4aFVymFwPf5ukcg6aEnJCC8dQj/pKudv1WOJg==').text
    letters = requests.get('https://dpusernamegen2446.azurewebsites.net/api/service3?code=LCsN79IeJGYHKutVG0MzEvq2MJ4IcNNFJ/NG4lgtlJkV9ZV2j3UL3A==').text
    numbers = str(numbers)
    username = numbers + letters
    username = list(username)
    random.shuffle(username)
    randusername = ''
    for char in username:
        if char in (string.ascii_letters):
            randusername += char
        elif char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            randusername += char
    container.create_item(body={"id":str(1), "username":randusername})
    return func.HttpResponse(f"{randusername}")
