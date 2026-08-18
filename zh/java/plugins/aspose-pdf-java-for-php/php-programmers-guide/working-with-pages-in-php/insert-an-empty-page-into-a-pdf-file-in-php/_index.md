---
title: 在 PHP 中将空页面插入 PDF 文件
linktitle: 在 PHP 中将空页面插入 PDF 文件
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中的 PDF 文件中的任意位置插入空白页面，以实现灵活的文档结构。
lastmod: "2026-06-09"
---
## Aspose.PDF - 插入空白页

要使用 **Aspose.PDF Java for PHP** 将空页面插入到 Pdf 文档中，只需调用 **InsertEmptyPage** 类即可。

PHP代码

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

从以下任何一个社交编码网站下载**插入空页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
