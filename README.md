# KronumApp
    Trabajo realizado de la mano de Carlos Manuel Soto de Freitas y Juan Camilo Amaya

    commando:
        - uvicorn app:app --reload 

### Librerias
    - fastapi uvicorn
    - python-dotenv
    - pip install peewee
    - pip install pymysql
    - pip install "pydantic[email]"
    - pip install "passlib[bcrypt]"
    - pip install "python-jose[cryptography]"
    - pip install python-multipart

### PROCESO PARA EL MONTAJE DE LA API y APLICACIÓN WEB
#### API 
    1- conar el repositorio 
    2- En la carpeta dockerMysql ejecutar docker-compose
    3- Importar base de datos carpeta DATABE/kronumapp.sql
    4- Instalar librerias
    5- poner api en marcha uvicorn app:app --reload
#### WEBAPP
    1- En una carpeta distinta, clonar el repositiorio https://github.com/juank2808/kronum_app_web
    2- si tiene Node instalado y npm dentro del repositorio instalado, ejecutar npm install
    3- ejecutar el comando npm run start para la aplicación web 
    4- logearse cliente1@gmail.com passwod:numeros del 1 al 8
    
   
