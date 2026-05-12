---
title: Requisitos del sistema
linktitle: Requisitos del sistema
type: docs
weight: 30
url: /es/python-net/system-requirements/
description: Esta sección enumera los sistemas operativos compatibles que un desarrollador necesita para trabajar con éxito con Aspose.PDF for Python.
lastmod: "2025-02-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sistemas operativos compatibles de Aspose.PDF for Python via .NET
Abstract: Aspose.PDF for Python via .NET es una API de procesamiento de PDF diseñada para que los desarrolladores gestionen documentos PDF sin necesidad de Microsoft Office o Adobe Acrobat Automation. Admite el desarrollo de aplicaciones Python de 32 bits y 64 bits en varios sistemas operativos, incluidos Windows y Linux, donde está instalado Python 3.5 o posterior. La API es compatible con varias versiones de Windows, desde Windows XP hasta Windows 11, y con las principales distribuciones de Linux como Ubuntu, OpenSUSE y CentOS. Para los sistemas Linux, los requisitos específicos incluyen bibliotecas de tiempo de ejecución GCC-6, dependencias del .NET Core Runtime (sin necesitar el runtime en sí), y la compilación pymalloc de Python para las versiones 3.5-3.7. Además, se necesita una biblioteca libpython compartida, lo que podría requerir ajustes de configuración para el reconocimiento correcto de la ruta de la biblioteca.
---

## Visión general

Aspose.PDF for Python via .NET, API de procesamiento de PDF que permite a los desarrolladores trabajar con documentos PDF sin necesitar Microsoft Office® o Adobe Acrobat Automation. Aspose.PDF for Python puede usarse para desarrollar aplicaciones Python de 32 bits y 64 bits para diferentes sistemas operativos (como Windows y Linux) donde Python 3.5 o posterior está instalado.

## Sistema operativo compatible

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Servidor Windows 2012 R2
- Servidor Windows 2016
- Servidor Windows 2019
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

## Requisitos del sistema para Linux de destino

- Bibliotecas de tiempo de ejecución GCC-6 (o posteriores).

- Dependencias del tiempo de ejecución de .NET Core. Instalar el propio tiempo de ejecución de .NET Core NO es necesario.

- Para Python 3.5-3.7: se necesita la compilación pymalloc de Python. La opción de compilación --with-pymalloc de Python está habilitada por defecto. Normalmente, la compilación pymalloc de Python se marca con el sufijo m en el nombre de archivo.

- Biblioteca compartida libpython de Python. La opción de compilación de Python --enable-shared está desactivada por defecto, algunas distribuciones de Python no incluyen la biblioteca compartida libpython. En algunas plataformas Linux, la biblioteca compartida libpython puede instalarse usando el gestor de paquetes, por ejemplo: sudo apt-get install libpython3.7. El problema común es que la biblioteca libpython se instala en una ubicación diferente a la ubicación estándar del sistema para bibliotecas compartidas. El problema puede resolverse usando las opciones de compilación de Python para establecer rutas de biblioteca alternativas al compilar Python, o resolverse creando un enlace simbólico al archivo de biblioteca libpython en la ubicación estándar del sistema para bibliotecas compartidas. Normalmente, el nombre del archivo de la biblioteca compartida libpython es libpythonX.Ym.so.1.0 para Python 3.5-3.7, o libpythonX.Y.so.1.0 para Python 3.8 o posterior (por ejemplo: libpython3.7m.so.1.0, libpython3.9.so.1.0).


