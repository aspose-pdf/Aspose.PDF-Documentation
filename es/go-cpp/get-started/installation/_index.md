---
title: Cómo instalar Aspose.PDF para Go via C++
linktitle: Instalación
type: docs
weight: 20
url: /es/go-cpp/installation/
description: Esta sección muestra una descripción del producto e instrucciones para instalar Aspose.PDF for Go por su cuenta.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía de instalación de Aspose.PDF for Go
Abstract: La guía de instalación de Aspose.PDF for Go via C++ proporciona instrucciones paso a paso para instalar y configurar la biblioteca para su uso en proyectos Go con integración C++. Cubre varios métodos de instalación, incluyendo la configuración manual y el uso de gestores de paquetes como NuGet. La guía también describe los requisitos del sistema, dependencias y los pasos de configuración necesarios para garantizar una integración sin problemas en los entornos de desarrollo. Esta documentación ayuda a los desarrolladores a iniciar la creación, lectura y manipulación de documentos PDF en Go vía C++ de manera efectiva.
SoftwareApplication: go-cpp
---

## Instalación

Este paquete incluye un archivo grande que está almacenado como un archivo bzip2.

1. Agrega el paquete asposepdf a tu proyecto:

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. Generar el archivo grande:

- **macOS y linux**

1. Abrir Terminal

2. Enumere las carpetas de github.com/aspose-pdf dentro de la caché de módulos de Go:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. Cambie la carpeta curent a la carpeta de la versión específica del paquete obtenida en el paso anterior:

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

Reemplaza `@vx.x.x` con la versión real del paquete.

4. Ejecute go generate con privilegios de superusuario:

```sh
sudo go generate
```

- **Windows**

1. Abrir el símbolo del sistema

2. Enumere las carpetas de github.com/aspose-pdf dentro de la caché de módulos de Go:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. Cambie la carpeta curent a la carpeta de la versión específica del paquete obtenida en el paso anterior:

```cmd
cd <specific version folder of the package>
```

4. Ejecuta go generate:

```cmd
go generate
```

5. Agrega la carpeta de versión específica del paquete a la variable de entorno %PATH%:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

Reemplazar `<specific version folder of the package>` con la ruta real obtenida del paso 2.

## Prueba

La ejecución de la prueba desde la carpeta raíz del paquete:

```sh
go test -v
```

## Inicio rápido

Todos los fragmentos de código están contenidos en el [fragmento](https://github.com/aspose-pdf/aspose-pdf-go-cpp).