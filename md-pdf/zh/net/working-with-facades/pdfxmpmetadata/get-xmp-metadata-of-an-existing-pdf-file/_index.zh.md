---
title: 获取 PDF 文件的 XMP 元数据
type: docs
weight: 30
url: /net/get-xmp-metadata-of-an-existing-pdf-file/
description: 本节介绍如何使用 Aspose.PDF Facades 获取现有 PDF 的 XMP 元数据。
lastmod: "2021-06-05"
draft: false
---

为了从 PDF 文件中获取 XMP 元数据，您需要创建 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定 PDF 文件。您可以将特定的 XMP 元数据属性传递给 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 对象以获取它们的值。以下代码片段展示了如何从 PDF 文件中获取 XMP 元数据。

```csharp
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// 创建 PdfXmpMetadata 对象
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// 绑定 PDF 文件到对象
xmpMetaData.BindPdf( dataDir + "input.pdf");

// 获取 XMP 元数据属性
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```