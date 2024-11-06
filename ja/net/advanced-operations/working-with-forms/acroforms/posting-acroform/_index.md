---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: ja/net/posting-acroform-data/
description: Aspose.PDF for .NETのAspose.Pdf.Facades名前空間を使用して、フォームデータをXMLファイルにインポートおよびエクスポートできます。
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
    "alternativeHeadline": "XMLファイルにフォームデータをインポートおよびエクスポート",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, posting acroform data",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETのAspose.Pdf.Facades名前空間を使用して、フォームデータをXMLファイルにインポートおよびエクスポートできます。"
}
</script>
{{% alert color="primary" %}}
AcroFormはPDFドキュメントの重要なタイプです。[Aspose.Pdf.Facades 名前空間](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)を使用してAcroFormを作成および編集するだけでなく、フォームデータをXMLファイルにインポートおよびエクスポートすることもできます。.NETのAspose.PDF用Aspose.Pdf.Facades名前空間は、外部のウェブページにAcroFormデータを投稿するというAcroFormの別の機能を実装することを可能にします。このウェブページは、投稿された変数を読み取り、このデータをさらに処理するために使用します。この機能は、データをPDFファイルに保持したいだけでなく、サーバーに送信してデータベースなどに保存したい場合に便利です。
{{% /alert %}}

## 実装の詳細

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリと一緒に動作します。

この記事では、[Aspose.Pdf.Facades 名前空間](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)を使用してAcroFormを作成しようとしました。
この記事では、[Aspose.Pdf.Facades名前空間](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)を使用してAcroFormを作成しようと試みました。

```csharp
// FormEditorクラスのインスタンスを作成し、入力および出力PDFファイルをバインドします
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// AcroFormフィールドを作成します - 簡単のために2つのフィールドのみを作成しました
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// 提出ボタンを追加し、ターゲットURLを設定します
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// 出力PDFファイルを保存します
editor.Save();
```

{{% alert color="primary" %}}

次のコードスニペットは、ターゲットWebページで投稿された値を受け取る方法を示しています。
次のコードスニペットは、対象のWebページで投稿された値を受け取る方法を示しています。

{{% /alert %}}

```csharp
// 対象のWebページで投稿された値を表示する
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

