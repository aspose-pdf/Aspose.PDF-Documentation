---
title: Convertir archivos SVG a formato PDF en PHP
linktitle: Convertir archivos SVG a formato PDF en PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: Explore cómo convertir archivos SVG a formato PDF en PHP usando Aspose.PDF para una gestión de documentos eficaz.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Convertir SVG a PDF



Para convertir un archivo SVG a formato PDF usando **Aspose.PDF Java para PHP**, simplemente invoque el módulo **SvgToPdf**.

Código PHP


```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```


**Descargar código de ejecución**



Descargue **Convierta SVG a PDF (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
