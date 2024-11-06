---
title: PDFファイルのXMPメタデータを取得する
type: docs
weight: 30
url: ja/net/get-xmp-metadata-of-an-existing-pdf-file/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFのXMPメタデータを取得する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

PDFファイルからXMPメタデータを取得するには、[PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用してPDFファイルをバインドする必要があります。特定のXMPメタデータプロパティを[PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata)オブジェクトに渡して、その値を取得することができます。次のコードスニペットは、PDFファイルからXMPメタデータを取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET を参照してください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// PdfXmpMetadataオブジェクトを作成
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// オブジェクトにPDFファイルをバインド
xmpMetaData.BindPdf( dataDir + "input.pdf");

// XMPメタデータプロパティを取得
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```