---
title: 在 PHP 中将 PDF 转换为 Excel 工作簿
linktitle: 在 PHP 中将 PDF 转换为 Excel 工作簿
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
description: 了解如何使用 Aspose.PDF 将 PDF 文件转换为 PHP 中的 Excel 工作簿，从而实现无缝数据提取和操作。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 PDF 转换为 Excel 工作簿

要使用 **Aspose.PDF Java for PHP** 将 PDF 文档转换为 Excel 工作簿，只需调用 **PdfToExcel** 模块即可。

PHP代码

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

从以下任何社交编码网站下载**将 PDF 转换为 Excel 工作簿 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
