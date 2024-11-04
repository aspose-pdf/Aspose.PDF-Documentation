---
title: 设置现有 PDF 的 XMP 元数据
type: docs
weight: 20
url: /net/set-xmp-metadata-of-an-existing-pdf/
description: 本节解释如何使用 Aspose.PDF Facades 设置现有 PDF 的 XMP 元数据。
lastmod: "2021-06-05"
draft: false
---

为了在 PDF 文件中设置 XMP 元数据，您需要创建 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定 PDF 文件。 您可以使用 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 类的 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) 方法添加不同的属性。最后，调用 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法。以下代码片段向您展示如何在 PDF 文件中添加 XMP 元数据。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// 创建 PdfXmpMetadata 对象
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// 绑定 PDF 文件到对象
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// 添加创建日期
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// 更改元数据日期
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// 添加创建工具
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Creator tool name");

// 移除修改日期
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// 添加用户定义属性
// 步骤 #1: 注册命名空间前缀和 URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// 步骤 #2: 使用前缀添加用户属性
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// 更改用户定义属性
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// 将 xmp 元数据保存到 PDF 文件中
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// 关闭对象
xmpMetaData.Close();
```