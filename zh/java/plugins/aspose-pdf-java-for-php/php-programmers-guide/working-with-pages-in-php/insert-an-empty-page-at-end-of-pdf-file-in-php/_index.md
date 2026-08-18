---
title: 在 PHP 中的 PDF 文件末尾插入空白页
linktitle: 在 PHP 中的 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中的 PDF 文档末尾插入空白页面以进行文档扩展。
lastmod: "2026-06-09"
---
## Aspose.PDF - 在 PDF 文件末尾插入空白页

要使用 **Aspose.PDF Java for PHP** 在 PDF 文档末尾插入空页，只需调用 **InsertEmptyPageAtEndOfFile** 类即可。

PHP代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## 下载运行代码

从以下任何社交编码网站下载 **在 PDF 文件末尾插入空页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
