[`Backend con Python`](../../Readme.md) > [`Sesión 01`](../Readme.md) > Reto-01
# Reto 01: Creación de un ambiente virtual

## Objetivo
- Inicializar un ambiente virtual
- Instalar un modulo dentro de un ambiente virtual
- Generar un archivo requirements para tu ambiente virtual

## Desarrollo

En el ejemplo 03 se presentaron los ambientes virtuales y se describieron las ventajas que otorgan a proyectos en Django.

Identificaste las buenas prácticas para la generación de archivos de requerimientos e instalaste paquetes con pip.

Nota:
- Recuerda que tienes a tu disposición virtuanenv y venv para la generación de ambientes virtuales. La diferencia es que venv es una herramienta oficial de Python.

Para repasar generaremos una vez más un ambiente virtual. Está vez generaremos el ambiente virtual a partir de un archivo de requirements.

Si ha explorado cualquier proyecto de Python en Github o en otro lugar, probablemente has notado un archivo llamado requierements.txt este archivo de requisitos.txt se usa para especificar qué paquetes de Python se requieren para ejecutar el proyecto está utilizando.

Para este ejercicio guarda las siguientes líneas como un archivo requirements.txt

```
Django==1.5
MySQL-python==1.2.4
Pillow==2.0.0
```


1. Genera una carpeta con el nombre ambiente
2. Después, genera un ambiente virtual dentro de esta carpeta.
3. utiliza pip con los parametros necesarios para instalar el ambiente desde el archivo requitements.txt:
    - **a)** Recuerda mover el archivo requirements.txt a la carpeta correcta.
    - **b)** Recuerda que el parametro para instalar pip de un archivo de requisitos es: `pip install -r /path/to/requirements.txt`
    - **c)** Imprime la versión de Django para verificar que se instaló de acuerdo al archivo.



<details><summary>Solución</summary>

 Crear las carpetas desde un explorador o de la consola.

   ```console
   mkdir micarpeta
   ```

 Inicializa el ambiente virtual con:

   ```console
   python -m venv miambiente
   ```

 Activa tu ambiente utilizando el comando source o activando el script.ps1
Utiliza pip para instalar el archivo de requirements
```
pip install -r /path/to/requirements.txt
```
Para ver las versiones de tus modulos instalados. Utiliza
```
pip freeze
```
La versión instalada debería ser Django==1.5

</details>
</br>

