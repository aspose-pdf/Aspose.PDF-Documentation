---
title: Converter PDF em pasta de trabalho do Excel em PHP
linktitle: Converter PDF em pasta de trabalho do Excel em PHP
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
description: Aprenda como converter arquivos PDF em pastas de trabalho do Excel em PHP usando Aspose.PDF, permitindo extração e manipulação de dados perfeitas.
lastmod: "2026-06-09"
---
## Aspose.PDF - Converter PDF em pasta de trabalho do Excel

Para converter um documento PDF em uma pasta de trabalho do Excel usando **Aspose.PDF Java para PHP**, basta invocar o módulo **PdfToExcel**.

Código PHP

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**Baixar código em execução**

Baixe **Converter PDF para Excel Workbook (Aspose.PDF)**Â de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
