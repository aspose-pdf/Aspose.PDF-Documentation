---
title: Cómo ejecutar otros ejemplos de Aspose.PDF para C++
linktitle: Cómo ejecutar otros ejemplos
type: docs
weight: 50
url: /es/cpp/how-to-run-other-examples/
description: Esta página demuestra pautas que serán útiles para los siguientes requisitos antes de descargar y ejecutar los ejemplos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Requisitos de software

Asegúrese de cumplir con los siguientes requisitos antes de descargar y ejecutar los ejemplos.

1. Microsoft Visual Studio 2017 o posterior.
1. Administrador de paquetes NuGet instalado en Visual Studio. Asegúrese de que la última versión de la API de NuGet esté instalada en Visual Studio. Para obtener detalles sobre cómo instalar el administrador de paquetes NuGet, consulte <http://docs.nuget.org/ndocs/guides/install-nuget>
1. Vaya a `Herramientas->Opciones->Administrador de paquetes NuGet->Fuentes de paquetes` y asegúrese de que la opción **nuget.org** esté marcada
1. El proyecto de ejemplo utiliza la función de Restauración Automática de Paquetes de NuGet, por lo tanto, debes tener una conexión a internet activa. Si no tienes una conexión a internet activa en la máquina donde se van a ejecutar los ejemplos, por favor revisa [Instalación](/pdf/es/cpp/installation/) y añade manualmente la referencia a Aspose.PDF.dll en el proyecto de ejemplo.

## Descargar desde GitHub

Todos los ejemplos de Aspose.PDF para C++ están alojados en [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-C).

- Puedes clonar el repositorio usando tu cliente de GitHub favorito o descargar el archivo ZIP desde [aquí](https://codeload.github.com/aspose-pdf/Aspose.PDF-for-C/zip/master).
- Extrae el contenido del archivo ZIP a cualquier carpeta en tu computadora. Todos los ejemplos están ubicados en la carpeta **Examples**.
- Hay dos archivos de solución de Visual Studio, uno para Consola y otro para Aplicación Web.
- Los proyectos están creados en Visual Studio 2013, pero los archivos de solución son compatibles con Visual Studio 2010 SP1 y superiores.

- Abre el archivo de solución en Visual Studio y compila el proyecto.- En la primera ejecución, las dependencias se descargarán automáticamente a través de NuGet.
- La carpeta **Data** en la carpeta raíz de **Examples** contiene los archivos de entrada que los ejemplos de CSharp utilizan. Es obligatorio que descargues la carpeta **Data** junto con el proyecto de ejemplos.
- Abre el archivo *RunExamples.cs*, todos los ejemplos se llaman desde aquí.
- Descomenta los ejemplos que deseas ejecutar desde dentro del proyecto.

No dudes en comunicarte usando nuestros foros si tienes algún problema configurando o ejecutando los ejemplos.

## Contribuir

Si deseas agregar o mejorar un ejemplo, te animamos a contribuir al proyecto. Todos los ejemplos y proyectos de demostración en este repositorio son de código abierto y pueden ser utilizados libremente en tus propias aplicaciones.

Para contribuir, puedes bifurcar el repositorio, editar el código fuente y crear una solicitud de extracción. Revisaremos los cambios y los incluiremos en el repositorio si resultan útiles.