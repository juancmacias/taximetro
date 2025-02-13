# 🚕 Proyecto Python: Taxímetro Digital



Imagen creada con IA Recraft

<img src="https://raw.githubusercontent.com/juancmacias/taximetro/refs/heads/main/imagenes/ico.webp">

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt="python"> 
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostGreSQL">
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="Visual Studio">

<p align="left"><img src="https://img.shields.io/badge/Juan%20Carlos%20Macias-lightgray.svg">  <img src="https://img.shields.io/github/created-at/juancmacias/taximetro">
</p>

## 📝 Descripción del Proyecto

Este proyecto consiste en desarrollar un prototipo de taxímetro digital utilizando Python. El objetivo es modernizar el sistema de facturación de los taxis y crear un sistema que calcule las tarifas a cobrar a los clientes de manera precisa y eficiente.

## 📊 Niveles de Implementación

### 🟢 Nivel Esencial

Desarrollar un programa CLI (Interfaz de Línea de Comandos) en Python.

- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
- Implementar las siguientes funcionalidades básicas:
  - ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Iniciar un trayecto.
  - ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Calcular tarifa mientras el taxi está parado (2 céntimos por segundo).
  - ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Calcular tarifa mientras el taxi está en movimiento (5 céntimos por segundo).
  - ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Finalizar un trayecto y mostrar el total en euros.
  - ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Permitir iniciar un nuevo trayecto sin cerrar el programa.

### 🟡 Nivel Medio

- Implementar un sistema de logs para la trazabilidad del código.
- Agregar tests unitarios para asegurar el correcto funcionamiento del programa.
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Crear un registro histórico de trayectos pasados en un archivo de texto plano.
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Permitir la configuración de precios para adaptarse a la demanda actual.

### 🟠 Nivel Avanzado

- Refactorizar el código utilizando un enfoque orientado a objetos (OOP).
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Implementar un sistema de autenticación con contraseñas para proteger el acceso al programa.
- Desarrollar una interfaz gráfica de usuario (GUI) para hacer el programa más amigable.

### 🔴 Nivel Experto

- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Integrar una base de datos para almacenar los registros de trayectos pasados.
- Dockerizar la aplicación para facilitar su despliegue y portabilidad.
- Desarrollar una versión web de la aplicación accesible a través de internet.

## 🛠️ Tecnologías a Utilizar

- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg)Python
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg)Git y GitHub para control de versiones
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg)Trello o Jira para la gestión del proyecto [Projects GitHub](https://github.com/users/juancmacias/projects/9)
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg)Bibliotecas adicionales según el nivel de implementación: PostgreSQL, pandas, speech_recognition, pyttsx3. pygame (por ejemplo, logging, unittest, tkinter para GUI, SQLite para base de datos)
- Docker para containerización (nivel experto)
- Framework web como Flask o Django para la versión web (nivel experto)


## 📦 Entregables

- Repositorio de GitHub con el código fuente del proyecto.
- Demostración del CLI desarrollado.
- Presentación para público no técnico.
- Presentación técnica del código, destacando fortalezas y debilidades.
- Enlace al tablero Kanban (GitHub proyectos) utilizado para la organización del proyecto.

## ⏳ Plazo de Entrega

Dos semanas a partir de la fecha de inicio del proyecto.

## 💡 Consejos para el Desarrollo

- Comienza con el nivel esencial y ve agregando funcionalidades gradualmente.
- Utiliza control de versiones desde el inicio del proyecto.
- Realiza pruebas frecuentes para asegurar el correcto funcionamiento en cada etapa.
- Documenta tu código y mantén un registro de los cambios y decisiones de diseño.
- Considera la usabilidad y la experiencia del usuario, incluso en la versión CLI.


# Mí solución

- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) creación de un entorno CLI; necesitaremos:
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) base de datos PostgreSQL:
        - Utilice [mkdb](https://www.mkdb.sh/) es gratuido y funciona muy bien, podeis usar el que se ajuste a vuestras necesidades. Las tablas que usaremos sera:


## Base de datos
      
        ```
        CREATE TABLE IF NOT EXISTS precios(id SERIAL PRIMARY KEY, estado CHAR(20) NOT NULL, precio FLOAT)
        CREATE TABLE IF NOT EXISTS trayecto(id SERIAL PRIMARY KEY, fecha TIMESTAMP NOT NULL DEFAULT NOW(), precio DECIMAL(10,2) NOT NULL)
        CREATE TABLE IF NOT EXISTS usuarios(id SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL, usuario VARCHAR(50) NIQUE NOT NULL)
        ```

        Esas seran las tres principales tablas
## Dependencias:
        
Para instalar las dependencias, terminal, ser:

        ```
        $ pip install -r requirements.txt
        ```
Instalar el entorno para mejorar la eficación de ejecución.
## ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Experimental:
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Juego de práctica:
        Los operarios puede practicar con el entorno para mejorar su rendimiento en el desarrollo de sus funciones
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Comandos de voz:
        para ello usaremos 'speech_recognition' de Google, es gratuito, especial atención en la linea 19 donde indicamos el idioma que queremos que reconozca
            
            ```
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput, language='es-ES', show_all=False)
            ```
- ![.](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/octicons/IssueClosed.svg) Nos dice el menú
            para que nos diga el menú de forma hablada usaremos 'pyttsx3' simplemente le mandamos un texto y nos lo pasa a voz

[Readme-Workflows/Readme-Icons CDN files](https://cdn.jsdelivr.net/gh/Readme-Workflows/Readme-Icons@main/icons/)

[Las key para controlar](https://www.pygame.org/docs/ref/key.html)
