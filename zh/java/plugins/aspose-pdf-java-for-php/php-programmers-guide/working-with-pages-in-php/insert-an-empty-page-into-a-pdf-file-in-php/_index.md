---
title: 在 PHP 中向 PDF 文件插入空页
linktitle: 在 PHP 中向 PDF 文件插入空页
type: docs
weight: 70
url: /zh/java/insert-an-empty-page-into-a-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中在 PDF 文件的任意位置插入空页，以实现灵活的文档结构。
lastmod: "2026-10-06"
---
## Aspose.PDF - 插入空页

要在 PDF 文档中插入空页，可使用 **Aspose.PDF Java for PHP**，只需调用 **InsertEmptyPage** 类。

PHP 代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```

**下载运行代码**

下载\u0412\u00A0**插入空页面 (Aspose.PDF)**\u0412\u00A0 来自\u0412\u00A0 以下列出的任何社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
