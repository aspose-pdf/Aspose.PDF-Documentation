---
title: 在 PHP 中为 Web 优化 PDF 文档
linktitle: 在 PHP 中为 Web 优化 PDF 文档
type: docs
weight: 60
url: /zh/java/optimize-pdf-document-for-the-web-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中优化 PDF 文档，以实现更快的网页性能和更小的文件体积。
lastmod: "2026-10-06"
---
## Aspose.PDF - 为 Web 优化 PDF

要使用 **Aspose.PDF Java for PHP** 对 Web 进行 PDF 文档优化，只需调用 **optimize_web** 方法的 В  **Optimize** 类。

PHP 代码

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**下载运行代码**

下载В **为 Web 优化 PDF (Aspose.PDF)**В 来自В 以下任意一个提及的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
