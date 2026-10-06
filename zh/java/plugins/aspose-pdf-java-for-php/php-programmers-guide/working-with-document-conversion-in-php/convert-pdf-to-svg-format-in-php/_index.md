---
title: 在 PHP 中将 PDF 转换为 SVG 格式
linktitle: 在 PHP 中将 PDF 转换为 SVG 格式
type: docs
weight: 30
url: /zh/java/convert-pdf-to-svg-format-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中将 PDF 文档转换为 SVG 格式，以实现高质量的矢量图形转换。
lastmod: "2026-10-06"
---
## Aspose.PDF - 将 PDF 转换为 SVG

要使用 **Aspose.PDF Java for PHP** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块。

PHP 代码

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

下载 **Convert PDF to SVG Format (Aspose.PDF)** 来自以下提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
