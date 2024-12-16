---
title: 将 PDF/A 转换为 PDF 格式
linktitle: 将 PDF/A 转换为 PDF 格式
type: docs
weight: 110
url: /zh/php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: 本主题向您展示如何使用 PHP 库通过 Aspose.PDF 将 PDF/A 文件转换为 PDF 文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将 PDF/A 文档转换为 PDF

将 PDF/A 文档转换为 PDF 意味着从原始文档中移除 <abbr title="可移植文档格式存档">PDF/A</abbr> 限制。类 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 具有方法 removePdfaCompliance(..) 用于从输入/源文件中移除 PDF 兼容性信息。

```php
// 使用输入文件创建 Document 类的新实例
$document = new Document($inputFile);

// 从文档中移除 PDF/A 兼容性
$document->removePdfaCompliance();

// 将修改后的文档保存到输出文件
$document->save($outputFile);
```

如果您对文档进行任何更改（例如，
 添加页面）。在下面的示例中，输出文档在添加页面后失去了PDF/A合规性。

```php
// 使用输入文件创建Document类的新实例
$document = new Document($inputFile);

// 从文档中移除PDF/A合规性
$document->getPages()->add();

// 将修改后的文档保存到输出文件
$document->save($outputFile);
```