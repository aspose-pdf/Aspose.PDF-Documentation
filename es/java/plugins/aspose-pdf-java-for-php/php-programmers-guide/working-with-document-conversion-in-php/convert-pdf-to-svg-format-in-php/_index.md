---
title: Convertir PDF a Formato SVG en PHP
type: docs
weight: 30
url: /es/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Convertir PDF a SVG

Para convertir PDF a formato SVG usando **Aspose.PDF Java for PHP**, simplemente invoque el módulo **PdfToSvg**.

Código PHP

```php

# Abrir el documento objetivo
$pdf = new Document($dataDir . 'input1.pdf');

# instanciar un objeto de SvgSaveOptions
$save_options = new SvgSaveOptions();

# no comprimir la imagen SVG en un archivo Zip
$save_options->CompressOutputToZipArchive = false;

# Guardar la salida en formato XLS
$pdf->save($dataDir . "Output.svg", $save_options);

print "El documento ha sido convertido exitosamente" . PHP_EOL;

```

**Descargar Código en Ejecución**

Descargue **Convertir PDF a Formato SVG (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)