import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('sas_products')

#print(table.creation_date_time)

resp = table.scan()
# prod = resp["Items"]

def get_item(number):
    return resp["Items"][number]

def get_names():
    names = []
    for item in  resp["Items"]:
        names.append(item)
    return names
        