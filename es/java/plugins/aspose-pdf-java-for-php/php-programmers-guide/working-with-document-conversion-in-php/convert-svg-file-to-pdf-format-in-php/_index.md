---
title: Convertir archivo SVG a formato PDF en PHP
linktitle: Convertir archivo SVG a formato PDF en PHP
type: docs
weight: 40
url: /es/java/convert-svg-file-to-pdf-format-in-php/
description: Explore cómo convertir archivos SVG a formato PDF en PHP usando Aspose.PDF para una gestión de documentos eficaz.
lastmod: "2026-09-03"
---
## Aspose.PDF - Convertir SVG a PDF

Para convertir un archivo SVG a formato PDF usando **Aspose.PDF Java for PHP**, simplemente invoque el módulo **SvgToPdf**.

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

**Descargar código en ejecución**

DescargarВ **Convert SVG to PDF (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
