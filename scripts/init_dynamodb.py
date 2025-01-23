import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MunicipiosCauca')

with open('scripts/municipios.json', 'r') as file:
    municipios = json.load(file, parse_float=Decimal)

for municipio in municipios:
    table.put_item(Item=municipio)
    print(f"Added {municipio['nombre']}")
