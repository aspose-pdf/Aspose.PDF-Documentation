---
title: 在 PHP 中设置 PDF 过期时间
linktitle: 在 PHP 中设置 PDF 过期时间
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
description: 了解如何在 PHP 中设置 PDF 文件的到期日期，并使用 Aspose.PDF 控制访问。
lastmod: "2026-06-09"
---
## Aspose.PDF - 设置 PDF 过期时间

要使用 **Aspose.PDF Java for PHP** 设置 Pdf 文档的过期时间，只需调用 **SetExpiration** 类即可。

PHP代码

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

从以下任何一个社交编码网站下载**设置 PDF 过期时间 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
