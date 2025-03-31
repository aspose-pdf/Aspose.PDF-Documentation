---
title: 在 .NET 中将 HTML 转换为 PDF
linktitle: 将 HTML 转换为 PDF 文件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: 本主题向您展示如何使用 Aspose.PDF 将 HTML 和 MHTML 转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "Aspose.PDF for .NET 中的转换功能允许将 HTML 和 MHTML 文档无缝转换为高质量的 PDF 文件。通过高级自定义选项，用户可以控制字体嵌入、媒体查询和外部资源管理，同时确保网页或本地 HTML 文件准确地呈现为 PDF 格式，并根据其特定需求进行灵活调整。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 概述 

本文解释了如何使用 **C# 将 HTML 转换为 PDF**。它涵盖以下主题。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

_格式_: **HTML**
- [C# HTML 转 PDF](#csharp-html-to-pdf)
- [C# 将 HTML 转换为 PDF](#csharp-html-to-pdf)
- [C# 如何将 HTML 转换为 PDF](#csharp-html-to-pdf)

_格式_: **MHTML**
- [C# MHTML 转 PDF](#csharp-mhtml-to-pdf)
- [C# 将 MHTML 转换为 PDF](#csharp-mhtml-to-pdf)
- [C# 如何将 MHTML 转换为 PDF](#csharp-mhtml-to-pdf)

_格式_: **网页**
- [C# 网页转 PDF](#csharp-webpage-to-pdf)
- [C# 将网页转换为 PDF](#csharp-webpage-to-pdf)
- [C# 如何将网页转换为 PDF](#csharp-webpage-to-pdf)

## C# HTML 转 PDF 转换

**Aspose.PDF for .NET** 是一个 PDF 操作 API，允许您无缝地将任何现有的 HTML 文档转换为 PDF。将 HTML 转换为 PDF 的过程可以灵活自定义。

## 将 HTML 转换为 PDF

以下 C# 代码示例演示了如何将 HTML 文档转换为 PDF。

<a name="csharp-html-to-pdf"><strong>步骤：在 C# 中将 HTML 转换为 PDF</strong></a>

1. 创建 [HtmlLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions/) 类的实例。
2. 初始化 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/) 对象。
3. 通过调用 **Document.Save()** 方法保存输出 PDF 文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**尝试在线将 HTML 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 HTML 转换为 PDF](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## 从 HTML 转 PDF 的高级转换

HTML 转换引擎有几个选项，允许我们控制转换过程。

### 媒体查询支持

媒体查询是一种流行的技术，用于向不同设备提供定制的样式表。我们可以使用 [`HtmlMediaType`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype) 属性设置设备类型。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### 启用（禁用）字体嵌入

HTML 页面通常使用字体（例如来自本地文件夹的字体、Google Fonts 等）。我们还可以使用 [`IsEmbedFonts`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions/properties/isembedfonts) 属性控制文档中字体的嵌入。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### 管理外部资源加载

转换引擎提供了一种机制，允许您控制与 HTML 文档相关的某些资源的加载。
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions) 类具有属性 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)，通过该属性我们可以定义资源加载器的行为。
假设我们需要将所有 PNG 图像替换为单个图像 `test.jpg`，并将其他资源的外部 URL 替换为内部 URL。
为此，我们可以定义一个自定义加载器 `SamePictureLoader` 并将 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) 指向该名称。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## 将网页转换为 PDF

将网页转换与将本地 HTML 文档转换略有不同。为了将网页内容转换为 PDF 格式，我们可以首先使用 HttpClient 实例获取 HTML 页面内容，创建 Stream 对象，将内容传递给 Document 对象，并以 PDF 格式呈现输出。

在将托管在 Web 服务器上的网页转换为 PDF 时：

<a name="csharp-webpage-to-pdf"><strong>步骤：在 C# 中将网页转换为 PDF</strong></a>

1. 使用 HttpClient 对象读取页面内容。
1. 实例化 [HtmlLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions) 对象并设置基本 URL。
1. 初始化 Document 对象，同时传递流对象。
1. 可选地，设置页面大小和/或方向。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### 提供凭据进行网页到 PDF 的转换

有时我们需要执行需要身份验证和访问权限的 HTML 文件转换，以便只有经过身份验证的用户才能获取页面内容。这还包括某些资源/数据在 HTML 中引用的场景，这些资源/数据从某个外部服务器获取，需要身份验证。为满足此要求，[`HtmlLoadOptions`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions) 类中添加了 [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/zh/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) 属性。以下代码片段显示了在将 HTML 文件转换为 PDF 时传递凭据以请求 HTML 及其相关资源的步骤。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### 在单个页面中呈现所有 HTML 内容

Aspose.PDF for .NET 提供了在将 HTML 文件转换为 PDF 格式时在单个页面上呈现所有内容的能力。例如，如果您有一些 HTML 内容，其输出大小大于一页，您可以使用选项将输出数据呈现为单个 PDF 页面。为使用此选项，HtmlLoadOptions 类通过 IsRenderToSinglePage 标志进行了扩展。以下代码片段显示了如何使用此功能。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### 使用 SVG 数据呈现 HTML

Aspose.PDF for .NET 提供了将 HTML 页面转换为 PDF 文档的能力。由于 HTML 允许将 SVG 图形元素作为标签添加到页面中，Aspose.PDF 也支持将此类数据转换为生成的 PDF 文件。以下代码片段显示了如何将带有 SVG 图形标签的 HTML 文件转换为标记 PDF 文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## 将 MHTML 转换为 PDF 

{{% alert color="success" %}}
**尝试在线将 MHTML 转换为 PDF**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 MHTML 转换为 PDF](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME 封装的聚合 HTML 文档">MHTML</abbr>，即 MIME HTML，是一种网页归档格式，用于将通常由外部链接（如图像、Flash 动画、Java 小程序和音频文件）表示的资源与 HTML 代码组合成一个文件。MHTML 文件的内容被编码为 HTML 电子邮件消息的形式，使用 MIME 类型 multipart/related。Aspose.PDF for .NET 可以将 HTML 文件转换为 PDF 格式，并且随着 Aspose.PDF for .NET 9.0.0 的发布，我们引入了一项新功能，允许您将 MHTML 文件转换为 PDF 格式。以下代码片段显示了如何使用 C# 将 MHTML 文件转换为 PDF 格式：

<a name="csharp-mhtml-to-pdf"><strong>步骤：在 C# 中将 MHTML 转换为 PDF</strong></a>

1. 创建 [MhtLoadOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/mhtloadoptions/) 类的实例。
2. 初始化 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/) 对象。
3. 通过调用 **Document.Save()** 方法保存输出 PDF 文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## 另请参阅 

本文还涵盖了以下主题。代码与上述相同。

_格式_: **HTML**
- [C# HTML 转 PDF 代码](#csharp-html-to-pdf)
- [C# HTML 转 PDF API](#csharp-html-to-pdf)
- [C# 以编程方式将 HTML 转 PDF](#csharp-html-to-pdf)
- [C# HTML 转 PDF 库](#csharp-html-to-pdf)
- [C# 将 HTML 保存为 PDF](#csharp-html-to-pdf)
- [C# 从 HTML 生成 PDF](#csharp-html-to-pdf)
- [C# 从 HTML 创建 PDF](#csharp-html-to-pdf)
- [C# HTML 转 PDF 转换器](#csharp-html-to-pdf)

_格式_: **MHTML**
- [C# MHTML 转 PDF 代码](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF API](#csharp-mhtml-to-pdf)
- [C# 以编程方式将 MHTML 转 PDF](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF 库](#csharp-mhtml-to-pdf)
- [C# 将 MHTML 保存为 PDF](#csharp-mhtml-to-pdf)
- [C# 从 MHTML 生成 PDF](#csharp-mhtml-to-pdf)
- [C# 从 MHTML 创建 PDF](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF 转换器](#csharp-mhtml-to-pdf)

_格式_: **网页**
- [C# 网页转 PDF 代码](#csharp-webpage-to-pdf)
- [C# 网页转 PDF API](#csharp-webpage-to-pdf)
- [C# 以编程方式将网页转 PDF](#csharp-webpage-to-pdf)
- [C# 网页转 PDF 库](#csharp-webpage-to-pdf)
- [C# 将网页保存为 PDF](#csharp-webpage-to-pdf)
- [C# 从网页生成 PDF](#csharp-webpage-to-pdf)
- [C# 从网页创建 PDF](#csharp-webpage-to-pdf)
- [C# 网页转 PDF 转换器](#csharp-webpage-to-pdf)