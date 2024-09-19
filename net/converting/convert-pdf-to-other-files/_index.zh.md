---
title: 将 PDF 转换为 EPUB、LaTeX、文本、XPS 在 C#
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: 转换, PDF, EPUB, LaTeX, 文本, XPS, C#
description: 本主题向您展示如何使用 C# 或 .NET 将 PDF 文件转换为其他文件格式，如 EPUB、LaTeX、文本、XPS 等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将 PDF 转换为 EPUB

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for .NET 为您呈现在线免费应用程序 ["PDF 到 EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序转换 PDF 为 EPUB](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="电子出版">EPUB</abbr>** 是来自国际数字出版论坛 (IDPF) 的一个免费开放的电子书标准。
**<abbr title="电子出版物">EPUB</abbr>** 是国际数字出版论坛（IDPF）推出的一个免费开放的电子书标准。
EPUB 设计用于可重排内容，意味着 EPUB 阅读器可以为特定的显示设备优化文本。EPUB 也支持固定布局内容。该格式旨在作为出版商和转换公司内部使用的单一格式，同时也用于分销和销售。它取代了开放电子书标准。

下面的代码片段也可以与 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库一起使用。

Aspose.PDF for .NET 还支持将 PDF 文档转换为 EPUB 格式的功能。Aspose.PDF for .NET 有一个名为 EpubSaveOptions 的类，可以用作 [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法的第二个参数，生成 EPUB 文件。
请尝试使用以下代码片段以 C# 实现此需求。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 加载 PDF 文档
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// 实例化 Epub 保存选项
EpubSaveOptions options = new EpubSaveOptions();
// 指定内容布局
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// 保存 ePUB 文档
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for .NET** 支持将 PDF 转换为 LaTeX/TeX。
LaTeX 文件格式是一种带有特殊标记的文本文件格式，在基于 TeX 的文档准备系统中用于高质量排版。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for .NET 为您提供免费在线应用程序 ["PDF 到 LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以在此尝试探索其功能和工作质量。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

要将 PDF 文件转换为 TeX，Aspose.PDF 提供了 [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) 类，该类提供了 OutDirectoryPath 属性，用于在转换过程中保存临时图片。

以下代码片段展示了使用 C# 将 PDF 文件转换为 TEX 格式的过程。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 创建 Document 对象
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// 实例化 LaTex 保存选项          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// 指定输出目录
string pathToOutputDirectory = dataDir;

// 为保存选项对象设置输出目录路径
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// 将 PDF 文件保存为 LaTex 格式           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## 将 PDF 转换为文本

**Aspose.PDF for .NET** 支持将整个 PDF 文档和单页转换为文本文件。

### 将整个 PDF 文档转换为文本文件

您可以使用 [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber) 类的 [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) 方法将 PDF 文档转换为 TXT 文件。

以下代码片段说明了如何提取所有页面的文本。

```csharp
public static void ConvertPDFDocToTXT()
{
    // 打开文档
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // 将提取的文本保存在文本文件中
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**尝试在线转换 PDF 到文本**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以在此尝试探索功能和它的工作质量。
Aspose.PDF for .NET 为您提供在线免费应用程序 [“PDF 转文本”](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换 PDF 到文本的免费应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)

### 将 PDF 页面转换为文本文件

您可以使用 Aspose.PDF for .NET 将 PDF 文档转换为 TXT 文件。您应该使用 `TextAbsorber` 类的 `Visit` 方法来解决这个任务。

以下代码片段解释了如何从特定页面提取文本。

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // 将提取的文本保存在文本文件中
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## 将 PDF 转换为 XPS

**Aspose.PDF for .NET** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用提供的代码片段，用 C# 将 PDF 文件转换为 XPS 格式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for .NET 为您提供了免费的在线应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与 Microsoft Corporation 的 XML Paper Specification 相关。XML Paper Specification (XPS)，之前被称为 Metro 并包括 Next Generation Print Path (NGPP) 营销概念，是 Microsoft 将文档创建和查看整合到 Windows 操作系统中的一项举措。

要将 PDF 文件转换为 XPS，Aspose.PDF 有一个类 [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions)，它被用作 [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法的第二个参数，以生成 XPS 文件。
要将PDF文件转换为XPS，Aspose.PDF提供了[XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions)类，该类作为[Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)方法的第二个参数，用于生成XPS文件。

以下代码片段展示了将PDF文件转换为XPS格式的过程。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 加载PDF文档
Document pdfDocument = new Document(dataDir + "input.pdf");

// 实例化XPS保存选项
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// 保存XPS文档
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
