---
title: 在 PHP 中将 SVG 文件转换为 PDF 格式
linktitle: 在 PHP 中将 SVG 文件转换为 PDF 格式
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: 探索如何在 PHP 中使用 Aspose.PDF 将 SVG 文件转换为 PDF 格式，以实现有效的文档管理。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 SVG 转换为 PDF

要使用 **Aspose.PDF Java for PHP** 将 SVG 文件转换为 PDF 格式，只需调用 **SvgToPdf** 模块即可。

PHP代码

```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```

**下载运行代码**

从以下任何社交编码网站下载**将 SVG 转换为 PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
