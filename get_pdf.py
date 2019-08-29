import json
import base64

def handler(event, context):
    with open("sample.pdf", "rb") as f:
        b = base64.b64encode(f.read()).decode("utf-8")

    return {
        "statusCode": 200,
        "headers": {
            'Content-type' : 'application/pdf'
        },
        "body": b,
        "isBase64Encoded": True
    }
