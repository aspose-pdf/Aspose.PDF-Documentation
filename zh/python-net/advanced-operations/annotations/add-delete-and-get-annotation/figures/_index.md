---
title: 使用 Python 添加图形注释
linktitle: 图形注释
type: docs
weight: 30
url: /zh/python-net/figures-annotation/
description: 本文描述如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中添加、获取和删除图形注释
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 关于如何在 PDF 中操作图形注释的指南
Abstract: 本文提供了使用 Aspose.PDF for Python 在 PDF 文档中添加、检索和删除方形、圆形、多边形和折线注释的完整指南。方形和圆形注释分别使用矩形和椭圆形状在 PDF 页面上直观地突出显示特定区域。文章包含逐步说明和 Python 代码片段，演示通过加载 PDF 文件、配置注释属性（如标题、颜色和不透明度）并将其附加到 PDF 页面来创建这些注释。此外，文章还详细介绍了按类型检索注释、打印其矩形尺寸以及从 PDF 文档中删除注释的方法。还覆盖了多边形和折线注释，其中多边形由一系列相连的顶点构成闭合形状，而折线则以开放方式连接顶点。文档提供了代码示例，阐明向 PDF 添加这些注释的过程，以及访问和移除它们的方法。

---

## 添加方形和圆形注释

在 PDF 文档中，方形注释指的是一种以正方形形状表示的特定类型注释。方形注释用于突出或引起对文档中特定区域或章节的注意。

[方形](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/) 和 [圆形](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/circleannotation/) 注释应分别在页面上显示矩形或椭圆。

创建方形或圆形注释的步骤：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation) 并设置参数（new Rectangle、title、color、interior_color、opacity）。
1. 然后需要将方形注释添加到页面。

以下代码片段展示了如何在 PDF 页面中添加方形注释。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(output_file)
```

以下代码片段展示了如何在 PDF 页面中添加圆形注释。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(output_file)
```

例如，我们将看到将方形和圆形注释添加到 PDF 文档后的以下结果：

![圆形和方形注释示例](circle_demo.png)

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

以下代码片段展示了如何从 PDF 文件中删除圆形注释。

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

以下代码片段展示了如何从 PDF 文件中删除方形注释。

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

Polyline 工具允许您在文档上创建具有任意边数的形状和轮廓。

[Polygon Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation/) 表示页面上的多边形。它们可以有任意数量的顶点，由直线连接。

[Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) 也类似于多边形，唯一的区别是首尾顶点不隐式相连。

创建多边形注释的步骤：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [Polygon Annotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polygonannotation) 并设置多边形参数（new Rectangle、new Points、title、color、interior_color 和 opacity）。
1. 然后我们可以将注释添加到页面。

以下代码片段展示了如何向 PDF 文件添加多边形注释：

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

以下代码片段展示了如何向 PDF 文件添加折线注释：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 创建新的 [Polyline Annotations](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/polylineannotation/) 并设置多边形参数（new Rectangle、new Points、title、color、interior_color 和 opacity）。
1. 然后我们可以将注释添加到页面。

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


