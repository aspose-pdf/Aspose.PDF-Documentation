---
title: 设置 PDF 到期时间在 PHP 中
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 设置 PDF 到期时间

要使用 **Aspose.PDF Java for PHP** 设置 PDF 文档的到期时间，只需调用 **SetExpiration** 类。

PHP 代码

```php

# 打开一个 PDF 文档。
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('文件已过期。您需要一个新的。');");
$doc->setOpenAction($javascript);

# 保存更新的文档带有新信息
$doc->save($dataDir . "set_expiration.pdf");

print "更新文档信息，请检查输出文件。" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载 **Set PDF Expiration (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)