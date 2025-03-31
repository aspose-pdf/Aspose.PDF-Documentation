---
title: C#言語を使用したHello Worldの例
linktitle: Hello Worldの例
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/hello-world-example/
description: このサンプルは、Aspose.PDFを使用して「Hello World」というテキストを含むシンプルなPDFドキュメントを作成する方法を示しています。
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "このサンプルは、Aspose.PDFを使用して「Hello World」というテキストを含むシンプルなPDFドキュメントを作成する方法を示しています。",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

「Hello World」例は、プログラミング言語やソフトウェアの機能をシンプルなユースケースで紹介するために伝統的に使用されます。

Aspose.PDF for .NETは、開発者が.NETアプリケーションにPDFドキュメントの作成、操作、および変換機能を組み込むことを可能にする機能豊富なPDF APIです。PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX、および画像ファイル形式を含む多くの人気ファイル形式での作業をサポートしています。この記事では、「Hello World!」というテキストを含むPDFドキュメントを作成します。Aspose.PDF for .NETを環境にインストールした後、以下のコードサンプルを実行してAspose.PDF APIがどのように機能するかを確認できます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

以下のコードスニペットは、次の手順に従います：

1. [Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトをインスタンス化します。
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page)を追加します。
1. [TextFragment](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textfragment)オブジェクトを作成します。
1. TextFragmentをページの[Paragraph](https://reference.aspose.com/pdf/ja/net/aspose.pdf/page/properties/paragraphs)コレクションに追加します。
1. 結果のPDFドキュメントを[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.document/save/methods/4)します。

以下のコードスニペットは、Aspose.PDF for .NET APIの動作を示すHello Worldプログラムです。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```