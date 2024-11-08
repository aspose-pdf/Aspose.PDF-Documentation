---
title: Converter PDF para Workbook Excel em PHP
type: docs
weight: 20
url: /pt/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Converter PDF para Workbook Excel

Para converter documento PDF para Workbook Excel usando **Aspose.PDF Java for PHP**, simplesmente invoque o módulo **PdfToExcel**.

Código PHP

```php
# Abra o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# Instanciar objeto ExcelSave Option
$excelsave = new ExcelSaveOptions();

# Salvar a saída no formato XLS
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Documento foi convertido com sucesso" . PHP_EOL;

```

**Baixar Código em Execução**

Baixar **Converter PDF para Workbook Excel (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)