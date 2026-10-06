---
title: Converter arquivo SVG para formato PDF em PHP
linktitle: Converter arquivo SVG para formato PDF em PHP
type: docs
weight: 40
url: /pt/java/convert-svg-file-to-pdf-format-in-php/
description: Explore como converter arquivos SVG para formato PDF em PHP usando Aspose.PDF para uma gestão eficaz de documentos.
lastmod: "2026-10-06"
---
## Aspose.PDF - Converter SVG para PDF

Para converter um arquivo SVG para formato PDF usando **Aspose.PDF Java for PHP**, basta invocar o módulo **SvgToPdf**.

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

**Baixar Código em Execução**

BaixarВ **Converter SVG para PDF (Aspose.PDF)**В deВ qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
