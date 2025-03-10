---
title: スタンプからテキストを抽出する C#
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/extract-text-from-stamps/
description: Aspose.PDF for .NET の特別な機能 - スタンプ注釈からのテキスト抽出の使用方法を学ぶ
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text From Stamps using C#",
    "alternativeHeadline": "Extract Text from PDF Stamp Annotations with Ease",
    "abstract": "PDF ドキュメントのスタンプ注釈からテキストを取得するために特別に設計された Aspose.PDF for .NET の強力なテキスト抽出機能を発見してください。この新機能はプロセスを合理化し、開発者が簡潔なコードスニペットを使用してスタンプ注釈内のテキストに簡単にアクセスし、操作できるようにし、PDF 管理タスクの生産性と効率を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "168",
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
    "url": "/net/extract-text-from-stamps/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-stamps/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF は、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## スタンプ注釈からテキストを抽出する

Aspose.PDF for NET を使用すると、スタンプ注釈からテキストを抽出できます。PDF のスタンプ注釈からテキストを抽出するには、次の手順を使用できます。

1. `Document` クラスのオブジェクトを作成します。
1. ページの注釈リストから目的の `Annotation` を取得します。
1. `TextAbsorber` クラスの新しいオブジェクトを定義します。
1. TextAbsorber の visit メソッドを使用してテキストを取得します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractStampText.pdf"))
    {
        Aspose.Pdf.Annotations.Annotation item = document.Pages[1].Annotations[1];
        if (item is Aspose.Pdf.Annotations.StampAnnotation annot)
        {
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            Aspose.Pdf.XForm appearance = annot.Appearance["N"];
            absorber.Visit(appearance);
            Console.WriteLine(absorber.Text);
        }
    }
}
```