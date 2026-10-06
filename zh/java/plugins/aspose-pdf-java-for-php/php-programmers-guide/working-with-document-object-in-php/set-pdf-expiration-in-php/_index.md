---
title: 在 PHP 中设置 PDF 过期
linktitle: 在 PHP 中设置 PDF 过期
type: docs
weight: 80
url: /zh/java/set-pdf-expiration-in-php/
description: 了解如何在 PHP 中为 PDF 文件设置过期日期，并使用 Aspose.PDF 控制访问。
lastmod: "2026-10-06"
---
## Aspose.PDF - 设置 PDF 过期

要使用 **Aspose.PDF Java for PHP** 为 PDF 文档设置过期，简单地调用 **SetExpiration** 类。

PHP 代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```

**下载运行代码**

下载 **Set PDF Expiration (Aspose.PDF)** 来自以下任意社交代码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
