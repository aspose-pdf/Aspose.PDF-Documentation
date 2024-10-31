---
title: 用Python添加图形注释
linktitle: 图形注释
type: docs
weight: 30
url: /python-net/figures-annotation/
description: 本文描述了如何使用Aspose.PDF for Python通过.NET添加、获取和删除PDF文档中的图形注释
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "用Python添加图形注释",
    "alternativeHeadline": "如何在PDF中添加图形注释",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 图形注释, 多边形注释, 线条注释, 方形注释, 圆形注释",
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
    "url": "/python-net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/figures-annotation/"
    },
    "dateModified": "2023-02-04",
    "description": "本文描述了如何使用Aspose.PDF for Python添加、获取和删除PDF文档中的图形注释"
}
</script>


## 添加方形和圆形注释

在 PDF 文档中，方形注释指的是一种特定类型的注释，它以方形形状表示。方形注释用于突出显示或引起文档中特定区域或部分的注意。

[方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/)和[圆形](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/)注释分别在页面上显示一个矩形或椭圆。

创建方形或圆形注释的步骤：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) 并设置参数（新的矩形、标题、颜色、内部颜色、不透明度）。
1. 然后我们需要将方形注释添加到页面中。

以下代码片段展示了如何在 PDF 页面中添加方形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "约翰·史密斯"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

以下代码片段向您展示了如何在 PDF 页面中添加圆形注释。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "约翰·史密斯"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```


例如，我们将看到在 PDF 文档中添加方形和圆形注释的以下结果：

![Circle and Square Annotation demo](circle_demo.png)

### 获取圆形注释

请尝试使用以下代码片段从 PDF 文档中获取圆形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)
```

### 获取方形注释

请尝试使用以下代码片段从 PDF 文档中获取方形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)
```

### 删除圆形注释

以下代码片段展示了如何从PDF文件中删除圆形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

### 删除方形注释

以下代码片段展示了如何从PDF文件中删除方形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```

## 添加多边形和折线注释

折线工具允许您在文档上创建具有任意边数的形状和轮廓。

[Polygon Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) 表示页面上的多边形。它们可以具有任意数量的由直线连接的顶点。

[Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) 也类似于多边形，唯一的区别是第一个和最后一个顶点没有隐式连接。

我们创建多边形注释的步骤：

1. 加载 PDF 文件 - 新的 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) 并设置多边形参数（新的矩形、新的点、标题、颜色、内部颜色和不透明度）。
1. 之后我们可以将注释添加到页面。

以下代码片段显示了如何向 PDF 文件添加多边形注释：

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(output_file)
```


以下代码片段显示了如何向 PDF 文件添加折线注释：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) 并设置多边形参数（新建矩形、新建点、标题、颜色、内颜色和不透明度）。
1. 之后我们可以将注释添加到页面。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(output_file)
```


### 获取多边形和折线注释

请尝试使用以下代码片段在 PDF 文档中获取多边形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
```

请尝试使用以下代码片段在 PDF 文档中获取折线注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)
```

### 删除多边形和折线注释

以下代码片段展示了如何从 PDF 文件中删除多边形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```


以下代码片段展示了如何从 PDF 文件中删除折线注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
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