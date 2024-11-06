---
title: Insertar una Página Vacía al Final del Archivo PDF en PHP
type: docs
weight: 60
url: es/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insertar una Página Vacía al Final del Archivo PDF

Para insertar una página vacía al final del documento PDF usando **Aspose.PDF Java for PHP**, simplemente invoque la clase **InsertEmptyPageAtEndOfFile**.

Código PHP

```php

# Abrir el documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# insertar una página vacía en un PDF
$pdf->getPages()->add();

# Guardar el archivo de salida concatenado (el documento de destino)
$pdf->save($dataDir . "output.pdf");

print "¡Página vacía añadida con éxito!" . PHP_EOL;

```

## Descargar Código en Ejecución

Descargar **Insertar una Página Vacía al Final del Archivo PDF (Aspose.PDF)** desde cualquiera de los siguientes sitios de codificación social:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)