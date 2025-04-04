---
title: 将 PDF 转换为 HTML 在 .NET 中
linktitle: 将 PDF 转换为 HTML 格式
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 本主题向您展示如何使用 Aspose.PDF C# 库将 PDF 文件转换为 HTML 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "介绍了 Aspose.PDF for .NET 中的一个强大新功能，使 PDF 文档无缝转换为 HTML 格式。此功能支持多页输出、SVG 图像管理和透明文本渲染选项，使开发人员能够仅用几行 C# 代码轻松将 PDF 转换为适合网页的内容。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1060",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 概述

本文解释了如何 **使用 C# 将 PDF 转换为 HTML**。它涵盖了以下主题。

- [将 PDF 转换为 HTML](#csharp-pdf-to-html)

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 将 PDF 转换为 HTML

**Aspose.PDF for .NET** 提供了许多将各种文件格式转换为 PDF 文档以及将 PDF 文件转换为各种输出格式的功能。本文讨论了如何将 PDF 文件转换为 <abbr title="超文本标记语言">HTML</abbr>。Aspose.PDF for .NET 提供了使用 InLineHtml 方法将 HTML 文件转换为 PDF 格式的能力。我们收到了许多关于将 PDF 文件转换为 HTML 格式的功能请求，并提供了此功能。请注意，此功能还支持 XHTML 1.0。

**Aspose.PDF for .NET** 支持将 PDF 文件转换为 HTML 的功能。您可以使用 Aspose.PDF 库完成的主要任务如下：

- 将 PDF 转换为 HTML。
- 将输出拆分为多页 HTML。
- 指定存储 SVG 文件的文件夹。
- 在转换过程中压缩 SVG 图像。
- 将图像保存为 PNG 背景。
- 指定图像文件夹。
- 仅创建包含主体内容的后续文件。
- 透明文本渲染。
- PDF 文档层渲染。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 HTML**

Aspose.PDF for .NET 为您提供了在线免费应用程序 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以尝试探索其功能和质量。

[![Aspose.PDF 将 PDF 转换为 HTML 的免费应用](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET 提供了两行代码来将源 PDF 文件转换为 HTML。[`SaveFormat 枚举`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/saveformat) 包含值 Html，允许您将源文件保存为 HTML。以下代码片段展示了将 PDF 文件转换为 HTML 的过程。

<a name="csharp-pdf-to-html" id="cshart-pdf-to-html"><strong>将 PDF 转换为 HTML</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/) 对象的实例，使用源 PDF 文档。
2. 通过调用 **Document.Save()** 方法将其保存为 **SaveFormat.Html** 格式。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### 将输出拆分为多页 HTML

在将大型 PDF 文件转换为 HTML 格式时，输出会显示为单个 HTML 页面。这可能会变得非常长。为了控制页面大小，可以在 PDF 转换为 HTML 时将输出拆分为多个页面。请尝试使用以下代码片段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### 指定存储 SVG 文件的文件夹

在 PDF 转换为 HTML 的过程中，可以指定 SVG 图像应保存到的文件夹。使用 [`HtmlSaveOption 类`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlsaveoptions) [`SpecialFolderForSvgImages 属性`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages) 来指定特殊的 SVG 图像目录。此属性获取或设置在转换过程中遇到时 SVG 图像必须保存到的目录路径。如果参数为空或为 null，则任何 SVG 文件将与其他图像文件一起保存。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### 在转换过程中压缩 SVG 图像

要在 PDF 转换为 HTML 的过程中压缩 SVG 图像，请尝试使用以下代码：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### 将图像保存为 PNG 背景

保存图像的默认输出格式为 SVG。在转换过程中，PDF 中的一些图像会转换为 SVG 矢量图像。这可能会很慢。相反，图像可以转换为每页一个 PNG 背景文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### 指定图像文件夹

我们还可以指定在 PDF 转换为 HTML 的过程中图像将保存到的文件夹：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### 仅创建包含主体内容的后续文件

最近，我们被要求引入一个功能，将 PDF 文件转换为 HTML，用户可以仅获取每页的 `<body>` 标签内容。这将生成一个包含 CSS、`<html>`、`<head>` 细节的文件，其他文件仅包含 `<body>` 内容。

为满足此要求，HtmlSaveOptions 类引入了一个新属性 HtmlMarkupGenerationMode。

使用以下简单代码片段，您可以将输出 HTML 拆分为页面。在输出页面中，所有 HTML 对象必须准确放置在它们现在的位置（字体处理和输出、CSS 创建和输出、图像创建和输出），除了输出 HTML 将包含当前放置在标签内的内容（现在将省略“body”标签）。但是，使用此方法时，CSS 的链接由您的代码负责，因为像这样的内容将被剥离。为此，您可以通过 File.ReadAllText() 读取 CSS，并通过 AJAX 发送到将由 jQuery 应用的网页。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### 透明文本渲染

如果源/输入 PDF 文件包含被前景图像遮挡的透明文本，则可能会出现文本渲染问题。因此，为了应对这种情况，可以使用 SaveShadowedTextsAsTransparentTexts 和 SaveTransparentTexts 属性。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### PDF 文档层渲染

我们可以在 PDF 转换为 HTML 的过程中将 PDF 文档层渲染为单独的层类型元素：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```