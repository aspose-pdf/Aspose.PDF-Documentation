---
title: 在 PHP 中获取 PDF 页数
linktitle: 在 PHP 中获取 PDF 页数
type: docs
weight: 40
url: /zh/java/get-page-count-of-pdf-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 进行文档分析，以检索 PDF 文档的总页数。
lastmod: "2026-10-06"
---
## Aspose.PDF - 获取页数

要使用 **Aspose.PDF Java for PHP** 获取 PDF 文档的页数，只需调用 **GetNumberOfPages** 类。

PHP 代码

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**下载运行代码**

下载В **获取页面计数 (Aspose.PDF)**В 来自В 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
