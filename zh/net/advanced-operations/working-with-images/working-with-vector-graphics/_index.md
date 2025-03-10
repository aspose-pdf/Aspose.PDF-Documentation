---
title: 使用矢量图形
linktitle: 使用矢量图形
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /zh/net/working-with-vector-graphics/
description: 本文描述了使用 C# 的 GraphicsAbsorber 工具的功能。
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics in PDF",
    "alternativeHeadline": "Programmatically manipulate PDF vector graphics",
    "abstract": "使用新的 GraphicsAbsorber 类以编程方式操作 PDF 文档中的矢量图形。Aspose.PDF for .NET C# 库允许对图形元素进行精确控制，使得移动、删除和添加图形等操作得以实现，从而增强 PDF 视觉效果。该工具提供了单个和批量操作方法，以实现最佳性能。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "GraphicsAbsorber, Vector Graphics, PDF Manipulation, C# library, Aspose.PDF, Move Graphics, Remove Graphics, Add Graphics, PDF Vector Graphics",
    "wordcount": "967",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "本节描述了使用 C# 库操作 GraphicsAbsorber PDF 文件的功能。"
}
</script>

在本章中，我们将探讨如何使用强大的 `GraphicsAbsorber` 类与 PDF 文档中的矢量图形进行交互。无论您需要移动、删除还是添加图形，本指南将向您展示如何有效地执行这些任务。让我们开始吧！

## 介绍<a name="introduction"></a>

矢量图形是许多 PDF 文档的重要组成部分，用于表示图像、形状和其他图形元素。Aspose.PDF 提供了 `GraphicsAbsorber` 类，允许开发人员以编程方式访问和操作这些图形。通过使用 `GraphicsAbsorber` 的 `Visit` 方法，您可以从指定页面提取矢量图形并执行各种操作，例如移动、删除或将其复制到其他页面。

## 1. 使用 `GraphicsAbsorber` 提取图形<a name="extracting-graphics"></a>

处理矢量图形的第一步是从 PDF 文档中提取它们。以下是使用 `GraphicsAbsorber` 类进行提取的方法：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Document-01.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}

```

### 说明：

1. **创建文档对象**：使用目标 PDF 文件的路径实例化一个新的 `Document` 对象。
2. **创建 `GraphicsAbsorber` 实例**：该类捕获指定页面上的所有图形元素。
3. **访问方法**：在第一页上调用 `Visit` 方法，允许 `GraphicsAbsorber` 吸收矢量图形。
4. **遍历提取的元素**：代码循环遍历每个提取的元素，打印页面编号、位置和涉及的绘图操作数量等信息。

## 2. 移动图形<a name="moving-graphics"></a>

一旦提取了图形，您可以将它们移动到同一页面上的不同位置。以下是实现此操作的方法：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Move graphics by shifting their X and Y coordinates
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "MoveGraphics_out.pdf");
        }
    }
}
```

### 关键点：

- **SuppressUpdate**：此方法暂时暂停更新，以提高进行多次更改时的性能。
- **ResumeUpdate**：此方法恢复更新并应用对图形位置所做的更改。
- **元素定位**：通过更改每个图形的 `X` 和 `Y` 坐标来调整其位置。

## 3. 删除图形<a name="removing-graphics"></a>

在某些情况下，您可能希望从页面中删除特定图形。Aspose.PDF 提供了两种方法来实现这一点：

### 方法 1：使用矩形边界

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suppress updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove those inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                if (rectangle.Contains(element.Position))
                {
                    element.Remove(); // Remove the graphic element
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### 方法 2：使用已删除元素的集合

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection to store the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Iterate through the extracted elements and add those inside the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the graphics elements from the page
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### 说明：

- **矩形边界**：定义一个矩形区域以指定要删除的图形。
- **暂停和恢复更新**：确保高效删除而不进行中间渲染。

## 4. 将图形添加到另一页面<a name="adding-graphics"></a>

从一个页面吸收的图形可以添加到同一文档中的另一页面。以下是实现此操作的两种方法：

### 方法 1：单独添加图形

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### 方法 2：作为集合添加图形

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics elements to the second page at once
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### 关键点：

- **SuppressUpdate 和 ResumeUpdate**：这些方法有助于在进行批量更改时保持性能。
- **AddOnPage 与 AddGraphics**：使用 `AddOnPage` 进行单个添加，使用 `AddGraphics` 进行批量添加。

## 结论

在本章中，我们探讨了如何使用 `GraphicsAbsorber` 类提取、移动、删除和添加 PDF 文档中的矢量图形，使用 Aspose.PDF。通过掌握这些技术，您可以显著增强 PDF 的视觉呈现，创建动态且视觉吸引人的文档。

欢迎您尝试代码示例并将其调整为您的特定用例。祝您编码愉快！

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