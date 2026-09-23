import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-stats')

def lambda_handler(event, context):
    # Update the 'views' count by +1 for item with id = '1'
    response = table.update_item(
        Key={'id': '1'},
        UpdateExpression='SET #v = #v + :val',
        ExpressionAttributeNames={'#v': 'views'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    # Get the updated view count
    updated_views = int(response['Attributes']['views'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET,OPTIONS'
        },
        'body': json.dumps({'views': updated_views})
    }