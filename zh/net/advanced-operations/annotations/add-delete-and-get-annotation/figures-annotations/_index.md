---
title: 使用 C# 添加图形注释
linktitle: 图形注释
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/figures-annotation/
description: 本文描述了如何从 PDF 文档中添加、获取和删除图形注释 Aspose.PDF for .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Figures Annotations using C#",
    "alternativeHeadline": "Enhance PDF Documents with Comprehensive Figure Annotations",
    "abstract": "介绍 Aspose.PDF for .NET 中的新图形注释功能，使用户能够无缝添加、检索和删除各种类型的注释，包括线条、方形、圆形、多边形和折线。这一功能增强了文档的互动性，允许在 PDF 文件中直接进行更清晰的沟通和视觉标记。使用此强大的注释工具集优化您的 PDF 编辑任务，专为使用 C# 的开发人员量身定制。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, figures annotations, line annotation, square annotation, circle annotation, polygon annotation, polyline annotation, free text annotation, ink annotation, Aspose.PDF for .NET",
    "wordcount": "2125",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "本文描述了如何从 PDF 文档中添加、获取和删除图形注释 Aspose.PDF for .NET"
}
</script>

PDF 文档管理应用程序提供了多种工具用于注释文档。从 PDF 的内部结构来看，这些工具是注释。我们支持以下几种绘图工具。

* 线注释 - 用于绘制线条和箭头的工具。
* 方形注释 - 用于绘制方形和矩形。
* 圆形注释 - 用于椭圆和圆形。
* 自由文本注释 - 用于标注评论。
* 多边形注释 - 用于多边形和云形。
* 折线注释 - 用于连接线。

## 在页面上添加形状和图形

添加注释的方法对于它们中的任何一种都是典型的。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

1. 加载 PDF 文件或通过 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 创建新文件。
1. 创建新的注释并设置参数（新的矩形、新的点、标题、颜色、宽度等）。
1. 创建新的 [PopupAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index)。
1. 将弹出注释与原始注释链接。
1. 将注释添加到页面

## 添加线条或箭头

线注释的目的是在页面上显示一条简单的线或箭头。
要创建线条，我们需要新的 LineAnnotation 对象。  
LineAnnotation 类的构造函数接受四个参数：

* 注释将添加到的页面。
* 定义注释边界的矩形。
* 定义线条起点和终点的两个点。

我们还需要初始化一些属性：

* `Title` - 通常是发表评论的用户的名称。
* `Subject` - 可以是任何字符串，但通常情况下是注释的名称。

为了给我们的线条设置样式，我们需要设置颜色、宽度、起始样式和结束样式。这些属性控制注释在 PDF 查看器中的外观和行为。例如，`StartingStyle` 和 `EndingStyle` 属性决定了在线条两端绘制什么样的形状，如开放箭头、闭合箭头、圆形等。

以下代码片段演示了如何将线注释添加到 PDF 文件中：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## 添加方形或圆形

[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) 和 [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) 注释将在页面上显示一个矩形或椭圆。当打开时，它们将显示一个弹出窗口，包含相关注释的文本。方形注释与圆形注释（Aspose. Pdf. Annotations. CircleAnnotation 类的实例）除了形状外是相似的。

### 添加圆形注释

要绘制新的圆形或椭圆注释，我们需要创建一个新的 CircleAnnotation 对象。`CircleAnnotation` 类的构造函数接受两个参数：

* 注释将添加到的页面。
* 定义注释边界的矩形。

我们还可以设置 `CircleAnnotation` 对象的一些属性，例如标题、颜色、内部颜色、不透明度。这些属性控制注释在 PDF 查看器中的外观和行为。在这里以及后面的方形中，`InteriorColor` 是填充颜色，`Color` 是边框颜色。

### 添加方形注释

绘制矩形与绘制圆形相同。以下代码片段演示了如何将圆形和方形注释添加到 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Circle Annotation
        var circleAnnotation = new Aspose.Pdf.Annotations.CircleAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(270, 160, 483, 383))
        {
            Title = "John Smith",
            Subject = "Circle",
            Color = Aspose.Pdf.Color.Red,
            InteriorColor = Aspose.Pdf.Color.MistyRose,
            Opacity = 0.5,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 316, 1021, 459))
        };

        // Create Square Annotation
        var squareAnnotation = new Aspose.Pdf.Annotations.SquareAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(67, 317, 261, 459))
        {
            Title = "John Smith",
            Subject = "Rectangle",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(circleAnnotation);
        document.Pages[1].Annotations.Add(squareAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCircleAndSquareAnnotations_out.pdf");
    }
}
```

作为示例，我们将看到将方形和圆形注释添加到 PDF 文档的以下结果：

## 添加多边形和折线注释

多边形工具允许您在文档上创建具有任意边数的形状和轮廓。

**多边形注释** 表示页面上的多边形。它们可以有任意数量的顶点，通过直线连接。
**折线注释** 也类似于多边形，唯一的区别是第一个和最后一个顶点没有隐式连接。

### 添加多边形注释

PolygonAnnotation 负责多边形注释。PolygonAnnotation 类的构造函数接受三个参数：

* 注释将添加到的页面。
* 定义注释边界的矩形。
* 定义多边形顶点的点数组。

`Color` 和 `InteriorColor` 分别用于边框和填充颜色。

### 添加折线注释

PolygonAnnotation 负责多边形注释。PolygonAnnotation 类的构造函数接受三个参数：

* 注释将添加到的页面。
* 定义注释边界的矩形。
* 定义多边形顶点的点数组。

与 `PolygonAnnotation` 不同，我们不能填充此形状，因此不需要使用 `InteriorColor`。

以下代码片段演示了如何将多边形和折线注释添加到 PDF 文件中：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPolygonAndPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Polygon Annotation
        var polygonAnnotation = new Aspose.Pdf.Annotations.PolygonAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(274, 381),
                new Aspose.Pdf.Point(555, 381),
                new Aspose.Pdf.Point(555, 304),
                new Aspose.Pdf.Point(570, 304),
                new Aspose.Pdf.Point(570, 195),
                new Aspose.Pdf.Point(274, 195)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Create Polyline Annotation
        var polylineAnnotation = new Aspose.Pdf.Annotations.PolylineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(545, 150),
                new Aspose.Pdf.Point(545, 190),
                new Aspose.Pdf.Point(667, 190),
                new Aspose.Pdf.Point(667, 110),
                new Aspose.Pdf.Point(626, 111)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(polygonAnnotation);
        document.Pages[1].Annotations.Add(polylineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddPolygonAndPolylineAnnotations_out.pdf");
    }
}
```

## 获取图形

所有注释都存储在 `Annotations` 集合中。任何注释都可以通过 `AnnotationType` 属性介绍其类型。因此，我们可以进行 LINQ 查询以过滤所需的注释。

### 获取线注释

下面的示例解释了如何从 PDF 文档的第一页获取所有线注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and print its coordinates
        foreach (var la in lineAnnotations)
        {
            Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
        }
    }
}
```

### 获取圆形注释

下面的示例解释了如何从 PDF 文档的第一页获取所有折线注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadCircleAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle annotations from the first page
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        // Iterate through each circle annotation and print its rectangle
        foreach (var ca in circleAnnotations)
        {
            Console.WriteLine($"[{ca.Rect}]");
        }
    }
}
```

### 获取方形注释

下面的示例解释了如何从 PDF 文档的第一页获取所有折线注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all square annotations from the first page
        var squareAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square)
            .Cast<Aspose.Pdf.Annotations.SquareAnnotation>();

        // Iterate through each square annotation and print its rectangle
        foreach (var sq in squareAnnotations)
        {
            Console.WriteLine($"[{sq.Rect}]");
        }
    }
}
```

### 获取折线注释

下面的示例解释了如何从 PDF 文档的第一页获取所有折线注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine)
            .Cast<Aspose.Pdf.Annotations.PolylineAnnotation>();

        // Iterate through each polyline annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

### 获取多边形注释

下面的示例解释了如何从 PDF 文档的第一页获取所有多边形注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon)
            .Cast<Aspose.Pdf.Annotations.PolygonAnnotation>();

        // Iterate through each polygon annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

## 删除图形

从 PDF 中删除注释的方法相当简单：

* 选择要删除的注释（创建一个集合）。
* 使用 foreach 循环遍历集合，并使用 Delete 方法从注释集合中删除每个注释。

### 删除线注释

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and delete it
        foreach (var la in lineAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLineAnnotations_out.pdf");
    }
}
```

### 删除圆形和方形注释

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle and square annotations from the first page
        var figures = document.Pages[1].Annotations
            .Where(a =>
                a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle
                || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square);

        // Iterate through each figure annotation and delete it
        foreach (var fig in figures)
        {
            document.Pages[1].Annotations.Delete(fig);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAndSquareAnnotations_out.pdf");
    }
}
```

### 删除多边形和折线注释

以下代码片段演示了如何从 PDF 文件中删除多边形和折线注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolylineAndPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline and polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon);

        // Iterate through each polyline or polygon annotation and delete it
        foreach (var pa in polyAnnotations)
        {
            document.Pages[1].Annotations.Delete(pa);
        }

        // Save PDF document
        document.Save(dataDir + DeletePolylineAndPolygonAnnotations_out.pdf");
    }
}
```

## 如何将墨水注释添加到 PDF 文件

墨水注释表示由一个或多个不相连的路径组成的手写“涂鸦”。打开时，它将显示一个弹出窗口，包含相关注释的文本。

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) 表示由一个或多个不相连的点组成的手写涂鸦。请尝试使用以下代码片段在 PDF 文档中添加 InkAnnotation。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define the rectangle for the ink annotation
        var arect = new Aspose.Pdf.Rectangle(156.574, 521.316, 541.168, 575.703);

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();
        var arrpt = new[]
        {
            new Aspose.Pdf.Point(209.727, 542.263),
            new Aspose.Pdf.Point(209.727, 541.94),
            new Aspose.Pdf.Point(209.727, 541.616)
        };
        inkList.Add(arrpt);

        // Create the ink annotation
        var ia = new Aspose.Pdf.Annotations.InkAnnotation(page, arect, inkList)
        {
            Title = "John Smith",
            Subject = "Pencil",
            Color = Aspose.Pdf.Color.LightBlue,
            CapStyle = Aspose.Pdf.Annotations.CapStyle.Rounded,
            Opacity = 0.5
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(ia)
        {
            Width = 25
        };
        ia.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(ia);

        // Save PDF document
        document.Save(dataDir + "AddInkAnnotation_out.pdf");
    }
}
```

### 设置 InkAnnotation 的线宽

[InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) 的宽度可以使用 LineInfo 和 Border 对象进行更改。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotationWithLineWidth()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();

        // Define line information
        var lineInfo = new Aspose.Pdf.Facades.LineInfo
        {
            VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 },
            Visibility = true,
            LineColor = System.Drawing.Color.Red,
            LineWidth = 2
        };

        // Convert line coordinates to Aspose.Pdf.Point array
        int length = lineInfo.VerticeCoordinate.Length / 2;
        var gesture = new Aspose.Pdf.Point[length];
        for (int i = 0; i < length; i++)
        {
            gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
        }

        // Add the gesture to the ink list
        inkList.Add(gesture);

        // Create the ink annotation
        var a1 = new Aspose.Pdf.Annotations.InkAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList)
        {
            Subject = "Test",
            Title = "Title",
            Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green)
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(a1)
        {
            Width = 3,
            Effect = Aspose.Pdf.Annotations.BorderEffect.Cloudy,
            Dash = new Aspose.Pdf.Annotations.Dash(1, 1),
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid
        };
        a1.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(a1);

        // Save PDF document
        document.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
    }
}
```

### 删除圆形注释

以下代码片段演示了如何从 PDF 文件中删除圆形注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAnnotation()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        foreach (var ca in circleAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAnnotation_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>