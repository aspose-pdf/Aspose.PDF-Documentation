---
title: 使用 C# 格式化 PDF 文档
linktitle: 格式化 PDF 文档
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/formatting-pdf-document/
description: 使用 Aspose.PDF for .NET 创建和格式化 PDF 文档。使用下一个代码片段来解决您的任务。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "发现 Aspose.PDF for .NET 的强大新功能，允许用户无缝创建和格式化 PDF 文档。通过对文档属性（如窗口显示设置、字体嵌入选项和可自定义的缩放因子）进行全面控制，开发人员可以增强用户体验并维护文档在不同平台上的完整性。利用这一强大的功能优化您的 PDF 操作任务，显著提高 .NET 应用程序的效率。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "使用 Aspose.PDF for .NET 创建和格式化 PDF 文档。使用下一个代码片段来解决您的任务。"
}
</script>

## 格式化 PDF 文档

### 获取文档窗口和页面显示属性

本主题帮助您了解如何获取文档窗口、查看应用程序的属性，以及页面的显示方式。要设置这些属性：

使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类打开 PDF 文件。现在，您可以设置 Document 对象的属性，例如

- CenterWindow – 将文档窗口居中显示在屏幕上。默认值：false。
- Direction – 阅读顺序。这决定了页面在并排显示时的布局。默认值：从左到右。
- DisplayDocTitle – 在文档窗口标题栏中显示文档标题。默认值：false（显示标题）。
- HideMenuBar – 隐藏或显示文档窗口的菜单栏。默认值：false（显示菜单栏）。
- HideToolBar – 隐藏或显示文档窗口的工具栏。默认值：false（显示工具栏）。
- HideWindowUI – 隐藏或显示文档窗口元素，如滚动条。默认值：false（显示 UI 元素）。
- NonFullScreenPageMode – 文档在未以全页模式显示时的显示方式。
- PageLayout – 页面布局。
- PageMode – 文档首次打开时的显示方式。选项包括显示缩略图、全屏、显示附件面板。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

以下代码片段演示了如何使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类获取属性。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### 设置文档窗口和页面显示属性

本主题解释如何设置文档窗口、查看应用程序和页面显示的属性。要设置这些不同的属性：

1. 使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类打开 PDF 文件。
1. 设置 Document 对象的属性。
1. 使用 Save 方法保存更新后的 PDF 文件。

可用的属性有：

- CenterWindow。
- Direction。
- DisplayDocTitle。
- FitWindow。
- HideMenuBar。
- HideToolBar。
- HideWindowUI。
- NonFullScreenPageMode。
- PageLayout。
- PageMode。

每个属性在下面的代码中使用并描述。以下代码片段演示了如何使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类设置属性。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### 在现有 PDF 文件中嵌入字体

PDF 阅读器支持 [14 种核心字体](https://en.wikipedia.org/wiki/PDF#Text)，以便文档可以在不同平台上以相同的方式显示。当 PDF 包含不属于 14 种核心字体的字体时，请将字体嵌入 PDF 文件，以避免字体替换。

Aspose.PDF for .NET 支持在现有 PDF 文件中嵌入字体。您可以嵌入完整字体或字体的子集。要嵌入字体，请使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类打开 PDF 文件。然后使用 [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) 类将字体嵌入 PDF 文件。要嵌入完整字体，请使用 Font 类的 IsEmbeded 属性；要使用字体的子集，请使用 IsSubset 属性。

{{% alert color="primary" %}}

字体子集仅嵌入使用的字符，适用于短句或标语的情况，例如在徽标中使用公司字体，但不用于正文文本。使用子集可以减少输出 PDF 的文件大小。但是，如果正文文本使用自定义字体，请完整嵌入它。

{{% /alert %}}

以下代码片段演示了如何在 PDF 文件中嵌入字体。

### 嵌入标准类型 1 字体

某些 PDF 文档使用特殊的 Adobe 字体集中的字体。来自此集合的字体称为“标准类型 1 字体”。此集合包括 14 种字体，嵌入此类型的字体需要使用特殊标志，即 [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts)。以下是可以用于获取包含所有字体（包括标准类型 1 字体）的文档的代码片段：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### 创建 PDF 时嵌入字体

如果您需要使用 Adobe Reader 支持的 14 种核心字体以外的任何字体，则必须在生成 PDF 文件时嵌入字体描述。如果未嵌入字体信息，Adobe Reader 将从操作系统中获取字体（如果已安装），或者根据 PDF 中的字体描述构造替代字体。

> 请注意，嵌入的字体必须安装在主机机器上，即在以下代码中，“Univers Condensed”字体已安装在系统上。

我们使用 Font 类的 IsEmbedded 属性将字体信息嵌入 PDF 文件。将此属性的值设置为“True”将把完整的字体文件嵌入 PDF，尽管这会增加 PDF 文件的大小。以下是可以用于将字体信息嵌入 PDF 的代码片段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### 保存 PDF 时设置默认字体名称

当 PDF 文档包含在文档本身和设备上不可用的字体时，API 会用默认字体替换这些字体。当字体可用（已安装在设备上或嵌入到文档中）时，输出 PDF 应该具有相同的字体（不应替换为默认字体）。默认字体的值应包含字体的名称（而不是字体文件的路径）。我们实现了一个功能，可以在将文档保存为 PDF 时设置默认字体名称。以下代码片段可用于设置默认字体：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### 从 PDF 文档中获取所有字体

如果您想从 PDF 文档中获取所有字体，可以使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类提供的 FontUtilities.GetAllFonts() 方法。请查看以下代码片段以获取现有 PDF 文档中的所有字体：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### 获取字体替换的警告

Aspose.PDF for .NET 提供了获取字体替换通知的方法，以处理字体替换情况。以下代码片段展示了如何使用相应的功能。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

**OnFontSubstitution** 方法如下所示。

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### 使用 FontSubsetStrategy 改进字体嵌入

将字体作为子集嵌入的功能可以通过使用 IsSubset 属性来实现，但有时您希望将完全嵌入的字体集减少到文档中仅使用的子集。Aspose.Pdf.Document 具有 FontUtilities 属性，其中包括方法 SubsetFonts(FontSubsetStrategy subsetStrategy)。在 SubsetFonts() 方法中，参数 subsetStrategy 有助于调整子集策略。FontSubsetStrategy 支持以下两种字体子集变体。

- SubsetAllFonts - 这将子集化文档中使用的所有字体。
- SubsetEmbeddedFontsOnly - 这将仅子集化完全嵌入到文档中的字体。

以下代码片段演示了如何设置 FontSubsetStrategy：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### 获取-设置 PDF 文件的缩放因子

有时，您想确定 PDF 文档的当前缩放因子。使用 Aspose.Pdf，您可以找出当前值并设置一个。

[GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) 类的 Destination 属性允许您获取与 PDF 文件关联的缩放值。同样，它可以用于设置文件的缩放因子。

#### 设置缩放因子

以下代码片段演示了如何设置 PDF 文件的缩放因子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### 获取缩放因子

以下代码片段演示了如何获取 PDF 文件的缩放因子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### 设置打印对话框预设属性

Aspose.PDF 允许设置 PDF 文档的打印对话框预设属性。它允许您更改 PDF 文档的 DuplexMode 属性，默认设置为单面打印。这可以通过以下两种不同的方法实现。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### 使用 PDF 内容编辑器设置打印对话框预设属性

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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