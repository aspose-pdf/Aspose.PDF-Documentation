---
title: 使用 Python 对 PDF 进行文本注释
linktitle: 文本注释
type: docs
weight: 10
url: /zh/python-net/text-annotation/
description: Aspose.PDF for Python 允许您在 PDF 文档中添加、获取和删除文本注释。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 关于如何在 PDF 中操作文本注释的指南
Abstract: 本文提供了使用 Aspose.PDF for Python 库在 PDF 文件中操作文本注释的全面指南。它涵盖了包括 Text、Free Text 和 StrikeOutAnnotations 在内的各种注释类型的添加、检索和删除。文本注释是附加在 PDF 中特定位置的备注，以图标形式显示，打开后会弹出包含注释文本的窗口。自由文本注释直接在页面上显示文本，而划线注释（StrikeOutAnnotations）则在文本上划线以表示删除或忽略。该过程涉及使用 `add()` 方法将注释添加到页面的 Annotations 集合中，并为每种注释类型提供示例。代码片段演示了如何实现这些任务，包括使用标题、主题、颜色和标志等特定属性创建注释，以及从 PDF 页面检索和删除注释。本指南为希望通过 Aspose.PDF 使用注释操作来增强 PDF 文档的开发者提供了实用资源。
---

## 如何向现有 PDF 文件添加文本注释

文本注释是附加在 PDF 文档中特定位置的注释。关闭时，注释显示为图标；打开时，它会显示一个弹出窗口，包含读者选择的字体和大小的注释文本。

注释由特定页面的 [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) 集合包含。此集合仅包含该页面的注释；每页都有自己的 Annotations 集合。

要向特定页面添加注释，请使用 [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/#methods) 方法将其添加到该页面的 Annotations 集合中。

1. 首先，创建您想要添加到 PDF 的注释。
1. 然后打开输入 PDF。
1. 将注释添加到 'page' 对象的 [Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/annotationcollection/) 集合中。

以下代码片段展示了如何在 PDF 页面中添加注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(300, 700.664, 320, 720.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.contents = "qwerty"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(textAnnotation)
    document.save(output_file)
```

## 从 PDF 文件获取文本注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)
```

## 从 PDF 文件删除文本注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


## 如何添加（或创建）新的自由文本注释

自由文本注释直接在页面上显示文本。[FreeTextAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/freetextannotation/) 类允许创建此类注释。在下面的代码片段中，我们在字符串的第一次出现上方添加自由文本注释。

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(output_file)
```

## 从 PDF 文件获取自由文本注释

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)
```

## 从 PDF 文件删除自由文本注释

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(output_file)
```


### 使用 StrikeOutAnnotation 划除单词

Aspose.PDF for Python 允许您在 PDF 文档中添加、删除和更新注释。其中的一个类还可以对注释进行划线。当 StrikeOutAnnotation 应用于 PDF 时，会在指定文本上划一条线，表示该文本应被删除或忽略。

以下代码片段展示了如何向 PDF 添加 [StrikeOutAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/strikeoutannotation/)。

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


## 从 PDF 获取 StrikeOutAnnotation

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

## 从 PDF 删除 StrikeOutAnnotation

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



