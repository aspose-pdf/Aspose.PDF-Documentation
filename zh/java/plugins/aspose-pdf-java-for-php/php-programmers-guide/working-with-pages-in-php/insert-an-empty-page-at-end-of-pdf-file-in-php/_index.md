---
title: 在 PHP 中在 PDF 文件末尾插入空白页
linktitle: 在 PHP 中在 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /zh/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中在 PDF 文档末尾插入空白页以扩展文档。
lastmod: "2026-10-06"
---
## Aspose.PDF - 在 PDF 文件末尾插入空白页

要使用 **Aspose.PDF Java for PHP** 在 PDF 文档末尾插入空白页，只需调用 **InsertEmptyPageAtEndOfFile** 类。

PHP 代码

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

下载 **Insert an Empty Page at End of PDF File (Aspose.PDF)**В 从В 以下任意提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
