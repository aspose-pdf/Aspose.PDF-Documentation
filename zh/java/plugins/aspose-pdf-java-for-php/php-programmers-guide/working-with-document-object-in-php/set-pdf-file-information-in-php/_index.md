---
title: 在 PHP 中设置 PDF 文件信息
linktitle: 在 PHP 中设置 PDF 文件信息
type: docs
weight: 90
url: /zh/java/set-pdf-file-information-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中为 PDF 文档设置各种文件属性，如元数据。
lastmod: "2026-10-06"
---
## Aspose.PDF - 设置 PDF 文件信息

要使用 **Aspose.PDF Java for PHP** 更新 PDF 文档信息，只需调用 **SetPdfFileInfo** 类。

PHP 代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```

**下载运行代码**

下载В **Set PDF File Information (Aspose.PDF)**В 来自В 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
