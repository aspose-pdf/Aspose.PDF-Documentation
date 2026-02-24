---
title: 在 PDF 中使用链接注释
linktitle: 链接注释
type: docs
weight: 70
url: /zh/python-net/link-annotations/
description: Aspose.PDF for Python via .NET 允许您在 PDF 文档中添加、获取和删除链接注释。
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## 在现有 PDF 文件中添加链接注释

[链接](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) 是注释，点击时可打开 URL 或在同一文档或外部文档中的特定位置之间移动。

链接注释是可以放置在页面任意位置的矩形区域。每个链接都有相应的 PDF 动作关联。当用户点击该链接区域时，将执行此动作。

以下代码片段展示了如何使用电话号码示例向 PDF 文件添加链接注释：

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### 获取链接注释

请尝试使用以下代码片段从 PDF 文档中获取 [链接注释](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### 删除链接注释

以下代码片段展示了如何从 PDF 文件中删除链接注释。为此，我们需要在第 1 页查找并删除所有链接注释。之后，我们将保存删除了注释的文档。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
