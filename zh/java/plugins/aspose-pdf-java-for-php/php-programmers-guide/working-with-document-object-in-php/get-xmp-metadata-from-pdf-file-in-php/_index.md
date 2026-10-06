---
title: 在 PHP 中获取 PDF 文件的 XMP 元数据
linktitle: 在 PHP 中获取 PDF 文件的 XMP 元数据
type: docs
weight: 50
url: /zh/java/get-xmp-metadata-from-pdf-file-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 提取 PDF 文档的 XMP 元数据，以进行高级内容分析。
lastmod: "2026-10-06"
---
## Aspose.PDF - 获取 XMP 元数据

要使用 **Aspose.PDF Java for PHP** 从 Pdf 文档获取 XMP 元数据，只需调用 **GetXMPMetadata** 类。

PHP 代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**下载 运行 代码**

DownloadВ **获取 XMP 元数据 (Aspose.PDF)**В 从В 以下提到的社交代码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
