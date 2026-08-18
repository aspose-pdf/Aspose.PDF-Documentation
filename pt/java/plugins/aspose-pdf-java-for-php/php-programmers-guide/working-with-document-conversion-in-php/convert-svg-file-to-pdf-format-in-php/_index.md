---
title: Converta arquivo SVG para formato PDF em PHP
linktitle: Converta arquivo SVG para formato PDF em PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: Explore como converter arquivos SVG para o formato PDF em PHP usando Aspose.PDF para um gerenciamento eficaz de documentos.
lastmod: "2026-06-09"
---
## Aspose.PDF - Converter SVG para PDF

Para converter o arquivo SVG para o formato PDF usando **Aspose.PDF Java para PHP**, basta invocar o módulo **SvgToPdf**.

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

**Baixar código em execução**

Baixe **Converter SVG em PDF (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
