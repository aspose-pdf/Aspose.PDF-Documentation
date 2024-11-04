---
title: Dividir PDF programáticamente
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /php-java/split-document/
description: Este tema muestra cómo dividir páginas PDF en archivos PDF individuales en sus aplicaciones PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Puede dividir archivos PDF usando Aspose.PDF y obtener los resultados en línea en este enlace: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Este tema muestra cómo dividir páginas PDF con Aspose.PDF para PHP a través de Java en archivos PDF individuales en sus aplicaciones PHP. Para dividir páginas PDF en archivos PDF de una sola página usando PHP, se pueden seguir los siguientes pasos:

1. Recorra las páginas del documento PDF a través de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Para cada iteración, crea un nuevo objeto Document y agrega el objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individual en el documento vacío.
1. Guarda el nuevo PDF usando el método Save.

El siguiente fragmento de código PHP te muestra cómo dividir páginas de PDF en archivos PDF individuales.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Recorrer todas las páginas
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```