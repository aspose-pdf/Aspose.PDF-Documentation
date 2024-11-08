---
title: 保存 PDF 文档
linktitle: 保存
type: docs
weight: 30
url: /zh/php-java/save-pdf-document/
description: 了解如何使用 Aspose.PDF for PHP via Java 库保存 PDF 文件。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将 PDF 文档保存到文件系统

您可以使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 save 方法将创建或修改的 PDF 文档保存到文件系统。

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```