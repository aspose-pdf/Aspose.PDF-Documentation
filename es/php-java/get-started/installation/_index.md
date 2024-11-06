---
title: Instalar Aspose.PDF para PHP a través de Java
linktitle: Instalación
type: docs
weight: 20
url: es/php-java/installation/
description: Esta sección muestra una descripción del producto e instrucciones para instalar Aspose.PDF para PHP a través de Java por su cuenta, así como utilizando NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF para PHP a través de Java se compone de dos componentes separados: el envoltorio de script (aspose.pdf.php) y Aspose.PDF para Java. Estos componentes interactúan a través del puente PHP/Java, y cada uno requiere su propio entorno y proceso de ejecución.

## Instalación

1. Instale Tomcat en cualquier ubicación, como \java\apache-tomcat-9.0.24.
1. Copie JavaBridge.war en la carpeta webapps de Tomcat, como \java\apache-tomcat-9.0.24\webapps.
1. Copie aspose-pdf-xx.x.jar en la carpeta lib, como \java\apache-tomcat-9.0.24\lib.
1. Ejecute \bin\startup.bat, JavaBridge.war se desplegará en \java\apache-tomcat-9.0.24\webapps\JavaBridge.

1. Prueba http://localhost:8080/JavaBridge/test.php para asegurarte de que PHP funciona correctamente.
1. Copia aspose.pdf.php y example.php a \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Abre http://localhost:8080/JavaBridge/example.php o crea tu propio archivo PHP de la siguiente manera.
Encontrarás la biblioteca Jar y PHP en la carpeta vendor/aspose/pdf.