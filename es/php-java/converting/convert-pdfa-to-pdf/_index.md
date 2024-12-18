---
title: Convertir PDF/A a formato PDF 
linktitle: Convertir PDF/A a formato PDF
type: docs
weight: 110
url: /es/php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: Este tema le muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF con la biblioteca PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir documento PDF/A a PDF

Convertir un documento PDF/A a PDF significa eliminar la restricción de <abbr title="Archivo de Formato de Documento Portátil">PDF/A</abbr> del documento original. La clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tiene el método removePdfaCompliance(..) para eliminar la información de conformidad PDF del archivo de entrada/origen.

```php
// Crear una nueva instancia de la clase Document con el archivo de entrada
$document = new Document($inputFile);

// Eliminar la conformidad PDF/A del documento
$document->removePdfaCompliance();

// Guardar el documento modificado en el archivo de salida
$document->save($outputFile);
```

Esta información también se elimina si realiza cualquier cambio en el documento (por ejemplo,
 agregar páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad con PDF/A después de agregar la página.

```php
// Crear una nueva instancia de la clase Document con el archivo de entrada
$document = new Document($inputFile);

// Eliminar la conformidad con PDF/A del documento
$document->getPages()->add();

// Guardar el documento modificado en el archivo de salida
$document->save($outputFile);
```