---
title: 在 PHP 中将 PDF 转换为 SVG 格式
linktitle: 在 PHP 中将 PDF 转换为 SVG 格式
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 将 PDF 文档转换为 SVG 格式，以实现高质量矢量图形转换。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 PDF 转换为 SVG

要使用 **Aspose.PDF Java for PHP** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块即可。

PHP代码

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

**下载运行代码**

从以下任何社交编码网站下载**将 PDF 转换为 SVG 格式 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
