---
title: Concatenate PDF Files in PHP
type: docs
weight: 10
url: es/java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Concatenar Archivos PDF

Para concatenar archivos PDF usando **Aspose.PDF Java para PHP**, simplemente invoca la clase **ConcatenatePdfFiles**.

Código PHP

```php

# Abre el documento de destino
$pdf1 = new Document($dataDir . 'input1.pdf');

# Abre el documento de origen
$pdf2 = new Document($dataDir . 'input2.pdf');

# Agrega las páginas del documento de origen al documento de destino
$pdf1->getPages()->add($pdf2->getPages());

# Guarda el archivo de salida concatenado (el documento de destino)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "El nuevo documento ha sido guardado, por favor revisa el archivo de salida" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descarga **Concatenar Archivos PDF (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)