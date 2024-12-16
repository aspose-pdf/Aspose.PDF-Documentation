---
title: Convertir HTML a PDF
linktitle: Convertir HTML a PDF
type: docs
weight: 40
url: /es/php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: Este tema le muestra cómo Aspose.PDF permite convertir formatos HTML y MHTML a un archivo PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visión general

Este artículo explica cómo convertir HTML a PDF usando PHP. El código es muy simple, solo cargue HTML en la clase Document y guárdelo como PDF de salida. Convertir MHTML a PDF en Java también es similar. Cubre los siguientes temas

## Biblioteca Java para Convertir HTML a PDF

**Aspose.PDF para PHP a través de Java** es una API de manipulación de PDF que le permite convertir cualquier documento HTML existente a PDF sin problemas.
El proceso de conversión de HTML a PDF se puede personalizar de manera flexible.

## Convertir HTML a PDF

El siguiente ejemplo de código Java muestra cómo convertir un documento HTML a un PDF.

1. Cree una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).

1. Inicializar el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Guardar el documento PDF de salida llamando al método [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-).

```php
    // Crear una instancia de HtmlLoadOptions para especificar las opciones de carga para el archivo HTML
    $loadOption = new HtmlLoadOptions();

    // Crear un nuevo objeto Document y cargar el archivo HTML
    $document = new Document($inputFile, $loadOption);

    // Guardar el documento como un archivo PDF
    $document->save($outputFile);
```

## Conversión avanzada de HTML a PDF

El motor de conversión HTML tiene varias opciones que nos permiten controlar el proceso de conversión.

### Soporte de Media Queries

1. Crear un HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. [Establecer modo de impresión o pantalla](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-).

1. Inicializar [objeto Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Guardar el documento PDF de salida.

Las consultas de medios son una técnica popular para ofrecer una hoja de estilo adaptada a diferentes dispositivos. Podemos establecer el tipo de dispositivo usando la clase [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```php

    // Crear una instancia de HtmlLoadOptions para especificar las opciones de carga para el archivo HTML
    $htmlMediaType = new HtmlMediaType();

    // Establecer modo de impresión o de pantalla
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // Crear un nuevo objeto Document y cargar el archivo HTML
    $document = new Document($inputFile, $loadOption);

    // Guardar el documento como un archivo PDF
    $document->save($outputFile);
```

### Habilitar (deshabilitar) la incrustación de fuentes

1. Agregar nuevas [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) de Html.
1. Deshabilitar la incrustación de fuentes.
1. Guardar un nuevo Document.

Las páginas HTML a menudo usan fuentes (p.ej.
 fonts desde una carpeta local, Google Fonts, etc). También podemos controlar la incrustación de fuentes en un documento usando una propiedad [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-).

```php

    // Crear una instancia de HtmlLoadOptions para especificar las opciones de carga para el archivo HTML
    $loadOption = new HtmlLoadOptions();

    // Desactivar la incrustación de fuentes
    $loadOption->setEmbedFonts(true);

    // Crear un nuevo objeto Document y cargar el archivo HTML
    $document = new Document($inputFile, $loadOption);

    // Guardar el documento como un archivo PDF
    $document->save($outputFile);
```

## Convertir MHTML a PDF

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, abreviatura de MIME HTML, es un formato de archivo de página web utilizado para combinar recursos que normalmente se representan mediante enlaces externos (como imágenes, animaciones Flash, applets de Java y archivos de audio) con código HTML en un solo archivo. El contenido de un archivo MHTML está codificado como si fuera un mensaje de correo electrónico HTML, utilizando el tipo MIME multipart/related.

El siguiente fragmento de código muestra cómo convertir archivos MHTML a formato PDF con Java:

```php

    // Crear una nueva instancia de la clase MhtLoadOptions.
    $loadOption = new MhtLoadOptions();

    // Crear una nueva instancia de la clase Document y cargar el archivo MHTML.
    $document = new Document($inputFile, $loadOption);

    // Guardar el documento como un archivo PDF.
    $document->save($outputFile);
```