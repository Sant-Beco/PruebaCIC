🌎 ProjectCIC
📌 Proyecto Django con MySQL para la gestión de datos, como información climática.

⚙️ Requisitos
✅ Python 3.8 o superior
✅ MySQL instalado y en ejecución
✅ (Opcional) Uso de un entorno virtual para aislar dependencias

📥 1. Clonar el repositorio
Ejecuta en la terminal:

bash

git clone https://github.com/tu-usuario/projectCIC.git
cd projectCIC

🐍 2. Crear y activar un entorno virtual
Se recomienda usar un entorno virtual para evitar conflictos de dependencias.

🔹 En Linux / macOS:

bash

python -m venv venv
source venv/bin/activate
🔹 En Windows:

bash

python -m venv venv
venv\Scripts\activate

📦 3. Instalar dependencias
Ejecuta el siguiente comando para instalar las dependencias del proyecto:

bash

pip install -r requirements.txt

🛠️ 4. Configurar la base de datos MySQL
1️⃣ Crea una base de datos en MySQL

Ejecuta en MySQL:

sql

CREATE DATABASE prueba_funcional;
2️⃣ Asegúrate de que el usuario tenga permisos adecuados:

sql

GRANT ALL PRIVILEGES ON prueba_funcional.* TO 'desarrollador'@'localhost' IDENTIFIED BY 'desarrollador58';
FLUSH PRIVILEGES;
3️⃣ Configura la base de datos en settings.py:

python

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


📌 5. Aplicar migraciones
Ejecuta el siguiente comando para crear las tablas en la base de datos:

bash

python manage.py migrate

🚀 6. Iniciar el servidor de desarrollo
Para ejecutar el servidor de Django:

bash
python manage.py runserver
Luego, abre en tu navegador:

🔗 http://127.0.0.1:8000