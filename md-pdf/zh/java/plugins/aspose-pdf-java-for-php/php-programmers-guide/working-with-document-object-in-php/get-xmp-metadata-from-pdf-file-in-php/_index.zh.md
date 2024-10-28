---
title: 从 PDF 文件中获取 XMP 元数据 (PHP)
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取 XMP 元数据

要使用 **Aspose.PDF Java for PHP** 从 PDF 文档中获取 XMP 元数据，只需调用 **GetXMPMetadata** 类。

PHP 代码

```php

# 打开一个 PDF 文档。
$doc = new Document($dataDir . "input1.pdf");

# 获取属性
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**下载运行代码**

从以下任何一个社交编码网站下载 **Get XMP Metadata (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)