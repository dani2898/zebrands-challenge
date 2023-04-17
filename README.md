# zebrands-challenge

# Backend test 

El desarrollo de esta prueba se realizó haciendo uso de Python, haciendo uso de FastAPI y Postgresql.

Se proporciona un env.dist con las variables que se requieren para el desarrollo de la práctica, al levantarse solo de forma local y no tocar información sensible se proporcionan los valores de las variables, por esta ocasión, favor de generar un archivo .env en raíz del proyecto y copiar las variables.

# Contenedores

El desarrollo de los contenedores se realiza por medio de docker.

En este caso se generan y levantan dos imágenes:
1. Contenedor de API para manejo de productos y usuarios
2. Un pre-build de postgresq

En caso de que no se cuente con una configuración de docker en el equipo, favor de seguir los pasos explicados en el siguiente enlace:

[Linux](https://docs.docker.com/desktop/install/linux-install/)

[Windows](https://docs.docker.com/desktop/install/windows-install/)

## Build y run de contenedores

1. Desde el directorio donde se encuentre el proyecto, en raíz, correr el siguiente comando para hacer el build de contenedores:

	`docker-compose build`

	Anexo captura:

![Screenshot_1](https://user-images.githubusercontent.com/61600273/232625169-9a169c7f-8f18-4b53-a147-4a3a45c37ce3.png)

	
2. Para levantar los contenedor ejecutar el siguiente comando:
	`docker-compose up -d` 

	Anexo captura:

![Screenshot_2](https://user-images.githubusercontent.com/61600273/232625188-91a2b82c-8154-4771-8a09-56ca8ead4d5a.png)


3. Accedemos, desde consola, a los logs del contenedor con el siguiente comando:
	"zebrands" es el nombre que se especifica en el docker-compose.yaml para crear el contenedor.
	`docker-compose logs -f --tail 30 zebrands`

Anexo captura:

![Screenshot_3](https://user-images.githubusercontent.com/61600273/232625243-4ad4f197-4c17-4b33-935b-24685646402b.png)

Procederemos a la ejecutar las migraciones de la base de datos, asegurarse de generar en el gestor de base de datos de su preferencia una base de datos con las siguientes credenciales:

    HOST_POSTGRES=storage
    USER_POSTGRES=zebrands
    PASSWORD_POSTGRES=zebrands_pass
    DB_POSTGRES=zebrands
    DB_PORT=5432
    
Una vez realizado el paso anterior abrimos una terminal nueva en el mismo directorio del proyecto y ejecutamos el siguiente comando para entrar a la consola del contedor.
    	`docker-compose exec zebrands sh`
	
Una vez que estamos en consola ejecutamos:
	`poetry run alembic upgrade head`

 Anexo captura:

 ![Screenshot_4](https://user-images.githubusercontent.com/61600273/232625303-c94cce0c-169f-4217-86bc-a89e10c46521.png)

  Se mostrará que las migraciones se corren de manera exitosa, además se agregan un par de registros con usuarios de prueba para que puedan acceder al token de acceso y probar los demás endpoints.
  
   Comprobamos que en la base de datos que creamos en el gestor ya tenemos nuestras tablas generadas:
 
 ![Screenshot_5](https://user-images.githubusercontent.com/61600273/232625340-e1a591c3-bd38-446b-8285-e4ee1f837abf.png)
  
Los usuarios de prueba son los siguientes:
email : danielavilla2898@gmail.com
email: fasttest2023api@outlook.com

password para ambos: superadmin

 Hasta este momento nuestros contenedores ya están activos, y nuestra base de datos lista con usuarios de prueba y brands para asignar a los productos.

Nos dirigimos a la siguiente url para hacer consulta de la documentación autogenerada:

http://localhost:5001/docs

![Screenshot_6](https://user-images.githubusercontent.com/61600273/232625459-a7791df1-9199-40ad-b529-439d15ca5c2b.png)
	
Para la prueba de correos se utiliza fastapi-mail, se proporciona un mail para que puedan verificar el envío y recepción de correos:

fasttest2023api@outlook.com
pass: mailing2023

Sin embargo cualquier correo que se registre durante la creación de un usuario debe de recibir un mail cuando se haga una actualización en un producto.

También se optó por no eliminar de forma definitiva los productos, en cambio se colocan con un status inactivo, esto siguiendo la lógica de que la información pueda ser utilizada para reportes en un futuro, como se plantea en la prueba, de esta forma evitamos la pérdida de información.

Se hace uso de una arquitectura de capas, esto para una mayor organización de código y posible escalabilidad del proyecto al tener cada elemento separado de acuerdo a su función y con los archivos que cada uno requiere.

De esta forma incluso si se desea realizar una modificación al proyecto ya establecido no debería de resultar en inconvenientes.

Quedo al pendiente de cualquier duda que se pueda presentar durante la revisión de la prueba.

Daniela Villa Bárcenas
