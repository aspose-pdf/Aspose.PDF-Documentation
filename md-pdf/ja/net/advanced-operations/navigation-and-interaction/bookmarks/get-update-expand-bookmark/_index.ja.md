---
title: ブックマークの追加と削除
linktitle: ブックマークの追加と削除
type: docs
weight: 10
url: /net/add-and-delete-bookmark/
description: C#を使用してPDFドキュメントにブックマークを追加することができます。PDFドキュメントからすべてのブックマークまたは特定のブックマークを削除することが可能です。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ブックマークの追加と削除",
    "alternativeHeadline": "PDFからブックマークを追加・削除する方法",
    "author": {
        "@type": "Person",
        "name":"アンドリー・アンドルホフスキー",
        "givenName": "アンドリー",
        "familyName": "アンドルホフスキー",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, ブックマーク削除, ブックマーク追加",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "C#を使用してPDFドキュメントにブックマークを追加することができます。PDFドキュメントからすべてのブックマークまたは特定のブックマークを削除することが可能です。"
}
</script>
次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## PDFドキュメントにブックマークを追加する

ブックマークは、[OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) コレクションに保持され、それ自体が [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) コレクションにあります。

PDFにブックマークを追加するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトを使用してPDFドキュメントを開きます。
1. ブックマークを作成し、そのプロパティを定義します。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) コレクションをアウトラインコレクションに追加します。

次のコードスニペットは、PDFドキュメントにブックマークを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// ブックマークオブジェクトを作成する
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// 目的のページ番号を設定する
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// ドキュメントのアウトラインコレクションにブックマークを追加する。
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// 出力を保存する
pdfDocument.Save(dataDir);
```
## PDFドキュメントに子ブックマークを追加する

ブックマークはネストすることができ、親と子のブックマークの階層的な関係を示しています。この記事では、PDFに二階層目のブックマーク、つまり子ブックマークを追加する方法について説明します。

PDFファイルに子ブックマークを追加するには、まず親ブックマークを追加します：

1. ドキュメントを開く。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection)にブックマークを追加し、そのプロパティを定義する。
1. OutlineItemCollectionをDocumentオブジェクトの[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションに追加する。

子ブックマークの作成は、上記の親ブックマークと同様に行われますが、親ブックマークのアウトラインコレクションに追加されます。

次のコードスニペットは、PDFドキュメントに子ブックマークを追加する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// 親ブックマークオブジェクトを作成する
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "親アウトライン";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// 子ブックマークオブジェクトを作成する
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "子アウトライン";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// 親ブックマークのコレクションに子ブックマークを追加する
pdfOutline.Add(pdfChildOutline);
// ドキュメントのアウトラインコレクションに親ブックマークを追加する。
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// 出力を保存する
pdfDocument.Save(dataDir);
```
## PDFドキュメントからすべてのブックマークを削除する

PDF内のすべてのブックマークは[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションに保持されています。この記事では、PDFファイルからすべてのブックマークを削除する方法について説明します。

PDFファイルからすべてのブックマークを削除するには：

1. [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションのDeleteメソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して、修正されたファイルを保存します。

次のコードスニペットは、PDFドキュメントからすべてのブックマークを削除する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// すべてのブックマークを削除
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// 更新されたファイルを保存
pdfDocument.Save(dataDir);
```
## PDFドキュメントから特定のブックマークを削除する

PDFファイルから特定のブックマークを削除するには：

1. ブックマークのタイトルをパラメータとして [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) コレクションのDeleteメソッドに渡します。
1. 次に、DocumentオブジェクトのSaveメソッドで更新されたファイルを保存します。

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスは [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) コレクションを提供します。[Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) メソッドは、メソッドに渡されたタイトルのブックマークを削除します。

以下のコードスニペットは、PDFドキュメントから特定のブックマークを削除する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// タイトルによる特定のアウトラインを削除
pdfDocument.Outlines.Delete("Child Outline");

// 更新されたファイルを保存
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```

