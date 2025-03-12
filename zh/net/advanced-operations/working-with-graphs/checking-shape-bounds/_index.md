---
title: 在 Aspose.Pdf.Drawing.Graph.Shapes 集合中检查形状边界
type: docs
weight: 10
url: /zh/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: 了解如何检查插入到 Aspose.Pdf.Drawing.Graph.Shapes 集合中的形状的边界，以确保其适合其父容器。
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Aspose.Pdf.Drawing.Graph.Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Aspose.PDF for .NET 在 `Drawing.Graph.Shapes` 集合中的新边界检查功能自动验证元素尺寸与父容器的匹配，防止布局溢出。当元素超出容器限制时，它会触发异常，在插入过程中强制执行严格的尺寸约束，以确保精确的 PDF 格式和简化设计准确性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1000",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-02-28",
    "description": ""
}
</script>

## 介绍
本文档提供了关于如何使用 Aspose.Pdf.Drawing.Graph.Shapes 集合中的边界检查功能的详细指南。此功能确保元素适合其父容器，并可以配置为在组件不适合时抛出异常。我们将逐步介绍实现此功能的步骤，并提供完整示例。

## 先决条件
您需要以下内容：
* Visual Studio 2019 或更高版本
* Aspose.PDF for .NET 25.3 或更高版本
* 包含一些页面的示例 PDF 文件

您可以从官方网站下载 Aspose.PDF for .NET 库，或使用 Visual Studio 中的 NuGet 包管理器进行安装。

## 步骤
以下是完成任务的步骤：
1. 创建一个新文档并添加一个页面。
2. 创建一个具有指定尺寸的 `Graph` 对象。
3. 创建一个具有指定尺寸的 `Shape` 对象。
4. 将 `BoundsCheckMode` 设置为 `ThrowExceptionIfDoesNotFit`。
5. 尝试将形状添加到图形中。

让我们看看如何在 C# 代码中实现这些步骤。

### 步骤 1：创建一个新文档并添加一个页面
首先，创建一个新的 PDF 文档并向其中添加一个页面。

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### 步骤 2：创建一个具有指定尺寸的 Graph 对象
接下来，创建一个宽度和高度均为 100 单位的 `Graph` 对象。将图形定位在页面顶部 10 单位和左侧 15 单位的位置。为图形添加黑色边框。

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### 步骤 3：创建一个具有指定尺寸的 Aspose.Pdf.Drawing.Shape 对象（例如，Aspose.Pdf.Drawing.Rectangle）
创建一个宽度和高度均为 50 单位的矩形对象。将矩形定位在 (-1, 0)，这超出了图形的边界。

```csharp
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### 步骤 4：将 BoundsCheckMode 设置为 ThrowExceptionIfDoesNotFit
将 `BoundsCheckMode` 设置为 `ThrowExceptionIfDoesNotFit`，以确保如果矩形不适合图形，则抛出异常。

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### 步骤 5：尝试将矩形添加到图形中
尝试将矩形添加到图形中。这将抛出 `Aspose.Pdf.BoundsOutOfRangeException`，因为矩形不适合图形的尺寸。

```csharp
graph.Shapes.Add(rect);
```

## 输出
执行代码后，预期输出将是一个 `Aspose.Pdf.BoundsOutOfRangeException`，其消息为：

```
Bounds not fit. Container dimensions: 100x100
```

## 故障排除
如果出现问题，以下是一些提示：
* 确保正确设置了 `BoundsCheckMode`。
* 验证元素和容器的尺寸是否准确。
* 检查元素在容器内的位置。

## 完整示例
以下是演示所有步骤的完整示例：

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Page page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
        Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    Aspose.Pdf.Page page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## 结论
'Aspose.Pdf.Drawing.Graph.Shapes' 集合中的边界检查功能是确保元素适合父容器的强大工具。通过将 BoundsCheckMode 设置为 ThrowExceptionIfDoesNotFit，您可以防止 PDF 文档中的布局问题。此功能在元素定位和尺寸至关重要的场景中尤其有用。有关更多详细信息，请访问 [官方文档](https://docs.aspose.com/pdf/net/)。