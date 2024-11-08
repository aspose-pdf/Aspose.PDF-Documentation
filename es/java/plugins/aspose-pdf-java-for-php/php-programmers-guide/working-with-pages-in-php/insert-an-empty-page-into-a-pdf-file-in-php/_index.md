---
title: Insertar una Página Vacía en un Archivo PDF en PHP
type: docs
weight: 70
url: /es/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Insertar una Página Vacía

Para insertar una página vacía en un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoca la clase **InsertEmptyPage**.

Código PHP

```php

# Abre el documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# inserta una página vacía en un PDF
$pdf->getPages()->insert(1);

# Guarda el archivo de salida concatenado (el documento de destino)
$pdf->save($dataDir . "output.pdf");

print "¡Página vacía añadida con éxito!";

```

**Descargar Código Ejecutable**

Descarga **Insertar una Página Vacía (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)