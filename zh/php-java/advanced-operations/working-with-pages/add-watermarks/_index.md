---
title: 添加水印到 PDF
linktitle: 添加水印
type: docs
weight: 90
url: /zh/php-java/add-watermarks/
description: 本文解释了使用 PHP 处理工件和获取 PDF 水印的功能。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** 允许使用工件向您的 PDF 文档添加水印。请查看本文以解决您的任务。

使用 Adobe Acrobat 创建的水印称为工件（如 PDF 规范的 14.8.2.2 实际内容和工件中所述）。为了处理工件，Aspose.PDF 提供了两个类：[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 和 [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection)。

为了获取特定页面上的所有工件， [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) 类具有 Artifacts 属性。
 这个主题解释了如何在 PDF 文件中处理工件。

## 处理工件

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 类包含以下属性：

**Artifact.Type** – 获取工件类型（支持 Artifact.ArtifactType 枚举的值，其中包括 Background, Layout, Page, Pagination 和 Undefined）。
**Artifact.Subtype** – 获取工件子类型（支持 Artifact.ArtifactSubtype 枚举的值，其中包括 Background, Footer, Header, Undefined, Watermark）。

{{% alert color="primary" %}}

请注意，使用 Adobe Acrobat 创建的水印的类型为 Pagination，子类型为 Watermark。

{{% /alert %}}

**Artifact.Contents** – 获取工件内部操作符的集合。其支持的类型是 System.Collections.ICollection。
**Artifact.Form** – 获取工件的 XForm（如果使用了 XForm）。水印、页眉和页脚工件包含显示所有工件内容的 XForm。

**Artifact.Image** – 获取工件的图像（如果存在图像，否则为 null）。**Artifact.Text** – 获取文档对象的文本。  
**Artifact.Rectangle** – 获取文档对象在页面上的位置。  
**Artifact.Rotation** – 获取文档对象的旋转角度（以度为单位，正值表示逆时针旋转）。  
**Artifact.Opacity** – 获取文档对象的不透明度。可能的值范围是0到1，其中1是完全不透明。

## 编程示例：获取水印

以下代码片段展示了如何使用PHP获取PDF文件第一页上的每个水印。

```php

    // 打开文档
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```