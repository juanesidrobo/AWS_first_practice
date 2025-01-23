import json
import boto3
from decimal import Decimal

def decimal_to_native(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj) # Convierte a int si no hay decimales, de lo contrario a float
    raise TypeError

# Establecer el recurso de DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MunicipiosCauca')

def lambda_handler(event, context):
    # Obtener parámetros de consulta, manejando el caso en que sean None, ya que dio errores en pruebas
    query_params = event.get('queryStringParameters') or {}

    # Se maneja el caso en el que se solicita un municipio específico por nombre
    if 'nombre' in query_params:
        try:
            response = table.get_item(Key={'nombre': query_params['nombre']})
            if 'Item' in response:
                return {
                    'statusCode': 200,
                    'body': json.dumps(response['Item'], default=decimal_to_native)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'Municipio no encontrado'})
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error al consultar DynamoDB', 'error': str(e)})
            }

    # Aqui se retornan todos los municipios si no hay filtro en el json de la petición
    try:
        scan_response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(scan_response.get('Items', []), default=decimal_to_native)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al escanear DynamoDB', 'error': str(e)})
        }
