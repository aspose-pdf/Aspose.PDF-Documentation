---
title: 在 .NET 中将 HTML 转换为 PDF
linktitle: 将 HTML 转换为 PDF 文件
type: docs
weight: 40
url: /net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: 本主题介绍如何使用 Aspose.PDF 将 HTML 转换为 PDF 和 MHTML 转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
## 概览

本文介绍如何**使用 C# 将 HTML 转换为 PDF**。它涵盖以下主题。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

格式：**HTML**
- [C# HTML 转 PDF](#csharp-html-to-pdf)
- [C# 将 HTML 转换为 PDF](#csharp-html-to-pdf)
- [C# 如何将 HTML 转换为 PDF](#csharp-html-to-pdf)

格式：**MHTML**
- [C# MHTML 转 PDF](#csharp-mhtml-to-pdf)
- [C# 将 MHTML 转换为 PDF](#csharp-mhtml-to-pdf)
- [C# 如何将 MHTML 转换为 PDF](#csharp-mhtml-to-pdf)

格式：**网页**
- [C# 网页转 PDF](#csharp-webpage-to-pdf)
- [C# 将网页转换为 PDF](#csharp-webpage-to-pdf)
- [C# 如何将网页转换为 PDF](#csharp-webpage-to-pdf)

## C# HTML 转 PDF 转换
## C# HTML 转 PDF 转换

**Aspose.PDF for .NET** 是一个PDF操作API，它可以让您无缝地将任何现有的HTML文档转换为PDF。HTML转PDF的过程可以灵活定制。

## 转换HTML为PDF

以下C#代码示例展示了如何将HTML文档转换为PDF。

<a name="csharp-html-to-pdf"><strong>步骤：在C#中转换HTML为PDF</strong></a>

1. 创建 [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/) 类的实例。
2. 初始化 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 对象。
3. 通过调用 **Document.Save()** 方法保存输出的PDF文档。

```csharp
public static void ConvertHTMLtoPDF()
{
    HtmlLoadOptions options= new HtmlLoadOptions();
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

{{% alert color="success" %}}
**尝试在线转换HTML为PDF**

Aspose为您提供了在线免费应用["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)，您可以在此尝试探索其功能和工作质量。
{{% /alert %}}

[![Aspose.PDF 转换 HTML 到 PDF 使用免费应用](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)

## 高级 HTML 到 PDF 转换

HTML 转换引擎具有多个选项，允许我们控制转换过程。

### 媒体查询支持

媒体查询是一种流行的技术，用于向不同设备提供定制的样式表。我们可以使用 [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype) 属性设置设备类型。

```csharp
public static void ConvertHTMLtoPDFAdvanced_MediaType()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        // 设置打印或屏幕模式
        HtmlMediaType = HtmlMediaType.Print
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```
### 启用（禁用）字体嵌入

HTML 页面通常使用字体（例如来自本地文件夹的字体、Google 字体等）。我们还可以使用[`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts)属性控制文档中的字体嵌入。

```csharp
public static void ConvertHTMLtoPDFAdvanced_EmbedFonts()
{
    // 禁用字体嵌入
    HtmlLoadOptions options = new HtmlLoadOptions {IsEmbedFonts = false};
    Document pdfDocument= new Document(_dataDir + "test_fonts.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

### 管理外部资源加载

转换引擎提供了一种机制，允许您控制与HTML文档相关的某些资源的加载。
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 类具有属性 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)，我们可以定义资源加载器的行为。
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 类具有属性 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)，我们可以通过它定义资源加载器的行为。
假设我们需要将所有 PNG 图像替换为单个图像 `test.jpg` 并将外部 URL 替换为内部资源。
为此，我们可以定义一个自定义加载器 `SamePictureLoader` 并将 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) 指向这个名称。

```csharp
public static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(_dataDir + "test.jpg");
        result = new LoadOptions.ResourceLoadingResult(resultBytes)
        {
            //设置 MIME 类型
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```
## 将网页转换为PDF

将网页转换为PDF与转换本地HTML文档略有不同。为了将网页内容转换为PDF格式，我们可以首先使用HttpClient实例获取HTML页面内容，创建Stream对象，将内容传递给Document对象并以PDF格式呈现输出。

将托管在网络服务器上的网页转换为PDF时：

<a name="csharp-webpage-to-pdf"><strong>步骤：在C#中将网页转换为PDF</strong></a>

1. 使用HttpClient对象读取页面内容。
1. 实例化[HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions)对象并设置基本URL。
1. 初始化Document对象，同时传递流对象。
1. 可选，设置页面大小和/或方向。

```csharp
public static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    const string url = "https://en.wikipedia.org/wiki/Aspose_API";
    // 设置页面大小为A3，方向为横向；   
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        PageInfo = {Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### 提供凭据的网页到PDF转换

有时我们需要执行需要认证和访问权限的HTML文件的转换，以便只有经过认证的用户才能获取页面内容。这也包括一些在HTML中引用的资源/数据需要从某个需要认证的外部服务器获取的情况，为了满足这一需求，[`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) 属性被添加到 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 类中。以下代码片段显示了在将HTML文件转换为PDF时传递凭据以请求HTML及其相应资源的步骤。

```csharp
public static void ConvertHTMLtoPDFAdvanced_Authorized()
{
    const string url = "http://httpbin.org/basic-auth/user1/password1";
    var credentials = new NetworkCredential("user1", "password1");
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        ExternalResourcesCredentials = credentials
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url, credentials), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### 在单页中渲染所有HTML内容

Aspose.PDF for .NET 提供了在将HTML文件转换为PDF格式时在单页上渲染所有内容的能力。例如，如果您有一些HTML内容，其输出大小超过一页，您可以使用将输出数据渲染到单个PDF页面的选项。为使用此选项，HtmlLoadOptions 类通过 IsRenderToSinglePage 标志进行了扩展。下面的代码片段展示了如何使用这个功能。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 初始化 HTMLLoadSave 选项
HtmlLoadOptions options = new HtmlLoadOptions();
// 设置渲染到单页属性
options.IsRenderToSinglePage = true;
// 加载文档
Document pdfDocument= new Document(dataDir + "HTMLToPDF.html", options);
// 保存
pdfDocument.Save(dataDir + "RenderContentToSamePage.pdf");
```

### 带SVG数据的渲染HTML
### 使用 SVG 数据渲染 HTML

Aspose.PDF for .NET 提供了将 HTML 页面转换为 PDF 文档的功能。由于 HTML 允许在页面中作为标签添加 SVG 图形元素，Aspose.PDF 也支持将此类数据转换为结果 PDF 文件。以下代码片段展示了如何将包含 SVG 图形标签的 HTML 文件转换为带标签的 PDF 文档。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 设置输入文件路径
string inFile = dataDir + "HTMLSVG.html";
// 设置输出文件路径
string outFile = dataDir + "RenderHTMLwithSVGData.pdf";
// 初始化 HtmlLoadOptions
HtmlLoadOptions options = new HtmlLoadOptions(Path.GetDirectoryName(inFile));
// 初始化 Document 对象
Document pdfDocument = new Document(inFile, options);
// 保存
pdfDocument.Save(outFile);
```

## 将 MHTML 转换为 PDF

{{% alert color="success" %}}
**尝试在线将 MHTML 转换为 PDF**
{{% /alert %}}

Aspose.PDF for .NET 为您提供免费的在线应用程序[“MHTML 到 PDF”](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)，您可以在此尝试探索其功能和工作质量。

[![Aspose.PDF 使用免费应用转换 MHTML 到 PDF](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)

<abbr title="MIME 封装的聚合 HTML 文档">MHTML</abbr>，即 MIME HTML 的简称，是一种网页存档格式，用于将通常通过外部链接表示的资源（如图片、Flash 动画、Java 小程序和音频文件）与 HTML 代码合并到一个文件中。
<abbr title="MIME封装的聚合HTML文档">MHTML</abbr>，即MIME HTML，是一种网页存档格式，用于将通常由外部链接（如图像、Flash动画、Java小程序和音频文件）表示的资源与HTML代码合并到一个文件中。

<a name="csharp-mhtml-to-pdf"><strong>步骤：在C#中将MHTML转换为PDF</strong></a>

1. 创建[MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/)类的实例。
2. 初始化[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)对象。
3. 通过调用**Document.Save()**方法保存输出的PDF文档。

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```

## 另见

本文还涵盖了这些主题。
这篇文章还涵盖了这些话题。

_格式_: **HTML**
- [C# HTML 转 PDF 代码](#csharp-html-to-pdf)
- [C# HTML 转 PDF API](#csharp-html-to-pdf)
- [C# HTML 转 PDF 编程方式](#csharp-html-to-pdf)
- [C# HTML 转 PDF 库](#csharp-html-to-pdf)
- [C# 将 HTML 保存为 PDF](#csharp-html-to-pdf)
- [C# 从 HTML 生成 PDF](#csharp-html-to-pdf)
- [C# 从 HTML 创建 PDF](#csharp-html-to-pdf)
- [C# HTML 转 PDF 转换器](#csharp-html-to-pdf)

_格式_: **MHTML**
- [C# MHTML 转 PDF 代码](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF API](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF 编程方式](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF 库](#csharp-mhtml-to-pdf)
- [C# 将 MHTML 保存为 PDF](#csharp-mhtml-to-pdf)
- [C# 从 MHTML 生成 PDF](#csharp-mhtml-to-pdf)
- [C# 从 MHTML 创建 PDF](#csharp-mhtml-to-pdf)
- [C# MHTML 转 PDF 转换器](#csharp-mhtml-to-pdf)

_格式_: **网页**
- [C# 网页转 PDF 代码](#csharp-webpage-to-pdf)
- [C# 网页转 PDF API](#csharp-webpage-to-pdf)
- [C# 网页转 PDF 编程方式](#csharp-webpage-to-pdf)
- [C# 将网页转换为PDF编程](#csharp-webpage-to-pdf)
- [C# 将网页转换为PDF库](#csharp-webpage-to-pdf)
- [C# 将网页保存为PDF](#csharp-webpage-to-pdf)
- [C# 从网页生成PDF](#csharp-webpage-to-pdf)
- [C# 从网页创建PDF](#csharp-webpage-to-pdf)
- [C# 网页到PDF转换器](#csharp-webpage-to-pdf)
