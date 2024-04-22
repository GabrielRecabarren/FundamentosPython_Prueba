# Generador de Sitio Web: Aves de Chile

Este es un proyecto desarrollado como parte de la Prueba de Fundamentos de Programación en Python de Desafío Latam. En esta prueba validaremos nuestros conocimientos de API respetando las buenas prácticas de modularización. El objetivo de este proyecto es crear un sitio web que liste algunas especies de aves típicas de Chile, mostrando sus nombres en español e inglés junto con sus imágenes.

## Descripción del Proyecto

La asociación de Amantes de los pájaros de Chile ha notado que actualmente no se tiene información de los distintos pájaros que pueden ser observados en Chile. Es por eso que les gustaría poder entender a manera de prototipo como poder listar muchos de estos especímenes. Para ello se solicita generar un prototipo muy sencillo en el cual se puedan observar algunas imágenes de pájaros típicos de Chile junto con su nombre en español e inglés. La idea es que esta información pueda ser eventualmente transformada en señaléticas bilingües que permitan fomentar el turismo en Chile.

Se da acceso a la API 'https://aves.ninjas.cl/api/birds', la cual da acceso a una base de datos con la información requerida.

## Requerimientos

1. Crear templates del HTML a utilizar. (3 Puntos)
2. Generar un llamado a la API que permita recopilar la información necesaria para construir el sitio. (5 Puntos)
3. Exportar el sitio creado como un archivo HTML que pueda ser abierto en el navegador. (2 Puntos)

## Estructura del Proyecto

- **main.py**: El script principal que se ejecuta para generar el sitio web.
- **api_requests.py**: Contiene la función para realizar el llamado a la API.
- **data_processing.py**: Contiene las funciones para procesar los datos obtenidos de la API.
- **html_templates.py**: Contiene los templates HTML para la representación de cada tarjeta de ave y la página principal del sitio.
- **README.md**: Este archivo que contiene la información sobre el proyecto.

## Modulación

El proyecto ha sido modularizado para mejorar su organización y legibilidad. Cada aspecto del proyecto se ha encapsulado en funciones o clases separadas, permitiendo un desarrollo más ordenado y mantenible.

## Ejecución del Proyecto

Para ejecutar el proyecto, simplemente ejecuta el script `main.py`. Esto generará el sitio web con el listado de aves de Chile y lo exportará como un archivo HTML.

## Autor

[GabrielRecabarren](https://github.com/gabrielRecabarren)


