---
title: 使用 Python 添加额外注释
linktitle: 额外注释
type: docs
weight: 60
url: /zh/python-net/extra-annotations/
description: 本节描述如何从您的 PDF 文档中添加、获取和删除额外类型的注释。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 添加额外注释",
    "alternativeHeadline": "如何在 PDF 中添加额外注释",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 链接注释, 插入符注释",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "本节描述如何使用 Python 从您的 PDF 文档中添加、获取和删除额外类型的注释。"
}
</script>


## 如何通过 Python 将插入符号注释添加到现有 PDF 文件中

插入符号注释是指示文本编辑的符号。插入符号注释也是一种标记注释，因此 Caret 类继承自 Markup 类，并提供函数以获取或设置插入符号注释的属性并重置插入符号注释外观的流程。插入符号注释通常用于建议文本的更改、添加或修改。

创建插入符号注释的步骤：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
2. 创建新的 [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) 并设置插入符号参数（新建矩形、标题、主题、标志、颜色）。此注释用于指示文本的插入。
3. 一旦我们能够将注释附加到页面。

以下代码片段显示了如何将插入符号注释添加到 PDF 文件：

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose 用户"
    caretAnnotation1.subject = "插入文本 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### 获取插入符号注释

请尝试使用以下代码片段在 PDF 文档中获取插入符号注释

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

### 删除插入符号注释

以下代码片段展示了如何使用 Python 从 PDF 文件中删除插入符号注释。

```python

    import aspose.pdf as ap

    # 加载 PDF 文件
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

## 添加链接注释

[链接](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) 是在点击时打开 URL 或移动到同一文档或外部文档中某些位置的注释。

一个链接注释是一个可以放置在页面任意位置的矩形区域。每个链接都有一个与之关联的相应 PDF 操作。当用户点击此链接的区域时，将执行此操作。

以下代码片段展示了如何使用电话号码示例向 PDF 文件添加链接注释：

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # 创建 TextFragmentAbsorber 对象以查找电话号码
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # 仅接受第一页的吸收器
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # 创建链接注释并设置操作以拨打电话号码
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # 添加注释到页面
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### 获取链接注释

请尝试使用以下代码片段从 PDF 文档中获取 [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/)。

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

以下代码片段显示了如何从 PDF 文件中删除链接注释。为此，我们需要找到并删除第一页上的所有链接注释。之后，我们将保存删除注释的文档。

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


## 使用 Aspose.PDF for Python 对指定页面区域进行编辑注释

Aspose.PDF for Python via .NET 支持在现有 PDF 文件中添加和操作注释。PDF 文档中的编辑注释用于永久删除或隐藏文档中的机密信息。编辑信息的过程包括覆盖或遮盖特定内容，例如文本、图像或图形，以限制其他人对其的可见性和访问。这确保了敏感信息在文档中保持隐藏和保护。为了满足这一要求，提供了一个名为 [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) 的类，可以用来编辑特定页面区域，或者可以用来操作现有的编辑注释并编辑它们（即展平注释并移除其下的文本）。

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


### 获取涂黑注解

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

### 删除涂黑注解

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


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>