---
title: 在 PHP 中获取 PDF 的页数
linktitle: 在 PHP 中获取 PDF 的页数
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中检索 PDF 文档的总页数进行文档分析。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取页数

要使用 **Aspose.PDF Java for PHP** 获取 Pdf 文档的页数，只需调用 **GetNumberOfPages** 类即可。

PHP代码

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**下载运行代码**

从以下任何一个社交编码网站下载**获取页数 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
