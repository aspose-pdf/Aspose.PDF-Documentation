---
title: 获取 PDF 文件信息在 PHP 中
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取 PDF 文件信息

要使用 **Aspose.PDF Java for PHP** 获取 Pdf 文档的信息，只需调用 **GetPdfFileInfo** 类。

PHP 代码

```php

# 打开一个 pdf 文档。
$doc = new Document($dataDir . "input1.pdf");

# 获取文档信息
$doc_info = $doc->getInfo();

# 显示文档信息
print "作者:-" . $doc_info->getAuthor();
print "创建日期:-" . $doc_info->getCreationDate();
print "关键词:-" . $doc_info->getKeywords();
print "修改日期:-" . $doc_info->getModDate();
print "主题:-" . $doc_info->getSubject();
print "标题:-" . $doc_info->getTitle();

```

**下载运行代码**

从以下任一社交编码网站下载 **获取 PDF 文件信息 (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)