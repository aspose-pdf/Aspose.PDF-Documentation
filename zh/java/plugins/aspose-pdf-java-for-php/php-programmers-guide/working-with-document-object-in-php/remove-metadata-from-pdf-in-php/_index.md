---
title: 在 PHP 中移除 PDF 元数据
linktitle: 在 PHP 中移除 PDF 元数据
type: docs
weight: 70
url: /zh/java/remove-metadata-from-pdf-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 移除 PDF 文档的元数据，以提升隐私和文档安全性。
lastmod: "2026-10-06"
---
## Aspose.PDF - 移除元数据

要在 PDF 文档中使用 **Aspose.PDF Java for PHP** 移除元数据，只需调用 **RemoveMetadata** 类。

PHP 代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```

**下载运行代码**

下载В **Remove Metadata (Aspose.PDF)**В fromВ 以下任意提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
