---
title: Obtener una Página Particular en un Archivo PDF en PHP
type: docs
weight: 30
url: es/java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtener Página

Para obtener una Página Particular en un documento PDF usando **Aspose.PDF Java para Ruby**, simplemente invoca la clase **GetPage**.

Código Ruby

```php

# Abrir el documento objetivo
$pdf = new Document($dataDir . 'input1.pdf');

# obtener la página en un índice particular de la Colección de Páginas
$pdf_page = $pdf->getPages()->get_Item(1);

# crear un nuevo objeto Document
$new_document = new Document();

# añadir página a la colección de páginas del nuevo objeto documento
$new_document->getPages()->add($pdf_page);

# guardar el archivo PDF recién generado
$new_document->save($dataDir . "output.pdf");

print "¡Proceso completado con éxito!";

```

## Descargar Código en Ejecución

Descargar **Obtener Página (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)