---
title: Añadir Texto al Archivo PDF 
linktitle: Añadir Texto al Archivo PDF
type: docs
weight: 10
url: /php-java/add-text-to-pdf-file/
description: Este artículo describe varios aspectos del trabajo con texto en Aspose.PDF. Aprende cómo añadir texto a PDF, añadir fragmentos HTML, o usar fuentes OTF personalizadas.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para añadir texto a un archivo PDF existente:

1. Abre el PDF de entrada usando el objeto Document.
1. Obtén la página particular a la que quieres añadir el texto.
1. Crea un fragmento de texto con el contenido "Aspose.PDF".
1. Establece la posición del fragmento de texto en la página.
1. Establece las propiedades del texto del fragmento de texto.
1. Crea un objeto TextBuilder para la página.
1. Anexa el fragmento de texto a la página PDF.
4. Guarda el documento PDF resultante en el archivo de salida.

## Añadiendo Texto

El siguiente fragmento de código te muestra cómo añadir texto en un archivo PDF existente.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // obtener página particular
    $page = $document->getPages()->add();
    
    // crear fragmento de texto
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // establecer propiedades del texto
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // crear objeto TextBuilder
    $textBuilder = new TextBuilder($page);
    // anexa el fragmento de texto a la página PDF
    $textBuilder->appendText($textFragment);

    // Guardar documento PDF resultante.    
    $document->save($outputFile);
    $document->close();
```