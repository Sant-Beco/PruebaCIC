🌎 ProjectCIC - Gestión de Datos Climáticos con Django & MySQL

¡Bienvenido a ProjectCIC! 🚀 Este es un potente sistema basado en Django y MySQL, diseñado para la gestión y visualización de datos climáticos. Ideal para investigadores, científicos de datos y cualquier persona interesada en el monitoreo ambiental.

Con ProjectCIC, puedes:
✅ Recopilar y almacenar datos climáticos de forma eficiente.
✅ Consultar, analizar y visualizar información en tiempo real.
✅ Aprovechar la robustez de Django y la escalabilidad de MySQL.

⚙️ Requisitos
Antes de comenzar, asegúrate de contar con:

🐍 Python 3.8 o superior

🛢️ MySQL instalado y en ejecución

📡 Clave de API de OpenWeatherMap (Regístrate en OpenWeatherMap)

🏗️ (Opcional) Uso de un entorno virtual para aislar dependencias


📥 1. Clonar el repositorio
Para obtener una copia del proyecto, ejecuta:

![image](https://github.com/user-attachments/assets/91dfdc17-401a-4118-ba1c-24571648f2af)

git clone https://github.com/Sant-Beco/PruebaCIC.git

🐍 2. Crear y activar un entorno virtual
Se recomienda usar un entorno virtual para evitar conflictos de dependencias.

🔹 En Linux / macOS:

![image](https://github.com/user-attachments/assets/ae756a98-4338-4778-b3e0-989781237b4f)

![image](https://github.com/user-attachments/assets/f5c1383c-6ce7-4b57-9abb-cbbcb21b4fb3)

python -m venv venv

source venv/bin/activate

🔹 En Windows:

![image](https://github.com/user-attachments/assets/332a5769-1676-45c7-b622-2f5e498c70a0)

![image](https://github.com/user-attachments/assets/4bbe95ce-a4c5-483d-944c-d90e92bc4707)

python -m venv venv

venv\Scripts\activate

📦 3. Instalar dependencias
Ejecuta el siguiente comando para instalar las dependencias del proyecto:

![image](https://github.com/user-attachments/assets/50c68aa7-a237-46d7-bc1e-844370714247)

pip install -r requirements.txt

🔑 4. Configurar la API de OpenWeatherMap
Para obtener los datos del clima, debes agregar tu clave de API en el archivo de configuración de Django.

Abre settings.py
Añade tu clave API en la configuración:

![image](https://github.com/user-attachments/assets/644d386e-c95a-436c-9743-44d949eee241)


🛠️ 5. Configurar la base de datos MySQL
1️⃣ Crea una base de datos en MySQL

Ejecuta en MySQL:

![image](https://github.com/user-attachments/assets/cf25df41-75dc-4b84-b4ec-6e5b4939b057)

CREATE DATABASE prueba_funcional;

2️⃣ Asegúrate de que el usuario tenga permisos adecuados:

![image](https://github.com/user-attachments/assets/0c67cde3-985b-4107-bd79-a5894a58b8dd)

GRANT ALL PRIVILEGES ON prueba_funcional.* TO 'desarrollador'@'localhost' IDENTIFIED BY 'desarrollador58';
FLUSH PRIVILEGES;

3️⃣ Configura la base de datos en settings.py:

![image](https://github.com/user-attachments/assets/33391dbf-6ec8-4f20-bdd8-c599f50a3de4)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prueba_funcional',
        'USER': 'desarrollador',
        'PASSWORD': 'desarrollador58',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


📌 6. Aplicar migraciones
Ejecuta el siguiente comando para crear las tablas en la base de datos:

![image](https://github.com/user-attachments/assets/5b3f0185-d91a-4bce-9838-1f690ea59493)

python manage.py migrate

🚀 7. Iniciar el servidor de desarrollo
Para ejecutar el servidor de Django:

python manage.py runserver

![image](https://github.com/user-attachments/assets/2253e9f1-732b-4756-b975-164f2a66d219)

Luego, abre en tu navegador:
http://127.0.0.1:8000

🌦️ Ejecutar el script de descarga de datos climáticos

El script Script_data.py obtiene información del clima desde OpenWeatherMap y la almacena en la base de datos cada minuto.

▶️ Ejecutarlo manualmente
Para ejecutar el script de manera manual, usa:

![image](https://github.com/user-attachments/assets/5deae0b7-2907-45e6-8ff6-fc1076920aeb)

🎯 ¿Por qué elegir ProjectCIC?


✅ Código limpio y bien estructurado 🛠️ 

✅ Base de datos optimizada con MySQL 🛢️ 

✅ Automatización de datos climáticos en tiempo real 🌦️ 

✅ CRUD funcional y ágil 📝 

✅ Diseñado para escalar y crecer con facilidad 🚀 

✅ Consumo eficiente de APIs 🔗 
