---
title: 使用 Python 的 PDF 粘性注释
linktitle: 粘性注释
type: docs
weight: 50
url: /zh/python-net/sticky-annotations/
description: 了解如何使用 Aspose.PDF 在 Python via .NET 中为 PDF 文档添加粘性注释，以实现评论和反馈。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 关于如何在 PDF 中操作粘性注释的指南
Abstract: 本文提供了使用 Aspose.PDF for Python 库在 PDF 文档中管理水印注释的详细指南。它解释了添加、检索和删除水印注释的过程，以确保文档的真实性和品牌标识。水印注释可用于在页面的固定大小和位置嵌入图形，例如徽标。指南包括代码片段，演示如何在特定位置添加具有可调不透明度的水印注释，以及如何检索和删除现有的水印注释。代码示例展示了使用 Aspose.PDF 库以编程方式操作 PDF 文档，为开发者在其应用程序中集成水印功能提供了实用方法。
---

## 添加水印注释

最显眼且易于可视化和传输的注释是水印注释。这是将徽标或任何其他标识放入 PDF 文档中以确认其原创性的最佳方式。

水印注释用于表示应以固定大小和位置打印在页面上的图形，无论打印页面的尺寸如何。

您可以使用 [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) 在 PDF 页面特定位置添加水印文本。也可以通过使用 [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties) 属性来控制水印的不透明度。

请查看以下代码片段以添加 WatermarkAnnotation。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## 获取水印注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## 删除水印注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


