---
title: 打开 PDF 文档
linktitle: 打开
type: docs
weight: 20
url: zh/php-java/open-pdf-document/
description: 了解如何使用 Aspose.PDF for PHP via Java 打开 PDF 文件。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 打开现有的 PDF 文档

PDF 文件或可移植文档格式文件已成为文档交换的通用标准。它们被广泛用于保存文档的格式。然而，使用诸如通过 Java 的 PHP 等编程语言处理 PDF 文件可能有点困难。本文介绍了 Aspose.PDF for PHP via Java 库，它可以让您快速轻松地打开 PDF 文件。

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "文档已成功打开。文件大小: " . filesize($inputFile);
```