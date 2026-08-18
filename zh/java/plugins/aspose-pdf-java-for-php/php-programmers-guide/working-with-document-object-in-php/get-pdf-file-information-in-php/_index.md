---
title: 在 PHP 中获取 PDF 文件信息
linktitle: 在 PHP 中获取 PDF 文件信息
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 检索有关 PDF 文件的详细信息，包括元数据和属性。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取 PDF 文件信息

要使用 **Aspose.PDF Java for PHP** 获取 Pdf 文档的文件信息，只需调用 **GetPdfFileInfo** 类即可。

PHP代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```

**下载运行代码**

从以下任何一个社交编码网站下载**获取 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
