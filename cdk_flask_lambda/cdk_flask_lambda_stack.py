import os

from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class CdkFlaskLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        flask_handler = _lambda.Function(
            self, 'FlaskHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda/'+ os.environ['ZAPPA_LAMBDA_PACKAGE']),
            handler='handler.lambda_handler',
            timeout=Duration.seconds(15),
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=flask_handler,
        )
