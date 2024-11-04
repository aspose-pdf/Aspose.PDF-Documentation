---
title: 设置PDF文件信息在PHP中
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 设置PDF文件信息

要使用**Aspose.PDF Java for PHP**更新Pdf文档信息，只需调用**SetPdfFileInfo**类。

PHP代码

```php

# 打开一个pdf文档。
$doc = new Document($dataDir . "input1.pdf");

# 获取文档信息
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF信息");
$doc_info->setTitle("设置PDF文档信息");

# 使用新信息保存更新的文档
$doc->save($dataDir . "Updated_Information.pdf");

print "更新文档信息，请检查输出文件。";

```

**下载运行代码**

从以下任何一个社交编码网站下载**设置PDF文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)