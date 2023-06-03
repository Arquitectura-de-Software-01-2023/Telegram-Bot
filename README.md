<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="https://botostore.com/netcat_files/6/7/preview_152786_1602785485.jpg" alt="Logo" width="300" height="300">
  </a>

  <h3 align="center">Telegram Bot</h3>

  <p align="center">
    Proyecto desarrollado para la materia de Arquitectura del Software
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="acerca-del-proyecto">Acerca del Proyecto</a>
      <ul>
        <li><a href="descripción">Descripción</a></li>
        <li><a href="tecnologías">Tecnologías</a></li>
      </ul>
    </li>
    <li>
      <a href="implementación">Implementación</a>
      <ul>
        <li><a href="requisitos">Requisitos</a></li>
        <li><a href="despliegue">Despliegue</a></li>
      </ul>
    </li>
    <li><a href="uso">Uso</a></li>
    <li><a href="contacto">Contacto</a></li>
  </ol>
</details>



<!-- ABOUT -->
## Acerca del Proyecto
![Telegram Bot Diagram](https://github.com/Arquitectura-de-Software-01-2023/Telegram-Bot/blob/main/Diagrama-Telegram%20Bot.jpg?raw=true)



En la anterior imagen se puede ver el diagrama de los componentes del proyecto, estos componentes son:

* Usuario
* Telegram
* API Gateway
* Lambda
* S3

El proyecto fue desarrollado para la materia de Arquitectura del Software, para la <a href="https://www.ucb.edu.bo">Universidad Católica Boliviana "San Pablo"</a>.

<!-- DESCRIPTION -->
### Descripción
Este proyecto consiste en el desarrollo de un bot de Telegram que proporciona recetas de comida a los usuarios y pasos de instalación de videojuegos. El bot permite a los usuarios enviar comandos para solicitar descripciones específicas y recibir instrucciones detalladas sobre el comando enviado.

#### Características principales del proyecto:
Las características principales del proyecto son las siguientes:

* El bot de Telegram está integrado con un backend desarrollado en AWS Lambda, utilizando el lenguaje de programación Python 3.7.
* Los datos de las recetas y videojuegos se almacenan en un bucket de Amazon S3 en formato JSON.
* Cada objeto tiene un identificador único (ID) y una descripción que incluye los pasos de preparación en el caso de comida y los pasos de instalación en el caso de los videojuegos.
* El bot responde a los comandos enviados por los usuarios y busca los datos correspondientes en el archivo JSON, devolviendo la descripción completa correspondiente al comando.
* Si un usuario envía un comando no reconocido, el bot muestra una lista de todos los comandos disponibles para los usuarios.
* Este proyecto es una muestra de cómo se puede utilizar la integración de Telegram con AWS Lambda y Amazon S3 para crear un bot de conversación que proporcione información útil y personalizada. Los usuarios pueden disfrutar de la comodidad de acceder a información directamente desde Telegram, facilitando la experiencia de búsqueda y centralización de información.

<!-- TECHNOLOGIES -->
### Tecnologías
Las tecnologías utilizadas para el proyecto fueron las siguientes:

  <a href="https://core.telegram.org" style="display: flex; flex-direction: column; align-items: center; text-decoration: none;">
      <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/telegram/telegram.png" alt="Telegram" style="width: 16%; height: auto;">
  </a>
  <a href="https://aws.amazon.com/es/lambda/" style="display: flex; flex-direction: column; align-items: center; text-decoration: none;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Amazon_Lambda_architecture_logo.svg/1200px-Amazon_Lambda_architecture_logo.svg.png" alt="AWS Lambda" style="width: 16%; height: auto;">
  </a>
  <a href="https://aws.amazon.com/s3/" style="display: flex; flex-direction: column; align-items: center; text-decoration: none;">
      <img src="https://static.us-east-1.prod.workshops.aws/public/c00a366f-e68a-43ef-bdb6-b120bc81e089/static/images/storage/s3-icon.png" alt="Amazon S3" style="width: 16%; height: auto;">
  </a>
  <a href="https://www.postman.com" style="display: flex; flex-direction: column; align-items: center; text-decoration: none;">
      <img src="https://yt3.googleusercontent.com/X-rhKMndFm9hT9wIaJns1StBfGbFdLTkAROwm4UZ3n9ucrBky5CFIeeZhSszFXBgQjItzCD0SA=s900-c-k-c0x00ffffff-no-rj" alt="Postman" style="width: 16%; height: auto;">
  </a>
  <a href="https://www.python.org" style="display: flex; flex-direction: column; align-items: center; text-decoration: none;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python" style="width: 16%; height: auto;">
  </a>
  <a href="https://www.json.org/json-es.html" style="display: flex; flex-direction: column; align-items: center; text-decoration: none;">
      <img src="https://cdn2.iconfinder.com/data/icons/file-formats-43/48/json-512.png" alt="JSON" style="width: 16%; height: auto;">
  </a>
  
<!-- TECHNOLOGIES -->
### Implementación
<!-- REQUIREMENT -->
### Requisitos
Antes de comenzar, se debe tener los siguientes requisitos instalados y configurados:
<ol>
    <li>Python 3: <a href="https://www.python.org/downloads/">Descargar Python</a></li>
    <li>Postman: <a href="https://www.postman.com/downloads/">Descargar Postman</a></li>
    <li>Cuenta de AWS: <a href="https://aws.amazon.com/es/free/">Crear cuenta de AWS</a></li>
  </ol>

<!-- DEPLOYMENT -->
### Despliegue
#### Configuración del webhook de Telegram mediante Postman
<ol>
  <li>Obtener el token del bot desde BotFather en Telegram.</li>
  <li>Abrir Postman y crea una nueva solicitud POST.</li>
  <li>Establecer la URL del webhook utilizando el siguiente formato: <br>
    <code>https://api.telegram.org/bot<token>/setWebhook?url=<webhook_url></code>, <br>
    reemplazando <code>&lt;token&gt;</code> con el token del bot y <code>&lt;webhook_url&gt;</code> con la URL del webhook.</li>
  <li>Enviar la solicitud y verificar que el webhook se haya configurado correctamente.</li>
</ol>
#### Configuración básica en AWS
<ol>
  <li>Iniciar sesión en la <a href="https://console.aws.amazon.com/">Consola de administración de AWS</a>.</li>
  <li>Crear un bucket en Amazon S3 para almacenar los datos del bot.</li>
  <li>Crear el lambda con el siguiente código:</li>
</ol>

<pre>
<code>
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
    url = f'https://api.telegram.org/<token>/sendMessage'

    # Initialize S3 client
    s3_client = boto3.client('s3')

    # Get list of commands from bucket.json
    try:
        response = s3_client.get_object(Bucket='<bucket-name>', Key='<object-json>')
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
</code>
</pre>

<ol start="4">
  <li>Configurar las políticas de acceso y permisos adecuados para el bucket y el lambda.</li>
  <li>Configurar el API Gateway con el lambda.</li>
  <li>Colocar el nombre del bucket en el código del lambda.</li>
  <li>Colocar el token previamente obtenido en el código del lambda.</li>
  <li>Agregar los dos objetos del presente repositorio en el bucket.</li>
  <li>Colocar el nombre del objeto.json en el código del lambda.</li>
</ol>

<!-- USE -->
## Uso
El bot ha sido desarrollado para proporcionar información y ejecutar comandos específicos a través de Telegram. Se puede utilizar este bot como base para construir cualquier tipo de bot personalizado según distintas necesidades.
<!-- CONTACT -->
## Contacto
Juan Carlos Avila Flores: [JuancaJcA](https://github.com/JuancaJcA)<br>
Link del Proyecto: [https://github.com/Arquitectura-de-Software-01-2023/Telegram-Bot](https://github.com/Arquitectura-de-Software-01-2023/Telegram-Bot)

<p align="right">(<a href="#readme-top">Volver Arriba</a>)</p>
