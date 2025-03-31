---
title: マルチライン透かしの追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/adding-multi-line-watermark-to-existing-pdf/
description: このセクションでは、FormattedTextクラスを使用して既存のPDFにマルチライン透かしを追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "Aspose.Pdf.Facades名前空間を使用して、既存のPDFにマルチライン透かしを追加する機能を紹介します。この新しい機能により、ユーザーはFormattedTextクラスの新しく実装されたAddNewLineText()メソッドを使用して、文書に複数行のテキストを簡単に組み込むことができます。カスタマイズされたマルチライン透かしでPDFプレゼンテーションを手軽に強化しましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "188",
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
    "url": "/net/adding-multi-line-watermark-to-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-multi-line-watermark-to-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

多くのユーザーがPDF文書にマルチラインテキストをスタンプしたいと考えています。彼らは通常、`\n`や`<br>`を使用しようとしますが、これらの文字はAspose.Pdf.Facades名前空間ではサポートされていません。したがって、これを可能にするために、Aspose.Pdf.Facades名前空間の[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)クラスに[AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index)という別のメソッドを追加しました。

{{% /alert %}}

## 実装の詳細

既存のPDFにマルチライン透かしを追加するためのコードチャンクを参照してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampToPdf()
{
    // Instantiate a stamp object
    var logoStamp = new Aspose.Pdf.Facades.Stamp();

    // Instantiate an object of FormattedText class
    var formatText = new Aspose.Pdf.Facades.FormattedText("Hello World!",
        System.Drawing.Color.FromArgb(180, 0, 0), 
        Aspose.Pdf.Facades.FontStyle.TimesItalic,
        Aspose.Pdf.Facades.EncodingType.Winansi, false, 50);

    // Add another line for Stamp
    formatText.AddNewLineText("Good Luck");
    // BindLogo to PDF
    logoStamp.BindLogo(formatText);
}
```