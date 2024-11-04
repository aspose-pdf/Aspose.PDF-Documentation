---
title: 在 .NET 中将 PDF 转换为 HTML 
linktitle: 将 PDF 转换为 HTML 格式
type: docs
weight: 50
url: /net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 本主题演示如何使用 Aspose.PDF C# 库将 PDF 文件转换为 HTML 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概览

本文解释了如何**使用 C# 将 PDF 转换为 HTML**。它涵盖了以下主题。

_格式_：**HTML**
- [C# PDF 到 HTML](#csharp-pdf-to-html)
- [C# 将 PDF 转换为 HTML](#csharp-pdf-to-html)
- [C# 如何将 PDF 文件转换为 HTML](#csharp-pdf-to-html)

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## 将 PDF 转换为 HTML

**Aspose.PDF for .NET** 提供了许多功能，用于将各种文件格式转换为 PDF 文档以及将 PDF 文件转换为各种输出格式。
**Aspose.PDF for .NET** 提供了许多功能，用于将各种文件格式转换为 PDF 文档以及将 PDF 文件转换为各种输出格式。

**Aspose.PDF for .NET** 支持将 PDF 文件转换为 HTML 的功能。您可以使用 Aspose.PDF 库完成的主要任务包括：

- 将 PDF 转换为 HTML；
- 将输出拆分为多页 HTML；
- 指定用于存储 SVG 文件的文件夹；
- 在转换时压缩 SVG 图像；
- 指定图片文件夹；
- 仅创建包含正文内容的后续文件；
- 透明文本渲染；
- PDF 文档图层渲染。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 HTML**

Aspose.PDF for .NET 为您提供在线免费应用程序 [“PDF 到 HTML”](https://products.aspose.app/pdf/conversion/pdf-to-html)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 HTML 的免费应用](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET 提供了两行代码，用于将源 PDF 文件转换为 HTML。
Aspose.PDF for .NET 提供了一个两行代码，用于将源 PDF 文件转换为 HTML。

<a name="csharp-pdf-to-html"><strong>步骤：在 C# 中将 PDF 转换为 HTML</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 对象的实例。
2. 通过调用 **Document.Save()** 方法将其保存为 **SaveFormat.Html** 格式。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 打开源 PDF 文档
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// 将文件保存为 MS 文档格式
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### 将输出拆分为多页 HTML

当将包含多页的大型 PDF 文件转换为 HTML 格式时，输出显示为单个 HTML 页面。
将多页 PDF 文件转换为 HTML 格式时，输出显示为单个 HTML 页面。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 打开源 PDF 文档
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// 实例化 HTML 保存选项对象
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 指定将输出分成多个页面
htmlOptions.SplitIntoPages = true;

// 保存文档
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### 指定存储 SVG 文件的文件夹

在 PDF 转 HTML 转换过程中，可以指定应将 SVG 图像保存到的文件夹。
在 PDF 到 HTML 转换过程中，可以指定保存 SVG 图像的文件夹。

```csharp
// 加载 PDF 文件
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// 实例化 HTML 保存选项对象
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// 指定 PDF 到 HTML 转换过程中保存 SVG 图像的文件夹
newOptions.SpecialFolderForSvgImages = dataDir;

// 保存输出文件
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### 在转换过程中压缩 SVG 图像

在 PDF 到 HTML 转换期间压缩 SVG 图像，请尝试使用以下代码：

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 创建具有测试功能的 HtmlSaveOption
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// 如果有 SVG 图像，则压缩它们
newOptions.CompressSvgGraphicsIfAny = true;
```

### 指定图像文件夹

我们还可以指定在 PDF 到 HTML 转换期间将保存图像的文件夹：
我们还可以指定在PDF转换为HTML期间图片将保存到的文件夹：

```csharp
// 要获取完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 创建具有测试功能的HtmlSaveOption
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// 指定保存图片的单独文件夹
newOptions.SpecialFolderForAllImages = dataDir;
```

### 仅创建包含正文内容的后续文件

最近，我们被要求引入一个功能，其中PDF文件被转换为HTML，并且用户可以仅获取每个页面的`<body>`标签内容。这将生成一个包含CSS、`<html>`、`<head>`细节的文件，以及其他仅包含`<body>`内容的文件。

为了满足这一要求，HtmlSaveOptions类中引入了一个新属性，HtmlMarkupGenerationMode。

通过以下简单的代码片段，您可以将输出HTML分割为多个页面。
通过以下简单的代码片段，您可以将输出HTML分割成多个页面。

```csharp
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// 这是经过测试的设置
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### 透明文本渲染

如果源/输入的PDF文件包含由前景图像阴影的透明文本，则可能会出现文本渲染问题。因此，为了应对这种情况，可以使用SaveShadowedTextsAsTransparentTexts和SaveTransparentTexts属性。

```csharp
// 若要获取完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### PDF文档层渲染

我们可以在PDF到HTML转换期间，将PDF文档层渲染到单独的层类型元素中：

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// 实例化HTML SaveOptions对象
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 指定在输出HTML中单独渲染PDF文档层
htmlOptions.ConvertMarkedContentToLayers = true;

// 保存文档
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## 另见

本文还涵盖以下主题。代码与上面相同。

_格式_: **HTML**
- [C# PDF转HTML代码](#csharp-pdf-to-html)
- [C# PDF转HTML API](#csharp-pdf-to-html)
- [C# 以编程方式PDF转HTML](#csharp-pdf-to-html)
- [C# PDF转HTML库](#csharp-pdf-to-html)
- [C# 将PDF保存为HTML](#csharp-pdf-to-html)
- [C# 将PDF保存为HTML](#csharp-pdf-to-html)
- [C# 从PDF生成HTML](#csharp-pdf-to-html)
- [C# 从PDF创建HTML](#csharp-pdf-to-html)
- [C# PDF转HTML转换器](#csharp-pdf-to-html)
