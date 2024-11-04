---
title: Hello World PHP via Java Ejemplo
linktitle: Hello World Ejemplo
type: docs
weight: 40
url: /php-java/hello-world-example/
description: Esta página muestra cómo usar programación simple para crear un documento PDF que contiene el texto - Hello World usando Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World Ejemplo

Un ejemplo de “Hello World” se utiliza típicamente para demostrar las características básicas de un lenguaje de programación o software con un caso de uso sencillo.

Aspose.PDF para PHP via Java API permite a los desarrolladores crear, leer, editar y manipular archivos PDF dentro de sus aplicaciones Java. Soporta la lectura y conversión de varios tipos de archivos hacia y desde el formato PDF. Este artículo de Hello World muestra cómo crear un archivo PDF usando Aspose.PDF para PHP via Java API. Después de [instalar Aspose.PDF para PHP via Java](/pdf/php-java/installation/) en su entorno, puede ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código sigue estos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) al objeto documento
1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Añadir TextFragment a la colección [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la página
1. Guardar el documento PDF resultante

El siguiente fragmento de código es un programa Hola Mundo para exhibir el funcionamiento de Aspose.PDF para PHP a través de la API de Java.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```