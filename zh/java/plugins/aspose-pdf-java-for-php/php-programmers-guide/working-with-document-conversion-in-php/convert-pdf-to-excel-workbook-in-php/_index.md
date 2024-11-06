---
title: 将PDF转换为Excel工作簿在PHP中
type: docs
weight: 20
url: zh/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将PDF转换为Excel工作簿

要使用**Aspose.PDF Java for PHP**将PDF文档转换为Excel工作簿，只需调用**PdfToExcel**模块。

PHP代码

```php
# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 实例化Excel保存选项对象
$excelsave = new ExcelSaveOptions();

# 将输出保存为XLS格式
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "文档已成功转换" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载**将PDF转换为Excel工作簿 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)