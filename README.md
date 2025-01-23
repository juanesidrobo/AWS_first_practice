# API de Municipios del Cauca

Este proyecto implementa una API en AWS para consultar datos de los municipios del departamento del Cauca, Colombia. Utiliza servicios como AWS Lambda, DynamoDB y API Gateway, gestionados mediante AWS CDK. La API permite obtener una lista de todos los municipios o buscar uno en particular.

---

## **Características**
- **Consulta todos los municipios**: Obtiene la lista completa de municipios almacenados en DynamoDB.
- **Consulta por nombre**: Devuelve detalles de un municipio específico.
- **Infraestructura como código**: Todo el proyecto se gestiona usando AWS CDK en Python.

---

## **Tecnologías Utilizadas**
- **AWS Lambda**: Lógica de negocio.
- **AWS DynamoDB**: Almacenamiento de datos de los municipios.
- **AWS API Gateway**: Exposición del endpoint HTTP.
- **AWS CDK**: Provisión de infraestructura.
- **Python**: Lenguaje de programación para Lambda y CDK.

---

## **Requisitos Previos**
1. **Cuenta de AWS**: Debes tener una cuenta activa.
2. **Herramientas Instaladas**:
   - [AWS CLI](https://aws.amazon.com/cli/)
   - [Node.js y NPM](https://nodejs.org/)
   - [Python 3.x](https://www.python.org/)
   - AWS CDK:
     ```bash
     npm install -g aws-cdk
     ```
3. **Configurar Credenciales de AWS**:
   ```bash
   aws configure
   ```
4. **Entorno Virtual de Python**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate   # Windows
   ```

---

## **Estructura del Proyecto**
```plaintext
.
|-- lambda/
|   |-- handler.py                # Lógica de la función Lambda
|-- municipios_cauca_api/
|   |-- __init__.py
|   |-- municipios_cauca_api_stack.py  # Definición de infraestructura
|-- scripts/
|   |-- init_dynamodb.py          # Script para inicializar datos en DynamoDB
|   |-- municipios.json           # Datos de los municipios
|-- app.py                        # Punto de entrada para CDK
|-- cdk.json                      # Configuración de CDK
|-- requirements.txt              # Dependencias de Python
|-- README.md                     # Documentación del proyecto
```

---

## **Despliegue del Proyecto**

### **1. Instalar Dependencias**
Asegúrate de que el entorno virtual esté activado e instala las dependencias:
```bash
pip install -r requirements.txt
```

### **2. Inicializar AWS CDK**
Ejecuta el siguiente comando si es la primera vez que usas CDK en tu cuenta:
```bash
cdk bootstrap
```

### **3. Desplegar la Infraestructura**
Ejecuta el siguiente comando para desplegar los recursos:
```bash
cdk deploy
```
Confirma la creación de recursos escribiendo `y` cuando se te solicite.

### **4. Poblar la Tabla DynamoDB**
Ejecuta el script para cargar los datos iniciales en DynamoDB:
```bash
python scripts/init_dynamodb.py
```

---

## **Uso de la API**

### **1. Endpoint de la API**
El endpoint se proporciona después del despliegue de CDK. Ejemplo:
```plaintext
https://<API_ID>.execute-api.<region>.amazonaws.com/prod/municipios
```

### **2. Consultar Todos los Municipios**
Haz una solicitud GET al endpoint:
```bash
curl https://<API_ENDPOINT>/municipios
```

### **3. Consultar un Municipio Específico**
Incluye el nombre del municipio como parámetro de consulta:
```bash
curl "https://<API_ENDPOINT>/municipios?nombre=Popayán"
```

---

## **Créditos**
Este proyecto fue creado como un ejemplo de uso de AWS CDK para construir una API basada en servicios serverles por Juanes Idrobo :c.

