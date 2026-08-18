---
title: 使用 PHP 优化 Web PDF 文档
linktitle: 使用 PHP 优化 Web PDF 文档
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中优化 PDF 文档，以提高 Web 性能并减小文件大小。
lastmod: "2026-06-09"
---
## Aspose.PDF - 优化 Web PDF

要使用 **Aspose.PDF Java for PHP** 优化 Web PDF 文档，只需调用 **Optimize** 类的 **optimize_web** 方法即可。

PHP代码

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

从以下任何一个社交编码网站下载**优化 Web PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
