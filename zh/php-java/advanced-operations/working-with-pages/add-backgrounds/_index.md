---
title: 为 PDF 添加背景
linktitle: 添加背景
type: docs
weight: 110
url: zh/php-java/add-backgrounds/
descriptions: 使用 PHP 为您的 PDF 文件添加背景图像。使用 BackgroundArtifact 对象。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

背景图像可以用于为文档添加水印或其他细微设计。在 Aspose.PDF for PHP via Java 中，每个 PDF 文档是页面的集合，每个页面包含一组工件。可以使用 [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) 类为页面对象添加背景图像。

下面的代码片段展示了如何使用 BackgroundArtifact 对象在 PHP 中为 PDF 页面添加背景图像。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 向文档对象添加新页面
    $page = $document->getPages()->add();

    // 创建 BackgroundArtifact 对象    
    $background = new BackgroundArtifact();

    // 为 backgroundArtifact 对象指定图像
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // 将 backgroundArtifact 添加到页面的 artifacts 集合
    $page->getArtifacts()->add($background);

    // 保存更新的 PDF 文件
    $document->save($outputFile);
    $document->close();
```