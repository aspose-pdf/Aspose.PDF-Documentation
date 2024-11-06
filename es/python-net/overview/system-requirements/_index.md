---
title: Requisitos del Sistema
linktitle: Requisitos del Sistema
type: docs
weight: 30
url: es/python-net/system-requirements/
description: Esta sección lista los sistemas operativos compatibles que un desarrollador necesita para trabajar exitosamente con Aspose.PDF para Python.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Descripción General

Aspose.PDF para Python a través de .NET, API de procesamiento de PDF que permite a los desarrolladores trabajar con documentos PDF sin necesidad de Microsoft Office® o Adobe Acrobat Automation. Aspose.PDF para Python puede ser utilizado para desarrollar aplicaciones Python de 32 bits y 64 bits para diferentes sistemas operativos (como Windows y Linux) donde Python 3.5 o posterior está instalado.

## Sistema Operativo Compatible

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

## Requisitos del Sistema para Linux Objetivo

- Bibliotecas de tiempo de ejecución de GCC-6 (o posteriores).

- Dependencias del entorno de ejecución de .NET Core. NO es necesario instalar el entorno de ejecución de .NET Core en sí.

- Para Python 3.5-3.7: Se necesita la compilación pymalloc de Python. La opción de compilación --with-pymalloc de Python está habilitada por defecto. Normalmente, la compilación pymalloc de Python está marcada con el sufijo m en el nombre del archivo.

- Biblioteca compartida de Python libpython.
 La opción de compilación de Python --enable-shared está desactivada por defecto, algunas distribuciones de Python no contienen la biblioteca compartida libpython. Para algunas plataformas Linux, la biblioteca compartida libpython se puede instalar utilizando el gestor de paquetes, por ejemplo: sudo apt-get install libpython3.7. El problema común es que la biblioteca libpython está instalada en una ubicación diferente a la ubicación estándar del sistema para bibliotecas compartidas. El problema se puede solucionar utilizando las opciones de compilación de Python para establecer rutas de bibliotecas alternativas al compilar Python, o solucionarlo creando un enlace simbólico al archivo de la biblioteca libpython en la ubicación estándar del sistema para bibliotecas compartidas. Típicamente, el nombre del archivo de la biblioteca compartida libpython es libpythonX.Ym.so.1.0 para Python 3.5-3.7, o libpythonX.Y.so.1.0 para Python 3.8 o posterior (por ejemplo: libpython3.7m.so.1.0, libpython3.9.so.1.0).