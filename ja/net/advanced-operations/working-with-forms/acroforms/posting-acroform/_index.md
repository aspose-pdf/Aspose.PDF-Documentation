---
title: AcroFormデータの投稿
linktitle: AcroFormの投稿
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/posting-acroform-data/
description: Aspose.Pdf.Facades名前空間を使用して、フォームデータをXMLファイルにインポートおよびエクスポートできます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Posting AcroForm Data",
    "alternativeHeadline": "Post AcroForm Data",
    "abstract": "Aspose.PDF for .NETの新しい強力な機能、AcroFormデータを投稿する機能を紹介します。この機能により、開発者はAcroFormを作成および編集するだけでなく、フォームデータをXMLファイルにシームレスにインポートおよびエクスポートでき、アプリケーション内でのデータ処理および保存機能が向上します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Posting AcroForm Data, Import and Export Form Data, Aspose.PDF for .NET, AcroForm Fields, Submit Button, External Web Page Integration, Form Data Posting, XML File Handling, FieldType.Text, Database Saving",
    "wordcount": "400",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.Pdf.Facades名前空間を使用して、フォームデータをXMLファイルにインポートおよびエクスポートできます。"
}
</script>

{{% alert color="primary" %}}

AcroFormはPDFドキュメントの重要なタイプです。[Aspose.Pdf.Facades名前空間](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)を使用してAcroFormを作成および編集するだけでなく、フォームデータをXMLファイルにインポートおよびエクスポートすることもできます。Aspose.PDF for .NETのAspose.Pdf.Facades名前空間を使用すると、AcroFormの別の機能を実装でき、AcroFormデータを外部ウェブページに投稿することができます。このウェブページは投稿された変数を読み取り、このデータをさらに処理するために使用します。この機能は、データをPDFファイルに保持するだけでなく、サーバーに送信し、データベースに保存するなどのケースで便利です。

{{% /alert %}}

## 実装の詳細

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

この記事では、[Aspose.Pdf.Facades名前空間](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)を使用してAcroFormを作成しようとしました。また、送信ボタンを追加し、そのターゲットURLを設定しました。以下のコードスニペットは、フォームを作成し、ウェブページで投稿されたデータを受信する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAcroFormWithFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create an instance of FormEditor class and bind input and output pdf files
    using (var editor = new Aspose.Pdf.Facades.FormEditor(dataDir + "input.pdf", dataDir + "output.pdf"))
    {
        // Create AcroForm fields - I have created only two fields for simplicity
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

        // Add a submit button and set target URL
        editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

        // Save PDF document
        editor.Save();
    }
}
```

{{% alert color="primary" %}}

以下のコードスニペットは、ターゲットウェブページで投稿された値を受信する方法を示しています。この例では、Show.aspxという名前のページを使用し、ページロードメソッドにシンプルな1行のコードを追加しました。

{{% /alert %}}

```csharp
// Show the posted values on the target web page
Response.Write("Hello " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
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