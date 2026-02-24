---
title: 使用 Python 的额外注释
linktitle: 额外注释
type: docs
weight: 60
url: /zh/python-net/extra-annotations/
description: 了解如何使用 Aspose.PDF 在 Python 中向 PDF 添加额外注释，如高亮或备注，以增强 PDF 内容。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 关于如何在 PDF 中操作额外注释的指南
Abstract: 本文提供了使用 Python（特别是 Aspose.PDF 库）在 PDF 文件中添加、检索和删除不同类型注释的完整指南。它涵盖了三种注释类型——Caret（插入符号）、Link（链接）和 Redaction（编辑删除）。文章解释了 Caret 注释用于文本编辑建议。它描述了加载 PDF 文件、使用特定参数（如矩形、标题、主题、标志和颜色）创建 Caret 注释、将其追加到文档并保存更改的过程。文中提供了添加、检索和删除 Caret 注释的代码示例。Link 注释用于创建可点击的区域，以重定向到 URL 或文档的特定位置。指南包括通过识别文本片段（例如电话号码）来添加 Link 注释、设置动作以及管理这些注释的说明和代码。
---

## 如何使用 Python 向现有 PDF 文件添加 Caret 注释

Caret 注释是一种指示文本编辑的符号。Caret 注释也是一种标记注释，因此 Caret 类继承自 Markup 类，并提供获取或设置 Caret 注释属性以及重置其外观流程的功能。
Caret 注释常用于对文本提出更改、添加或修改的建议。

创建 Caret 注释的步骤：

1. 加载 PDF 文件 - 新建 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [Caret 注释](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) 并设置 Caret 参数（新矩形、标题、主题、标志、颜色）。此注释用于指示文本插入。
1. 一旦我们能够将注释追加到页面上。

以下代码片段展示了如何向 PDF 文件添加 Caret 注释：

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### 获取 Caret 注释

请尝试使用以下代码片段在 PDF 文档中获取 Caret 注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### 删除 Caret 注释

以下代码片段展示了如何使用 Python 删除 PDF 文件中的 Caret 注释。

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## 使用 Aspose.PDF for Python 通过 Redaction 注释编辑特定页面区域

Aspose.PDF for Python via .NET 支持在现有 PDF 文件中添加和操作注释的功能。PDF 文档中的 Redaction 注释用于永久删除或隐藏文档中的机密信息。编辑这些信息的过程包括覆盖或遮蔽特定内容，如文本、图像或图形，以限制其对他人的可见性和访问性，从而确保敏感信息在文档中保持隐藏和受保护。为满足此需求，提供了一个名为 [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) 的类，可用于编辑特定页面区域，或用于操作现有的 Redaction 注释并对其进行编辑（即展平注释并删除其下方的文本）。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### 获取 Redaction 注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### 删除 Redaction 注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



