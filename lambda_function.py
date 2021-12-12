import json

from scraper import titles

with open("index.html") as file:
    src = file.read()

def lambda_handler(event, context):
    # TODO implement
    
    return {
        'statusCode': 200,
        'headers': {
            "content-type": "text/html, charset=utf-8"
        },
        'body': src.format(titles)
    }