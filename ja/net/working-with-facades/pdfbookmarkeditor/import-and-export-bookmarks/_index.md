---
title: ブックマークのインポートとエクスポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/import-and-export-bookmarks/
description: このセクションでは、Aspose.PDF Facadesを使用してブックマークをインポートおよびエクスポートする方法について説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Bookmarks",
    "alternativeHeadline": "Seamlessly Import and Export PDF Bookmarks with XML",
    "abstract": "Aspose.PDF for .NETの新しいブックマークのインポートとエクスポート機能を発見してください。これにより、ユーザーはXMLファイルから既存のPDFドキュメントにブックマークをシームレスにインポートし、ブックマークをXMLにエクスポートできます。この機能は、ブックマークの統合を簡素化することにより、文書管理を強化し、PDF内の組織構造を維持するための簡単なプロセスを提供します。この強力な追加機能でワークフローを最適化し、PDF処理能力を向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/import-and-export-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## XMLから既存のPDFファイルへのブックマークのインポート

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1)メソッドを使用すると、XMLファイルからPDFファイルにブックマークをインポートできます。ブックマークをインポートするには、[PdfBookmarkEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfbookmarkeditor)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/bindpdf/index)メソッドを使用してPDFファイルをバインドする必要があります。その後、[ImportBookmarksWithXml](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1)メソッドを呼び出す必要があります。最後に、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、XMLファイルからブックマークをインポートする方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ImportFromXML.pdf");

        // Import bookmarks
        bookmarkEditor.ImportBookmarksWithXML(dataDir + "bookmarks.xml");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "ImportFromXML_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ImportFromXML.pdf");

    // Import bookmarks
    bookmarkEditor.ImportBookmarksWithXML(dataDir + "bookmarks.xml");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "ImportFromXML_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 既存のPDFファイルからXMLへのブックマークのエクスポート

ExportBookmarksToXmlメソッドを使用すると、PDFファイルからXMLファイルにブックマークをエクスポートできます。

ブックマークをエクスポートするには：

1. PdfBookmarkEditorオブジェクトを作成し、BindPdfメソッドを使用してPDFファイルをバインドします。
1. ExportBookmarksToXmlメソッドを呼び出します。
1. Saveメソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、XMLファイルにブックマークをエクスポートする方法を示しています。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ExportToXML.pdf");

        // Export bookmarks to an XML file
        bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ExportToXML.pdf");

    // Export bookmarks to an XML file
    bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
}
```
{{< /tab >}}
{{< /tabs >}}