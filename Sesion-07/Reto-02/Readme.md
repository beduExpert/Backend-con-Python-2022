[`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Reto-02
## Reto 01: Carga de proyecto en Beanstalk
### Objetivos
- Obtener una cuenta en Beanstalk
- Generar un nuevo registra para servir una aplicación web
- Inicializar una base de Datos en Beanstalk

### Desarrollo
En este reto utilizaremos PythonAnywhere para servir en internet nuestra aplicación en Django. Recuerda haber generado tu cuenta gratuita siguiendo los pasos del prework.

![](img/img1.jpg)

Con tu cuenta de AmazoAWS  realiza las siguientes operaciones:

- Inicializa un proyecto django-aws
    - Este es un proyecto normal de Django que integra los directorios .ebextensions y el archivo de configuración django.config.

- Configura una usuario en tu cuenta de AWS que pueda utilizar los servicios de beanstalk
    - Esto se realiza desde el panel de IAM. Agregando las políticas de servicios necesarios.

- Configura un proyecto de AWS Beanstalk y haz un deploy hacia AWS
    - Para esto debes tener instaladas y configuradas las herramientas de CLI de AWS.
    - Asegurarte de haber ingresado tu acces_key de usuario.
    - Utiliza los comandos `eb create` para dar de alta las infraestructuras necesarias.
    - Utiliza `eb deploy` para enviar el proyecto desde tu equipo hacia AWS.


<details>
<summary>
Solución
</summary>
Para inicializar tu proyecto django-aws utiliza el siguiente comando.

```
mkdir django-aws
cd .\django-aws\

python -m venv eb-virt
```
estos son los comandos para inicializar un proyecto en django de forma normal.

Para poder utilizar Beanstalk necesitarás utilizar generar el siguiente directorio.

```
mkdir .ebextensions
```

incluyendo la siguiente configuración que debe ser acorde al nombre de creación de tu proyecto en Django.

```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango.wsgi:application
```

Para configurar aws y tu usuario utiliza el siguiente comando. 

```
aws configure
```

Recuerda que debes haber inicializado tu usuario en IAM y agregado los permisos necesarios.

![](img/img1.jpg)

Para inicilizar tu proyecto en amazon AWS utiliza la CLI desde tu consola y corre los siguientes comandos.

```
eb init-p python-3.8 django-tutorial
eb create django-env
```

En este caso djnago-tutorial corresponde al nombre del proyecto django que se inicilalizó anteriormente.

Para hacer el deploy del proyecto utiliza.

```
eb deploy
```

</details>