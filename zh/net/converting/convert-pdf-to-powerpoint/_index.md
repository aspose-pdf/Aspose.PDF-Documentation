---
title: 在 .NET 中将 PDF 转换为 PowerPoint
linktitle: 将 PDF 转换为 PowerPoint
type: docs
weight: 30
url: zh/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF 允许您使用 .NET 将 PDF 转换为 PPT (PowerPoint) 格式。其中一种方法是有可能将 PDF 转换为带有图像的幻灯片的 PPTX。
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概览

本文说明了如何**使用 C# 将 PDF 转换为 PowerPoint**。它涵盖了以下主题。

格式：**PPTX**
- [C# PDF 至 PPTX](#csharp-pdf-to-pptx)
- [C# 将 PDF 转换为 PPTX](#csharp-pdf-to-pptx)
- [C# 如何将 PDF 文件转换为 PPTX](#csharp-pdf-to-pptx)

格式：**PowerPoint**
- [C# PDF 至 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 将 PDF 转换为 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 如何将 PDF 文件转换为 PowerPoint](#csharp-pdf-to-powerpoint)

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## C# PDF 至 PowerPoint 和 PPTX 转换
## C# PDF 转 PowerPoint 和 PPTX 转换

**Aspose.PDF for .NET** 允许您跟踪 PDF 到 PPTX 转换的进度。

我们有一个名为 Aspose.Slides 的 API，它提供创建和操作 PPT/PPTX 演示文稿的功能。该 API 还提供将 PPT/PPTX 文件转换为 PDF 格式的功能。最近我们收到了许多客户的需求，支持 PDF 转换到 PPTX 格式的功能。从 Aspose.PDF for .NET 10.3.0 版本开始，我们引入了将 PDF 文档转换为 PPTX 格式的功能。在此转换过程中，PDF 文件的各个页面被转换为 PPTX 文件中的单独幻灯片。

在 PDF 到 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> 转换期间，文本被渲染为文本，您可以选择/更新它。
在PDF转换为<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>过程中，文本将以可选择/更新的文本形式呈现。

## 使用C#和Aspose.PDF .NET简单地将PDF转换为PowerPoint

为了将PDF转换为PPTX，建议使用Aspose.PDF for .NET的以下代码步骤。

<a name="csharp-pdf-to-powerpoint"><strong>步骤：在C#中将PDF转换为PowerPoint</strong></a> | <a name="csharp-pdf-to-pptx"><strong>步骤：在C#中将PDF转换为PPTX</strong></a>

1. 创建[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类的实例
2. 创建[PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)类的实例
3. 使用**Document**对象的**Save**方法将PDF保存为PPTX

```csharp
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 加载PDF文档
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// 实例化PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// 以PPTX格式保存输出
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## 将PDF转换为带图片的PPTX

{{% alert color="success" %}}
**尝试在线将PDF转换为PowerPoint**

Aspose.PDF for .NET为您提供免费的在线应用程序["PDF到PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 PPTX 的免费应用](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

如果您需要将可搜索的PDF转换为图片形式的PPTX，而不是可选择的文本，Aspose.PDF通过[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)类提供了这样的功能。要实现这一点，请将[PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)类的[SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages)属性设置为'true'，如下面的代码示例所示。

```csharp
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 加载PDF文档
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// 实例化PptxSaveOptions实例
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// 保存输出为PPTX格式
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## PPTX转换进度详情

Aspose.PDF for .NET允许您跟踪PDF到PPTX转换的进度。[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 类提供了 [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) 属性，可以指定为自定义方法来跟踪转换进度，如下代码示例所示。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 加载PDF文档
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// 实例化PptxSaveOptions实例
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//指定自定义进度处理器
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// 以PPTX格式保存输出
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
以下是自定义方法用于显示进度转换。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - 转换进度：{1}% 。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - 结果页的 {1} 于 {2} 布局已创建。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - 结果页 {1} 于 {2} 已导出。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - 源页面 {1} 于 {2} 已分析。", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    default:
        break;
}
```
## 另见

本文还涵盖了以下主题。代码与上述相同。

_格式_：**PowerPoint**
- [C# PDF 转 PowerPoint 代码](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint API](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint 编程方式](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint 库](#csharp-pdf-to-powerpoint)
- [C# 将 PDF 保存为 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 从 PDF 生成 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 从 PDF 创建 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint 转换器](#csharp-pdf-to-powerpoint)

_格式_：**PPTX**
- [C# PDF 转 PPTX 代码](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX API](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX 编程方式](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX 库](#csharp-pdf-to-pptx)
- [C# 将 PDF 保存为 PPTX](#csharp-pdf-to-pptx)
- [C# 从 PDF 生成 PPTX](#csharp-pdf-to-pptx)
- [C# 从 PDF 创建 PPTX](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX 转换器](#csharp-pdf-to-pptx)
