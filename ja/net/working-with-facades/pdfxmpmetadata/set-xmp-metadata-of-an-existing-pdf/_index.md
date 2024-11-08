---
title: 既存のPDFのXMPメタデータを設定する
type: docs
weight: 20
url: /ja/net/set-xmp-metadata-of-an-existing-pdf/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFのXMPメタデータを設定する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

PDFファイルにXMPメタデータを設定するには、[PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用してPDFファイルをバインドする必要があります。 You can use [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) method of the [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) class to add different properties. Finally, call the [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method of the [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) class. The following code snippet shows you how to add XMP metadata in a PDF file.

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// PdfXmpMetadataオブジェクトを作成
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// オブジェクトにPDFファイルをバインド
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// 作成日を追加
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// メタデータの日付を変更
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// 作成ツールを追加
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Creator tool name");

// 修正日を削除
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// ユーザー定義プロパティを追加
// ステップ #1: 名前空間プレフィックスとURIを登録
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// ステップ #2: プレフィックス付きのユーザープロパティを追加
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// ユーザー定義プロパティを変更
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// PDFファイルにxmpメタデータを保存
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// オブジェクトを閉じる
xmpMetaData.Close();
```