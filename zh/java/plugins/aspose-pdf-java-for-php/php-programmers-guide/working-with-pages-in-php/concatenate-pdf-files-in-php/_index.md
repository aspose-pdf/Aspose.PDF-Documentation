---
title: 在 PHP 中连接 PDF 文件
linktitle: 在 PHP 中连接 PDF 文件
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
description: 了解如何使用 Aspose.PDF 将多个 PDF 文件连接到 PHP 中的单个文档中，以更轻松地进行文档管理。
lastmod: "2026-06-09"
---
## Aspose.PDF - 连接 PDF 文件

要使用 **Aspose.PDF Java for PHP** 连接 PDF 文件，只需调用 **ConcatenatePdfFiles** 类。

PHP代码

```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```

**下载运行代码**

从以下任何社交编码网站下载**连接 PDF 文件 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
