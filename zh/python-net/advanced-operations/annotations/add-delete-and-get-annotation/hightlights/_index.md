---
title: 使用 Python 的 PDF 高亮注释
linktitle: 高亮注释
type: docs
weight: 20
url: /zh/python-net/highlights-annotation/
description: 了解如何使用 Aspose.PDF 在 Python 中为 PDF 文件添加高亮注释，以突出文本。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 关于如何在 PDF 中操作高亮注释的指南
Abstract: 本文提供了关于如何在 PDF 文档中使用文本标记注释的全面指南，重点关注 Aspose.PDF 库在 Python 中提供的功能。它解释了不同类型注释的目的和用法，包括高亮、下划线、删除线和波浪线注释，每种注释均用于以不同方式强调或修改文本。文档概述了将这些注释添加到 PDF 的步骤，包括加载文档、使用特定参数（如标题和颜色）创建注释，并将其附加到所需页面。此外，本文还包含了从 PDF 检索注释的代码片段，允许用户根据类型过滤并打印注释详情。最后，详细说明了删除注释的过程，提供了从文档中移除每种文本标记注释的代码示例。本指南是面向希望使用 Python 以编程方式操作 PDF 文件中文本注释的开发者的实用资源。
---

PDF 中的文本标记注释用于高亮、下划线、删除或添加注释到文档中的文本。这些注释旨在突出或引起对文本特定部分的注意。此类注释允许用户以可视方式标记或修改 PDF 文件的内容。

高亮注释用于使用彩色背景（通常为黄色）标记文本，以指示其重要性或相关性。

下划线注释是一条放置在所选文本下方的线，用于表示重要性、强调或建议的编辑。

删除线注释对特定文本进行划除，以显示该文本已被删除、替换或不再有效。

波浪线用于在文本下方划线，以表示不同类型的强调，例如拼写错误、潜在问题或建议的更改。

## 添加文本标记注释

为了向 PDF 文档添加文本标记注释，我们需要执行以下操作：

1. 加载 PDF 文件 - 新的 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 创建注释：
- [高亮注释](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation/) 并设置参数（标题，颜色）。
- [删除线注释](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/) 并设置参数（标题，颜色）。
- [波浪线注释](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squigglyannotation/) 并设置参数（标题，颜色）。
- [下划线注释](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/underlineannotation/) 并设置参数（标题，颜色）。
1. 然后我们应将所有注释添加到页面。

### 添加高亮注释

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
    document.save(output_file)
```

### 添加删除线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(output_file)
```

### 添加波浪线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(output_file)
```

### 添加下划线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(output_file)
```

## 获取文本标记注释

请尝试使用以下代码片段从 PDF 文档获取文本标记注释。

### 获取高亮注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)
```

### 获取删除线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)
```


### 获取波浪线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)
```

### 获取下划线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)
```

## 删除文本标记注释

以下代码片段展示了如何从 PDF 文件中删除文本标记注释。

### 删除高亮注释

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

### 删除删除线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 删除波浪线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

### 删除下划线注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



