from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb
)
from constructs import Construct

class MunicipiosCaucaApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Se crea la tabla DynamoDB para almacenar los municipios
        table = dynamodb.Table(
            self,
            "MunicipiosCauca",
            partition_key={"name": "nombre", "type": dynamodb.AttributeType.STRING}
        )

        # Se crea la función Lambda para obtener los municipios
        lambda_function = _lambda.Function(
            self,
            "MunicipiosLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="handler.lambda_handler",
            environment={
                "TABLE_NAME": table.table_name
            }
        )
        table.grant_read_data(lambda_function)

        api = apigateway.LambdaRestApi(
            self,
            "MunicipiosApi",
            handler=lambda_function,
            proxy=False
        )

        # Se define el endpoint de la API Gateway
        municipios_resource = api.root.add_resource("municipios")
        municipios_resource.add_method("GET")
