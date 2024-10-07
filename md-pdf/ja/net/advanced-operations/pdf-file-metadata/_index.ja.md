---
title: PDFファイルのメタデータの操作 | C#
linktitle: PDFファイルのメタデータ
type: docs
weight: 140
url: /net/pdf-file-metadata/
description: このセクションでは、PDFファイル情報の取得方法、PDFファイルからXMPメタデータを取得する方法、PDFファイル情報を設定する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルのメタデータの操作 | C#",
    "alternativeHeadline": "PDFファイルのメタデータの取得方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文書生成",
    "keywords": "pdf, c#, pdfファイルメタデータ",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、PDFファイル情報の取得方法、PDFファイルからXMPメタデータを取得する方法、PDFファイル情報を設定する方法について説明します。"
}
</script>

以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

## PDFファイル情報の取得

PDFファイルの特定の情報を取得するには、まず[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info)プロパティを使用して[DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo)オブジェクトを取得する必要があります。[DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo)オブジェクトが取得されたら、個々のプロパティの値を取得できます。以下のコードスニペットは、PDFファイル情報を取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// ドキュメント情報を取得
DocumentInfo docInfo = pdfDocument.Info;
// ドキュメント情報を表示
Console.WriteLine("著者: {0}", docInfo.Author);
Console.WriteLine("作成日: {0}", docInfo.CreationDate);
Console.WriteLine("キーワード: {0}", docInfo.Keywords);
Console.WriteLine("変更日: {0}", docInfo.ModDate);
Console.WriteLine("主題: {0}", docInfo.Subject);
Console.WriteLine("タイトル: {0}", docInfo.Title);
```
## PDFファイル情報を設定

Aspose.PDF for .NETでは、PDFのファイル固有情報（著者、作成日、主題、タイトルなど）を設定できます。この情報を設定するには：

1. [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) オブジェクトを作成します。
1. プロパティの値を設定します。
1. Document クラスの Save メソッドを使用して更新されたドキュメントを保存します。

{{% alert color="primary" %}}

*Application* と *Producer* フィールドに値を設定することはできません。これらのフィールドには Aspose Ltd. および Aspose.PDF for .NET x.x.x が表示されます。

{{% /alert %}}

次のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// ドキュメント情報を指定
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "PDF Information";
docInfo.Title = "Setting PDF Document Information";

dataDir = dataDir + "SetFileInfo_out.pdf";
// 出力ドキュメントを保存
pdfDocument.Save(dataDir);
```
## PDFファイルからXMPメタデータを取得する

Aspose.PDFを使用すると、PDFファイルのXMPメタデータにアクセスできます。PDFファイルのメタデータを取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成し、入力PDFファイルを開きます。
1. [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata)プロパティを使用してファイルのメタデータを取得します。

以下のコードスニペットは、PDFファイルからメタデータを取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// プロパティを取得
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## PDFファイルにXMPメタデータを設定する

Aspose.PDFを使用すると、PDFファイルにメタデータを設定できます。
Aspose.PDFを使用してPDFファイルのメタデータを設定できます。

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを作成します。
1. [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) プロパティを使用してメタデータ値を設定します。
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたドキュメントを保存します。

次のコードスニペットは、PDFファイルにメタデータを設定する方法を示しています。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// プロパティを設定
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// ドキュメントを保存
pdfDocument.Save(dataDir);
```
## メタデータをプレフィックスと共に挿入する

一部の開発者は、プレフィックス付きの新しいメタデータ名前空間を作成する必要があります。次のコードスニペットは、プレフィックス付きでメタデータを挿入する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Xmlnsプレフィックスが削除されました
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// ドキュメントを保存
pdfDocument.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

