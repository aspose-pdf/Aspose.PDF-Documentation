---
title: Requisitos del Sistema
linktitle: Requisitos del Sistema
type: docs
weight: 30
url: /es/python-net/system-requirements/
description: Esta sección enumera los sistemas operativos compatibles que un desarrollador necesita para trabajar con éxito con Aspose.PDF para Python.
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sistemas operativos compatibles de Aspose.PDF para Python a través de .NET
Abstract: Aspose.PDF for Python via .NET es una API de procesamiento de PDF diseñada para que los desarrolladores gestionen documentos PDF sin necesidad de Microsoft Office o la automatización de Adobe Acrobat. Admite el desarrollo de aplicaciones Python de 32 bits y 64 bits en varios sistemas operativos, incluidos Windows y Linux, donde está instalado Python 3.5 o posterior. La API es compatible con varias versiones de Windows, desde Windows XP hasta Windows 11, y con las principales distribuciones de Linux como Ubuntu, OpenSUSE y CentOS. Para los sistemas Linux, los requisitos específicos incluyen bibliotecas de tiempo de ejecución GCC-6, dependencias del runtime de .NET Core (sin necesidad del runtime en sí), y la compilación pymalloc de Python para las versiones 3.5-3.7. Además, se necesita una biblioteca compartida libpython, lo que podría requerir ajustes de configuración para el reconocimiento correcto de la ruta de la biblioteca.
---

## Visión general

Aspose.PDF for Python a través de .NET, API de procesamiento de PDF que permite a los desarrolladores trabajar con documentos PDF sin necesitar Microsoft Office® o la automatización de Adobe Acrobat. Aspose.PDF para Python puede usarse para desarrollar aplicaciones Python de 32 bits y 64 bits para diferentes sistemas operativos (como Windows y Linux) donde está instalado Python 3.5 o posterior.

## Sistemas operativos compatibles

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- y otros

## Requisitos del sistema para Linux objetivo

- Bibliotecas de tiempo de ejecución GCC-6 (o posterior).

- Dependencias del runtime de .NET Core. No se requiere instalar el runtime de .NET Core.

- Para Python 3.5-3.7: se necesita la compilación pymalloc de Python. La opción de compilación --with-pymalloc de Python está habilitada por defecto. Normalmente, la compilación pymalloc de Python está marcada con el sufijo m en el nombre del archivo.

- Biblioteca compartida libpython de Python. La opción de compilación --enable-shared de Python está deshabilitada por defecto, algunas distribuciones de Python no incluyen la biblioteca compartida libpython. En algunas plataformas Linux, la biblioteca compartida libpython se puede instalar usando el gestor de paquetes, por ejemplo: sudo apt-get install libpython3.7. El problema común es que la biblioteca libpython se instala en una ubicación diferente a la ubicación estándar del sistema para bibliotecas compartidas. El problema puede resolverse usando las opciones de compilación de Python para establecer rutas de biblioteca alternativas al compilar Python, o creando un enlace simbólico al archivo de la biblioteca libpython en la ubicación estándar del sistema para bibliotecas compartidas. Normalmente, el nombre del archivo de la biblioteca compartida libpython es libpythonX.Ym.so.1.0 para Python 3.5-3.7, o libpythonX.Y.so.1.0 para Python 3.8 o posterior (por ejemplo: libpython3.7m.so.1.0, libpython3.9.so.1.0).



