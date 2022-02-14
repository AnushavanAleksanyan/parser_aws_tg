import json

from scraper import titles
import database_query as q

with open("index.html") as file:
    src = file.read()


def lambda_handler(event, context):
    # TODO implement
    # GET_RAW_PATH = "/getProduct"
    # CREATE_RAW_PATH = "/createProduct"
    
    # if event['rawPath'] == GET_RAW_PATH:
       # #getPerson path
       # print("Start request getPerson")
       # productname = event['queryStringParameters']['productName']
       # return {"name":"Mike"}
    # elif event['rawPath'] == CREATE_RAW_PATH:
       # #CreatePerson path - write to database
       # print("Start request createPerson")
    return {
        'statusCode': 200,
        'headers': {
            "content-type": "text/html, charset=utf-8"
        },
        'body': src.format(titles, q.get_item(1))
    }
