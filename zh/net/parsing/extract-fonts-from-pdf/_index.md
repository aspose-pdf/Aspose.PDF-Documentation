---
title: 从 PDF 中提取字体 C#
linktitle: 从 PDF 中提取字体
type: docs
weight: 30
url: zh/net/extract-fonts-from-pdf/
description: 使用 Aspose.PDF for .NET 库从您的 PDF 文档中提取所有嵌入的字体。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

如果您想从 PDF 文档中获取所有字体，您可以使用 Document 类中提供的 FontUtilities.GetAllFonts() 方法。请查看以下代码片段，以从现有的 PDF 文档中获取所有字体：

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库一起使用。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

