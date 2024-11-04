---
title: Agregar Número de Página a PDF 
linktitle: Agregar Número de Página
type: docs
weight: 100
url: /php-java/add-page-number/
description: Aspose.PDF para PHP a través de Java te permite agregar un Sello de Número de Página a tu archivo PDF usando la clase PageNumber Stamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Todos los documentos deben tener números de página. El número de página facilita al lector localizar diferentes partes del documento.
**Aspose.PDF para PHP a través de Java** te permite agregar números de página con PageNumberStamp.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Puedes usar la clase [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) para agregar un sello de número de página en un documento PDF.
 El [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) clase proporciona métodos para crear un sello basado en el número de página como formato, márgenes, alineaciones, número inicial, etc. Para añadir un sello de número de página, necesitas crear un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y un objeto [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) con las propiedades de texto requeridas. Después de eso, puedes llamar al método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para añadir el sello en el archivo PDF. También puedes configurar los atributos de fuente del sello de número de página.

El siguiente fragmento de código te muestra cómo añadir números de página en un archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Crear sello de número de página
    $pageNumberStamp = new PageNumberStamp();

    // Si el sello es de fondo
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Página # de " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // Configurar propiedades de texto
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // Añadir sello a una página en particular
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```