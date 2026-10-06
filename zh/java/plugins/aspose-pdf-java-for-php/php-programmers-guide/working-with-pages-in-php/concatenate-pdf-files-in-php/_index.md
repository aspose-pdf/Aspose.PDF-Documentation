---
title: 在 PHP 中合并 PDF 文件
linktitle: 在 PHP 中合并 PDF 文件
type: docs
weight: 10
url: /zh/java/concatenate-pdf-files-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 将多个 PDF 文件合并为单个文档，以便更轻松地进行文档管理。
lastmod: "2026-10-06"
---
## Aspose.PDF - 合并 PDF 文件

要使用 **Aspose.PDF Java for PHP** 合并 PDF 文件，只需调用 **ConcatenatePdfFiles** 类。

PHP 代码

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

下载 **Concatenate PDF Files (Aspose.PDF)** 来自以下任意提及的社交编码网站：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)
