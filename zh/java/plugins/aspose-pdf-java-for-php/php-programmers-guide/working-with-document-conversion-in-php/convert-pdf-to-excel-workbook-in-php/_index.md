---
title: 在 PHP 中将 PDF 转换为 Excel 工作簿
linktitle: 在 PHP 中将 PDF 转换为 Excel 工作簿
type: docs
weight: 20
url: /zh/java/convert-pdf-to-excel-workbook-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 将 PDF 文件转换为 Excel 工作簿，实现无缝的数据提取和操作。
lastmod: "2026-10-06"
---
## Aspose.PDF - 将 PDF 转换为 Excel 工作簿

要使用 **Aspose.PDF Java for PHP** 将 PDF 文档转换为 Excel 工作簿，只需调用 **PdfToExcel** 模块。

PHP 代码

```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```

**下载运行代码**

下载В **将 PDF 转换为 Excel 工作簿 (Aspose.PDF)**В 来自В 以下任意提到的社交代码托管网站：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
