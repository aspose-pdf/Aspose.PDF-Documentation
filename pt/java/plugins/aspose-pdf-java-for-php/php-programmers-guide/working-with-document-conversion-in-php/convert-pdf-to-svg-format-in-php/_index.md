---
title: Converter PDF para formato SVG em PHP
linktitle: Converter PDF para formato SVG em PHP
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: Descubra como converter documentos PDF para o formato SVG em PHP com Aspose.PDF para transformação de gráficos vetoriais de alta qualidade.
lastmod: "2026-06-09"
---
## Aspose.PDF - Converter PDF em SVG

Para converter PDF para o formato SVG usando **Aspose.PDF Java para PHP**, basta invocar o módulo **PdfToSvg**.

Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```

**Baixar código em execução**

Baixe **Converter PDF para formato SVG (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
