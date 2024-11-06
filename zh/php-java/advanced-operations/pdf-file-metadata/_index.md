---
title: 使用PDF文件元数据
linktitle: PDF文件元数据
type: docs
weight: 140
url: zh/php-java/pdf-file-metadata/
description: 本节解释如何获取PDF文件信息，如何从PDF文件获取XMP元数据，设置PDF文件信息。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取PDF文件信息

要获取有关PDF文件的特定信息，首先使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类的[getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--)方法获取'docInfo'对象。一旦检索到'docInfo'对象，就可以获取各个属性的值。

以下代码片段显示了如何设置PDF文件信息。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 获取文档信息
    $docInfo = $document->getInfo();

    // 显示文档信息
    $responseData1 = "作者: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "创建日期: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "关键词: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "修改日期: " . $docInfo->getModDate() . ", ";
    $responseData5 = "主题: " . $docInfo->getSubject() . ", ";
    $responseData6 = "标题: " . $docInfo->getTitle() . "";

    $document->close();
```