---
title: 创建 PDF 文档
linktitle: 创建
type: docs
weight: 10
url: zh/php-java/create-document/
description: 了解如何在 Aspose.PDF for PHP via Java 中创建 PDF 文件。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** API 允许应用程序开发人员在其应用程序中嵌入 PDF 文档处理功能。它可以用于创建和读取 PDF 文件，而无需在底层计算机上安装任何其他软件。Aspose.PDF for PHP via Java 可以用于多种应用程序类型，如桌面应用程序、JSP 和 JSF 应用程序。

## 如何使用 PHP via Java 创建 PDF 文件

要使用 PHP via Java 创建 PDF 文件，可以使用以下步骤。

1. 实例化一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)

1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) 对象
1. 将 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) 添加到页面的 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 集合中
1. 保存生成的 PDF 文档

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```