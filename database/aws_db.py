import boto3
import pandas as pd
dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-west-1",
    aws_access_key_id="AKIA5VPNJWY3SKKGWMV5",
    aws_secret_access_key="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"
)

table = dynamodb.Table("ThreatAlerts")

def load_alerts():
    response = table.scan()
    items = response.get("Items", [])
    return pd.DataFrame(items)