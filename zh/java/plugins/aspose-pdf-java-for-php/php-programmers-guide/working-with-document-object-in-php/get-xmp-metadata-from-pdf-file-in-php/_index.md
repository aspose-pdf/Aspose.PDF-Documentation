---
title: 在 PHP 中从 PDF 文件获取 XMP 元数据
linktitle: 在 PHP 中从 PDF 文件获取 XMP 元数据
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 从 PHP 中的 PDF 文档中提取 XMP 元数据以进行高级内容分析。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取 XMP 元数据

要使用 **Aspose.PDF Java for PHP** 从 Pdf 文档获取 XMP 元数据，只需调用 **GetXMPMetadata** 类。

PHP代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**下载运行代码**

从以下任何一个社交编码网站下载**获取 XMP 元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
