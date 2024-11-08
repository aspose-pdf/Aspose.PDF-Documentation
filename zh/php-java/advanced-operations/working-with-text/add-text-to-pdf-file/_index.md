---
title: 向 PDF 文件添加文本 
linktitle: 向 PDF 文件添加文本
type: docs
weight: 10
url: /zh/php-java/add-text-to-pdf-file/
description: 本文介绍了在 Aspose.PDF 中处理文本的各个方面。了解如何向 PDF 添加文本、添加 HTML 片段或使用自定义 OTF 字体。
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

向现有 PDF 文件添加文本：

1. 使用 Document 对象打开输入 PDF。
1. 获取要添加文本的特定页面。
1. 创建一个内容为 "Aspose.PDF" 的文本片段。
1. 设置文本片段在页面上的位置。
1. 设置文本片段的文本属性。
1. 为页面创建一个 TextBuilder 对象。
1. 将文本片段附加到 PDF 页面。
4. 将生成的 PDF 文档保存到输出文件。

## 添加文本

以下代码片段展示了如何在现有 PDF 文件中添加文本。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 获取特定页面
    $page = $document->getPages()->add();
    
    // 创建文本片段
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // 设置文本属性
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // 创建 TextBuilder 对象
    $textBuilder = new TextBuilder($page);
    // 将文本片段附加到 PDF 页面
    $textBuilder->appendText($textFragment);

    // 保存生成的 PDF 文档。    
    $document->save($outputFile);
    $document->close();
```