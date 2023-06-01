import json
import boto3
import requests

def lambda_handler(event, context):
    # Get body
    body = event['body']
    payload = json.loads(body)

    # Get values
    message = payload['message']['text']
    chat_id = payload['message']['chat']['id']
    
    # Set Telegram URL
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Get list of commands from bucket.json
    try:
        response = s3_client.get_object(Bucket='{bucket}', Key='{object_JSON}')
        data = response['Body'].read().decode('utf-8')
        bucket_data = json.loads(data)
        commands = [item['id'] for item in bucket_data]
    except:
        commands = []
    
    # Check if message is a command
    if message.startswith('/'):
        command = message[1:]
        
        # Check if command exists
        if command in commands:
            # Retrieve command description from bucket.json
            description = next(item['description'] for item in bucket_data if item['id'] == command)
            
            # Send result
            result = {
                'chat_id': chat_id,
                'text': description
            }
            requests.post(url, json=result)
            return {'status_code': 200}
        else:
            # Command not recognized
            available_commands = "\n/" + "\n/".join(command for command in commands if command != "start")
            response_message = f"Comando no existente, puede ingresar los siguientes comandos:\n{available_commands}"
        
            result = {
                'chat_id': chat_id,
                'text': response_message
            }
            requests.post(url, json=result)
            return {'status_code': 200}

    else:
        # Regular message, not a command
        result = {
            'chat_id': chat_id,
            'text': "Mensaje no reconocido como comando"
        }
        requests.post(url, json=result)
        return {'status_code': 200}
