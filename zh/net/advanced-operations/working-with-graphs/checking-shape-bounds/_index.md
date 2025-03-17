---
title: 检查形状集合中的形状边界
type: docs
weight: 70
url: /zh/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: 了解如何检查插入到形状集合中的形状的边界，以确保它适合其父容器。
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Aspose.PDF for .NET的新边界检查功能在`Drawing.Graph.Shapes`集合中自动验证元素尺寸与父容器的匹配，防止布局溢出。当元素超出容器限制时，它会触发异常，在插入过程中强制执行严格的尺寸约束，以确保精确的PDF格式和简化设计准确性",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "476",
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
    "dateModified": "2025-03-17",
    "description": ""
}
</script>

## 介绍
本文档提供了关于如何使用形状集合中的边界检查功能的详细指南。此功能确保元素适合其父容器，并可以配置为在组件不适合时抛出异常。我们将逐步介绍实现此功能的步骤，并提供完整示例。

## 先决条件
您需要以下内容：
* Visual Studio 2019或更高版本
* Aspose.PDF for .NET 25.3或更高版本
* 一个包含一些页面的示例PDF文件

您可以从官方网站下载Aspose.PDF for .NET库，或使用Visual Studio中的NuGet包管理器进行安装。

## 步骤
完成任务的步骤如下：
1. 创建PDF文档。
2. 创建一个具有指定尺寸的`Graph`对象。
3. 创建一个具有指定尺寸的`Shape`对象。
4. 将`BoundsCheckMode`设置为`ThrowExceptionIfDoesNotFit`。
5. 尝试将形状添加到图形中。

让我们看看如何在C#代码中实现这些步骤。

### 步骤1：创建PDF文档
首先，创建一个新的PDF文档并向其中添加一页。

```csharp
using (var document = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### 步骤2：创建一个具有指定尺寸的Graph对象
接下来，创建一个宽度和高度均为100单位的`Graph`对象。将图形定位在页面顶部10单位和左侧15单位的位置。为图形添加黑色边框。

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### 步骤3：创建一个具有指定尺寸的Shape对象（例如，矩形）
创建一个宽度和高度均为50单位的矩形对象。将矩形定位在(-1, 0)，这超出了图形的边界。

```csharp
var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### 步骤4：将BoundsCheckMode设置为ThrowExceptionIfDoesNotFit
将`BoundsCheckMode`设置为`ThrowExceptionIfDoesNotFit`，以确保如果矩形不适合图形，则抛出异常。

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### 步骤5：将矩形添加到图形中
将矩形添加到图形中。这将抛出一个`Aspose.Pdf.BoundsOutOfRangeException`，因为矩形不适合图形的尺寸。

```csharp
graph.Shapes.Add(rect);
```

## 输出
执行代码后，预期的输出将是一个`Aspose.Pdf.BoundsOutOfRangeException`，其消息为：

```
Bounds not fit. Container dimensions: 100x100
```

## 故障排除
如果出现问题，以下是一些提示：
* 确保`BoundsCheckMode`设置正确。
* 验证元素和容器的尺寸是否准确。
* 检查元素在容器内的位置。

## 完整示例
以下是一个完整示例，演示所有步骤的结合：

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        
        // Create a Graph object with specified dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Shape object (for example, Rectangle) with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    
    // Add page
    var page = doc.Pages.Add();

    // Create a Graph object with specified dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## 结论
形状集合中的边界检查功能是确保元素适合父容器的强大工具。通过将BoundsCheckMode设置为ThrowExceptionIfDoesNotFit，您可以防止PDF文档中的布局问题。此功能在元素定位和尺寸至关重要的场景中尤其有用。有关更多详细信息，请访问[官方文档](https://docs.aspose.com/pdf/net/)。