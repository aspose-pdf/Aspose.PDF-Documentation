---
title: C#でPDFファイルにリンクを作成する
linktitle: リンクを作成
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/create-links/
description: このセクションでは、C#を使用してPDFドキュメントにリンクを作成する方法を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Links in PDF file with C#",
    "alternativeHeadline": "Create Interactive Links in PDFs Using C#",
    "abstract": "この新機能により、開発者はC#を使用してPDFドキュメント内にインタラクティブリンクをシームレスに作成できます。この機能は、外部アプリケーションや他のPDFファイルへのリンクを提供することで、ユーザーのエンゲージメントを高め、よりダイナミックで機能豊かなドキュメント体験を可能にします。チュートリアルやユーザーガイドに最適で、この統合によりユーザーはコンテンツを効果的に接続できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create Links, PDF document, C#, LinkAnnotation, LaunchAction, GoToRemoteAction, Aspose.PDF, Document object, PDF manipulation, External link",
    "wordcount": "690",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2024-11-25",
    "description": "このセクションでは、C#を使用してPDFドキュメントにリンクを作成する方法を説明します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## リンクを作成

ドキュメントにアプリケーションへのリンクを追加することで、ドキュメントからアプリケーションにリンクすることが可能です。これは、特定のチュートリアルのポイントで読者に特定のアクションを取らせたい場合や、機能豊かなドキュメントを作成したい場合に便利です。アプリケーションリンクを作成するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. リンクを追加したい[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を取得します。
1. Pageと[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle)オブジェクトを使用して[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを使用してリンク属性を設定します。
1. また、[LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction)オブジェクトのActionプロパティを設定します。
1. [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction)オブジェクトを作成する際に、起動したいアプリケーションを指定します。
1. リンクをPageオブジェクトの[Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations)プロパティに追加します。
1. 最後に、Documentオブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFを保存します。

次のコードスニペットは、PDFファイル内にアプリケーションへのリンクを作成する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateApplicationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateApplicationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### PDFファイル内にPDFドキュメントリンクを作成する

Aspose.PDF for .NETを使用すると、外部PDFファイルへのリンクを追加して、複数のドキュメントをリンクさせることができます。PDFドキュメントリンクを作成するには：

1. まず、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを作成します。
1. 次に、リンクを追加したい特定の[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を取得します。
1. Pageと[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle)オブジェクトを使用して[LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを作成します。
1. [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)オブジェクトを使用してリンク属性を設定します。
1. Actionプロパティを[GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction)オブジェクトに設定します。
1. GoToRemoteActionオブジェクトを作成する際に、起動すべきPDFファイルと、開くべきページ番号を指定します。
1. リンクをPageオブジェクトのAnnotationsコレクションに追加します。
1. Documentオブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFを保存します。

次のコードスニペットは、PDFファイル内にPDFドキュメントリンクを作成する方法を示しています。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateDocumentLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateDocumentLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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