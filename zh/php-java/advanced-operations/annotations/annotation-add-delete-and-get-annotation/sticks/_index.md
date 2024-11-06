---
title: PDF 粘性注释
linktitle: 粘性注释
type: docs
weight: 50
url: zh/php-java/sticky-annotations/
description: 本主题关于粘性注释，作为示例我们展示了文本中的水印注释。它用于表示页面上的图形。查看代码片段以解决此任务。
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 添加水印注释

水印注释用于表示将在页面上以固定大小和位置打印的图形，无论打印页面的尺寸如何。

您可以使用 [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) 在 PDF 页面的特定位置添加水印文本。水印的不透明度也可以通过使用不透明属性来控制。

请查看以下代码片段以添加 WatermarkAnnotation。

```php

    // 打开文档
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // 获取特定页面
    $page = $document->getPages()->get_Item(1);
    
    // 创建注释
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    // 将注释添加到页面的注释集合中
    $page->getAnnotations()->add($wa);

    // 创建用于字体设置的 TextState
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    // 设置注释文本的不透明度级别
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo" ];
    // 向注释添加文本
    $wa->setTextAndState($watermarkStrings, $ts);

    // 保存生成的 PDF 文档。
    $document->save($outputFile);
    $document->close();
```