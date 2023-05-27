# Universidad
Framework Flask de python 

una aplicación web desarrollada utilizando Flask, un framework de Python para construir aplicaciones web. La aplicación consiste en un formulario de registro de estudiantes, un formulario de matrícula y un formulario para enviar PQRS (Peticiones, Quejas, Reclamos y Sugerencias). Los datos ingresados en los formularios se almacenan en una base de datos PostgreSQL.

Aquí hay una descripción general de las diferentes partes del código:

Importaciones: Se importan los módulos y clases necesarios, como request, render_template, Flask, SQLAlchemy, entre otros.

Configuración de la aplicación: Se crea una instancia de la aplicación Flask y se configura la conexión a la base de datos PostgreSQL.

Definición de modelos: Se definen tres modelos de base de datos utilizando la extensión SQLAlchemy: Registro, Matricula y PQRS. Cada modelo representa una tabla en la base de datos con sus respectivos campos.

Rutas: Se definen las rutas de la aplicación utilizando el decorador @app.route. Hay tres rutas principales:

Ruta '/' (raíz): Esta ruta renderiza el archivo de plantilla 'Inicio_TDEA.html', que muestra la página de inicio de la aplicación.

Ruta '/Registros': Esta ruta maneja tanto las solicitudes GET como las POST. Cuando se realiza una solicitud GET, se obtienen todos los registros de la base de datos y se muestran en la plantilla 'Registros.html'. Cuando se realiza una solicitud POST, se procesa el formulario de registro, se crea un nuevo objeto Registro y se almacena en la base de datos.

Ruta '/Matriculas': Esta ruta maneja tanto las solicitudes GET como las POST. Cuando se realiza una solicitud GET, se obtienen todas las matrículas de la base de datos y se muestran en la plantilla 'Matriculas.html'. Cuando se realiza una solicitud POST, se procesa el formulario de matrícula, se crea un nuevo objeto Matricula y se almacena en la base de datos.

Ruta '/PQRS': Esta ruta maneja tanto las solicitudes GET como las POST. Cuando se realiza una solicitud GET, se obtienen todas las PQRS de la base de datos y se muestran en la plantilla 'PQRS.html'. Cuando se realiza una solicitud POST, se procesa el formulario de PQRS, se crea un nuevo objeto PQRS y se almacena en la base de datos.

Inicialización de la aplicación: Se inicia la aplicación Flask y se ejecuta el servidor web si se ejecuta el script directamente.

Los archivos HTML en la carpeta "templates" son plantillas que se renderizan para mostrar el contenido en el navegador. Cada plantilla corresponde a una ruta específica en la aplicación Flask y utiliza la sintaxis de plantillas de Flask para mostrar los datos dinámicamente.

Es importante destacar que para ejecutar la aplicación correctamente, debes asegurarte de tener instalados los módulos y dependencias requeridos, como Flask, SQLAlchemy y Flask-Migrate. Además, debes crear la base de datos en PostgreSQL con las credenciales y la URL especificadas en el código.
