---
title: ページプロパティの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ja/net/manipulate-page-properties/
description: このセクションでは、PdfPageEditorクラスを使用してAspose.PDFファサードでページプロパティを操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "PdfPageEditorクラスを紹介します。これは、Aspose.PDF for .NETファサードを使用してPDFページプロパティを管理するための強力なツールです。この機能により、開発者は回転、ズームレベル、ページ寸法などの重要なページ属性を取得および変更でき、PDFコンテンツのプレゼンテーションを細かく制御できます。特定のページコンテンツをリサイズする機能を含む、プロパティの取得と設定のための簡単なメソッドを使用することで、PDFドキュメントの強化がこれまでになく簡単になりました。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 既存のPDFファイルからPDFページプロパティを取得する

[PdfPageEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor)を使用すると、PDFファイルの個々のページを操作できます。これにより、異なるページボックスサイズ、ページ回転、ページズームなどの個々のページのプロパティを取得できます。これらのプロパティを取得するには、[PdfPageEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor)オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[GetPageRotation](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation)、[GetPages](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor/methods/getpages)、[GetPageBoxSize](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize)などの異なるメソッドを使用してページプロパティを取得できます。

以下のコードスニペットは、既存のPDFファイルからPDFページプロパティを取得する方法を示しています。


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## 既存のPDFファイルにPDFページプロパティを設定する

ページ回転、ズーム、または原点などのページプロパティを設定するには、[PdfPageEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor)クラスを使用する必要があります。このクラスは、これらのページプロパティを設定するためのさまざまなメソッドとプロパティを提供します。まず、[PdfPageEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、これらのメソッドとプロパティを使用してページプロパティを設定できます。最後に、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、既存のPDFファイルにPDFページプロパティを設定する方法を示しています。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## PDFファイルの特定のページのページコンテンツをリサイズする

[PdfPageEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfpageeditor)クラスのResizeContentsメソッドを使用すると、PDFファイル内のページコンテンツをリサイズできます。[ContentsResizeParameters](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters)クラスは、ページをリサイズするために使用されるパラメータ（例えば、パーセンテージまたは単位でのマージンなど）を指定するために使用されます。すべてのページをリサイズするか、リサイズするページの配列を指定することができます。

以下のコードスニペットは、PDFファイルの特定のページのコンテンツをリサイズする方法を示しています。



```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```