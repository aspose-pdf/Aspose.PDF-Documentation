---
title: 将 PDF 转换为 PDF/A 格式
linktitle: 将 PDF 转换为 PDF/A 格式
type: docs
weight: 100
url: zh/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: 本主题展示了如何使用 Aspose.PDF 将 PDF 文件转换为符合 PDF/A 的 PDF 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for .NET** 允许您将 PDF 文件转换为符合 <abbr title="Portable Document Format / A">PDF/A</abbr> 的 PDF 文件。在此之前，必须验证文件。本主题将进行说明。

{{% alert color="primary" %}}

请注意，我们遵循 Adobe Preflight 来验证 PDF/A 的一致性。市场上所有工具都有自己的“表示”PDF/A一致性。请参考此文章关于 PDF/A 验证工具。我们选择 Adobe 产品来验证 Aspose.PDF 如何生成 PDF 文件，因为 Adobe 是与 PDF 相关的一切的核心。

{{% /alert %}}

使用 Document 类的 Convert 方法转换文件。
{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for .NET 为您提供免费在线应用程序 ["PDF 转 PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以在此尝试探索其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 PDF/A 的免费应用](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## 将 PDF 文件转换为 PDF/A-1b

以下代码片段展示了如何将 PDF 文件转换为符合 PDF/A-1b 的 PDF。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 打开文档
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// 转换为符合 PDF/A 的文档
// 在转换过程中，也执行了验证
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// 保存输出文档
pdfDocument.Save(dataDir);
```

要仅执行验证，请使用以下代码行：

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 打开文档
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// 验证 PDF 是否符合 PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## 将 PDF 文件转换为 PDF/A-3b

Aspose.PDF for .NET 也支持将 PDF 文件转换为 PDF/A-3b 格式的功能。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 打开文档
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// 保存输出文档
pdfDocument.Save(dataDir);
```
## 将PDF文件转换为PDF/A-2u格式

Aspose.PDF for .NET也支持将PDF文件转换为PDF/A-2u格式的功能。

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## 将PDF文件转换为PDF/A-3u格式

Aspose.PDF for .NET也支持将PDF文件转换为PDF/A-3u格式的功能。

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## 向PDF/A文件添加附件

如果您需要向PDF/A合规格式的文件中添加文件，则我们推荐使用Aspose.PDF.PdfFormat枚举中的PDF_A_3A值。
PDF/A_3a是一种格式，它提供了将任何文件格式作为附件添加到PDF/A合规文件的功能。

```csharp
## 替换缺失字体为其他字体

根据PDFA标准，字体应嵌入PDFA文档中。

```csharp
// 对于完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 实例化Document实例以加载现有文件
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// 设置新文件添加为附件
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "大图片文件");
// 将附件添加到文档的附件集合中
doc.EmbeddedFiles.Add(fileSpecification);
// 执行转换到PDF/A_3a，以便将附件包含在结果文件中
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// 保存结果文件
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```
根据PDFA标准，字体应嵌入PDFA文档中。

```csharp
// 如需完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // 目标机器上缺少字体
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
