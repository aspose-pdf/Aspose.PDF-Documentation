---
title: 获取和设置页面属性
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /zh/net/get-and-set-page-properties/
description: 学习如何使用 Aspose.PDF for .NET 获取和设置 PDF 文档的页面属性，以实现自定义文档格式。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "Aspose.PDF for .NET 中的获取和设置页面属性功能使开发人员能够轻松访问和操作 PDF 页面属性。此功能允许用户检索关键信息，例如页面计数和特定属性，如颜色类型、媒体框和修剪框，所有这些只需几行代码。通过利用此强大功能，今天就增强您的 PDF 文档管理能力，以便在 .NET 应用程序中高效操作 PDF。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分，适合高级用户和开发人员。"
}
</script>

Aspose.PDF for .NET 让您在 .NET 应用程序中读取和设置 PDF 文件中页面的属性。本节展示了如何获取 PDF 文件中的页面数量，获取有关 PDF 页面属性的信息，例如颜色，并设置页面属性。给出的示例是 C# 语言，但您可以使用任何 .NET 语言，例如 VB.NET 来实现相同的功能。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 获取 PDF 文件中的页面数量

在处理文档时，您通常想知道它们包含多少页。使用 Aspose.PDF，这只需两行代码。

要获取 PDF 文件中的页面数量：

1. 使用 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 类打开 PDF 文件。
1. 然后使用 [PageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pagecollection) 集合的 Count 属性（来自 Document 对象）获取文档中的总页面数。

以下代码片段展示了如何获取 PDF 文件的页面数量。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### 在不保存文档的情况下获取页面计数

有时我们会动态生成 PDF 文件，在创建 PDF 文件时，可能会遇到需求（创建目录等）需要在不将文件保存到系统或流中的情况下获取 PDF 文件的页面计数。因此，为了满足这一需求，在 Document 类中引入了一个方法 [ProcessParagraphs](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/processparagraphs)。请查看以下代码片段，展示了如何在不保存文档的情况下获取页面计数的步骤。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## 获取页面属性

PDF 文件中的每个页面都有多个属性，例如宽度、高度、出血框、裁剪框和修剪框。Aspose.PDF 允许您访问这些属性。

### **理解页面属性：Artbox、BleedBox、CropBox、MediaBox、TrimBox 和 Rect 属性之间的区别**

- **媒体框**：媒体框是最大的页面框。它对应于在将文档打印为 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、美国信纸等）。换句话说，媒体框决定了 PDF 文档显示或打印的介质的物理大小。
- **出血框**：如果文档有出血，PDF 也会有出血框。出血是指超出页面边缘的颜色（或艺术作品）量。它用于确保在打印文档并裁剪到大小（“修剪”）时，墨水会一直延伸到页面的边缘。即使页面被错误修剪 - 稍微偏离修剪标记 - 页面上也不会出现白边。
- **修剪框**：修剪框指的是文档在打印和修剪后最终的大小。
- **艺术框**：艺术框是围绕文档中页面实际内容绘制的框。此页面框在将 PDF 文档导入其他应用程序时使用。
- **裁剪框**：裁剪框是您的 PDF 文档在 Adobe Acrobat 中显示的“页面”大小。在正常视图中，只有裁剪框的内容会在 Adobe Acrobat 中显示。
  有关这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页面边界。
- **Page.Rect**：媒体框和出血框的交集（通常可见的矩形）。下图说明了这些属性。

有关更多详细信息，请访问 [此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

### **访问页面属性**

[Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 类提供与特定 PDF 页面相关的所有属性。PDF 文件的所有页面都包含在 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象的 [PageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pagecollection) 集合中。

从那里，可以使用索引访问单个 Page 对象，或使用 foreach 循环遍历集合以获取所有页面。一旦访问了单个页面，我们可以获取其属性。以下代码片段展示了如何获取页面属性。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## 获取 PDF 文件的特定页面

Aspose.PDF 允许您 [将 PDF 拆分为单个页面](/pdf/zh/net/split-pdf-document/) 并将其保存为 PDF 文件。获取 PDF 文件中的指定页面并将其保存为新 PDF 是一个非常相似的操作：打开源文档，访问页面，创建新文档并将页面添加到此文档中。

[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象的 [PageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pagecollection) 保存 PDF 文件中的页面。要从此集合中获取特定页面：

1. 使用 Pages 属性指定页面索引。
1. 创建一个新的 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象。
1. 将 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象添加到新的 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象中。
1. 使用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf.document/save/methods/4) 方法保存输出。

以下代码片段展示了如何从 PDF 文件中获取特定页面并将其保存为新文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## 确定页面颜色

[Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 类提供与 PDF 文档中特定页面相关的属性，包括页面使用的颜色类型 - RGB、黑白、灰度或未定义。

PDF 文件的所有页面都包含在 [PageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pagecollection) 集合中。ColorType 属性指定页面上元素的颜色。要获取或确定特定 PDF 页面的颜色信息，请使用 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象的 [ColorType](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page/properties/colortype) 属性。

以下代码片段展示了如何遍历 PDF 文件的每个页面以获取颜色信息。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
        }
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