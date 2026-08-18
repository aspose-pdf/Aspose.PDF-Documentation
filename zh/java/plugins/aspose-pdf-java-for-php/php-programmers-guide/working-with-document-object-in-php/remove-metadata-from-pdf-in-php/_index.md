---
title: 在 PHP 中从 PDF 中删除元数据
linktitle: 在 PHP 中从 PDF 中删除元数据
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
description: 探索如何使用 Aspose.PDF 从 PHP 中的 PDF 文档中删除元数据，以提高隐私性和文档安全性。
lastmod: "2026-06-09"
---
## Aspose.PDF - 删除元数据

要使用 **Aspose.PDF Java for PHP** 从 Pdf 文档中删除元数据，只需调用 **RemoveMetadata** 类即可。

PHP代码

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

从以下任何社交编码网站下载**删除元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
