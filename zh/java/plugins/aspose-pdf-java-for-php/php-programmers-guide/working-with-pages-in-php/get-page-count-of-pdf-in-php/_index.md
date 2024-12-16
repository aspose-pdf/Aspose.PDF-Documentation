---
title: 获取 PDF 页数在 PHP 中
type: docs
weight: 40
url: /zh/java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取页数

要使用 **Aspose.PDF Java for PHP** 获取 PDF 文档的页数，只需调用 **GetNumberOfPages** 类。

PHP 代码

```php

# 创建 PDF 文档

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "页数:" . $page_count . PHP_EOL;

```

**下载运行代码**

从以下任一社会编码网站下载 **获取页数 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)