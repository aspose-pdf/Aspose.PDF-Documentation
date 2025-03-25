---
title: 複雑なPDFの作成
linktitle: 複雑なPDFの作成
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/complex-pdf-example/
description: Aspose.PDF for NETを使用すると、画像、テキストフラグメント、およびテーブルを含むより複雑なドキュメントを1つのドキュメントに作成できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NETは、開発者が画像、テキストフラグメント、およびテーブルを1つのドキュメントにシームレスに統合できるようにする、複雑なPDFを作成するための強力な機能を紹介します。この機能はDOMベースのアプローチを活用しており、PDF生成における詳細なカスタマイズとレイアウト制御を可能にし、プロフェッショナルグレードのドキュメントを効率的に作成するのに最適です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

[こんにちは、世界](/pdf/ja/net/hello-world-example/)の例では、C#とAspose.PDFを使用してPDFドキュメントを作成するための簡単な手順を示しました。この記事では、C#とAspose.PDF for .NETを使用して、より複雑なドキュメントを作成する方法を見ていきます。例として、旅客フェリーサービスを運営する架空の会社のドキュメントを取り上げます。
私たちのドキュメントには、画像、2つのテキストフラグメント（ヘッダーと段落）、およびテーブルが含まれます。このようなドキュメントを構築するために、DOMベースのアプローチを使用します。詳細については、[DOM APIの基本](/pdf/ja/net/basics-of-dom-api/)のセクションをお読みください。

ゼロからドキュメントを作成する場合、特定の手順に従う必要があります：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトをインスタンス化します。このステップでは、メタデータはあるがページがない空のPDFドキュメントを作成します。
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を追加します。これで、ドキュメントには1ページが追加されます。
1. ページに[Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index)を追加します。
1. ヘッダー用の[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)を作成します。ヘッダーには、フォントサイズ24ptのArialフォントと中央揃えを使用します。
1. ヘッダーをページの[Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)に追加します。
1. 説明用の[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)を作成します。説明には、フォントサイズ24ptのArialフォントと中央揃えを使用します。
1. （説明）をページのParagraphsに追加します。
1. テーブルを作成し、テーブルプロパティを追加します。
1. （テーブル）をページの[Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)に追加します。
1. ドキュメントを「Complex.pdf」として保存します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```