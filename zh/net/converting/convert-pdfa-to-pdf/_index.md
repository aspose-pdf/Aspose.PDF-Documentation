---
title: 将 PDF/A 转换为 PDF 格式
linktitle: 将 PDF/A 转换为 PDF 格式
type: docs
weight: 110
url: /zh/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: 本主题展示了如何使用 Aspose.PDF 将 PDF/A 文件转换为 .NET 库的 PDF 文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 将 PDF/A 文档转换为 PDF

将 PDF/A 文档转换为 PDF 意味着从原始文档中移除 <abbr title="便携式文档格式档案">PDF/A</abbr> 限制。
类 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 有方法 [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) 用于从输入/源文件中删除 PDF 符合性信息。

```csharp
public static void ConvertPDFAtoPDF()
{
    // 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // 移除 PDF/A 符合性信息
    pdfDocument.RemovePdfaCompliance();
    // 保存更新的文档
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
此信息也将在您对文档进行任何更改时删除（例如，添加页面）。在以下示例中，输出文档在添加页面后失去了 PDF/A 合规性。

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // 添加一个新的（空白）页面会删除 PDF/A 合规性信息。
    pdfDocument.Pages.Add();
    // 保存更新后的文档
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
