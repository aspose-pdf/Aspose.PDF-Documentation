---
title: プログラムでPDFドキュメントを作成する
linktitle: PDFを作成する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/create-document/
description: このページでは、Aspose.PDFライブラリを使用してゼロからPDFドキュメントを作成する方法を説明します。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "Aspose.PDF for .NETの新機能により、開発者はC#およびVB.NETを使用してプログラムでPDFドキュメントを作成できるようになり、WinFormsやASP.NETなどのさまざまな.NETアプリケーションのプロセスが簡素化されます。ページやテキストを追加するための簡単なメソッドを使用することで、ユーザーはゼロからカスタムPDFファイルを簡単に生成でき、アプリケーションの機能性とユーザーエクスペリエンスを向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

Aspose.PDF for .NET APIを使用すると、C#およびVB.NETを使用してPDFファイルを作成および読み取ることができます。このAPIは、WinForms、ASP.NETなどのさまざまな.NETアプリケーションで使用できます。この記事では、Aspose.PDF for .NET APIを使用して.NETアプリケーションでPDFファイルを簡単に生成および読み取る方法を示します。

## C#を使用してPDFファイルを作成する方法

C#を使用してPDFファイルを作成するには、次の手順を使用できます。

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスのオブジェクトを作成します。
1. Documentオブジェクトの[Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages)コレクションに[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)オブジェクトを追加します。
1. ページの[Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)コレクションに[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)を追加します。
1. 結果のPDFドキュメントを保存します。

次のコードスニペットは、[Aspose.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

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

この場合、A4ページサイズ、縦向きの1ページのPDFドキュメントを作成します。ページの左上部分には「Hello, World」が含まれます。