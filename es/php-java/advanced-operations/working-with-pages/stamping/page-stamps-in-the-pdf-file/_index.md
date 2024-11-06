---
title: Añadir Sello de Página a PDF
linktitle: Sellos de página en archivo PDF
type: docs
weight: 30
url: es/php-java/page-stamps-in-the-pdf-file/
description: Añadir un sello de página a un archivo PDF usando la clase PdfPageStamp con PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir Sello de Página 

Un [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) se puede usar cuando necesitas aplicar un sello compuesto que contenga gráficos, texto, tablas. El siguiente ejemplo muestra cómo usar un sello para crear papelería como en el uso de Adobe InDesign, Illustrator, Microsoft Word. Supongamos que tenemos algún documento de entrada y queremos aplicar 2 tipos de bordes con color azul y ciruela.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();  
```