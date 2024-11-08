---
title: 从 PDF 中移除元数据在 PHP 中
type: docs
weight: 70
url: /zh/java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 移除元数据

要使用 **Aspose.PDF Java for PHP** 从 PDF 文档中移除元数据，只需调用 **RemoveMetadata** 类。

PHP 代码

```php

# 打开一个 pdf 文档。
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# 保存更新后的文档与新信息
$doc->save($dataDir . "Remove_Metadata.pdf");

print "成功移除元数据，请检查输出文件。" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载 **Remove Metadata (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)