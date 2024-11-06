---
title: Cómo ejecutar otros ejemplos
linktitle: Cómo ejecutar otros ejemplos
type: docs
weight: 50
url: es/net/how-to-run-other-examples/    
description: Esta página demuestra pautas que serán útiles para los siguientes requisitos antes de descargar y ejecutar los ejemplos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Requisitos del software

Asegúrate de cumplir con los siguientes requisitos antes de descargar y ejecutar los ejemplos.

1. Visual Studio 2010 o superior
1. Gestor de paquetes NuGet instalado en Visual Studio. Asegúrate de que la última versión de la API de NuGet esté instalada en Visual Studio. Para detalles sobre cómo instalar el gestor de paquetes NuGet, por favor consulta <https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools>
1. Ve a `Herramientas->Opciones->Gestor de paquetes NuGet->Fuentes de paquetes` y asegúrate de que la opción **nuget.org** esté seleccionada
1.
## Descargar desde GitHub

Todos los ejemplos de Aspose.PDF para .NET están alojados en [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-.NET).

- Puedes clonar el repositorio usando tu cliente de GitHub favorito o descargar el archivo ZIP desde [aquí](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/archive/master.zip).
- Extrae los contenidos del archivo ZIP en cualquier carpeta de tu computadora. Todos los ejemplos se encuentran en la carpeta **Examples**.
- Hay dos archivos de solución de Visual Studio, uno para Consola y otro para Aplicación Web.
- Los proyectos se crearon en Visual Studio 2013, pero los archivos de solución son compatibles con Visual Studio 2010 SP1 y superior.
- Abre el archivo de solución en Visual Studio y construye el proyecto.
- En la primera ejecución, las dependencias se descargarán automáticamente a través de NuGet.
- La carpeta **Data** en la carpeta raíz de **Examples** contiene archivos de entrada que los ejemplos de CSharp usan. Es obligatorio que descargues la carpeta **Data** junto con el proyecto de ejemplos.
- Abre el archivo *RunExamples.cs*, todos los ejemplos se llaman desde aquí.
- Abre el archivo *RunExamples.cs*, todos los ejemplos se llaman desde aquí.
- Descomenta los ejemplos que quieras ejecutar dentro del proyecto.

Si tienes algún problema configurando o ejecutando los ejemplos, no dudes en contactarnos a través de nuestros Foros.

## Contribuir

Si te gustaría añadir o mejorar un ejemplo, te animamos a contribuir al proyecto. Todos los ejemplos y proyectos de muestra en este repositorio son de código abierto y pueden ser utilizados libremente en tus propias aplicaciones.

Para contribuir, puedes hacer un fork del repositorio, editar el código fuente y crear un pull request. Revisaremos los cambios e incluiremos en el repositorio si resultan útiles.
