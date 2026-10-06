---
title: Converter PDF para pasta de trabalho Excel em PHP
linktitle: Converter PDF para pasta de trabalho Excel em PHP
type: docs
weight: 20
url: /pt/java/convert-pdf-to-excel-workbook-in-php/
description: Aprenda como converter arquivos PDF em pastas de trabalho Excel em PHP usando Aspose.PDF, permitindo extração e manipulação de dados sem interrupções.
lastmod: "2026-10-06"
---
## Aspose.PDF - converter PDF para pasta de trabalho Excel

Para converter um documento PDF em Pasta de Trabalho Excel usando **Aspose.PDF Java for PHP**, basta chamar o módulo **PdfToExcel**.

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

**Baixar Código em Execução**

Baixar **Converter PDF para Pasta de Trabalho Excel (Aspose.PDF)** de qualquer um dos sites de codificação social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
