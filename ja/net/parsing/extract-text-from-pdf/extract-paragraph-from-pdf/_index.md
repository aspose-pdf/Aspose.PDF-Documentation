---
title: PDFから段落を抽出する C#
linktitle: PDFから段落を抽出する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/extract-paragraph-from-pdf/
description: Aspose.PDFを使用して、.NETでPDF文書から段落を抽出する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Paragraph from PDF C#",
    "alternativeHeadline": "Extract Text from PDF as Paragraphs Efficiently",
    "abstract": "Aspose.PDFの新しいParagraphAbsorber機能により、開発者はPDF文書から段落を効率的に抽出および操作できます。このツールを使用すると、ユーザーは整理された段落形式でテキストを取得できるだけでなく、カスタマイズ可能な境界線を通じてセクションを視覚化し、PDFテキスト抽出の精度を向上させることができます。この機能は、構造化されたPDFデータを扱う際の作業を簡素化し、詳細なテキスト分析を必要とするアプリケーションにとって非常に貴重です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "590",
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
    "url": "/net/extract-paragraph-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-paragraph-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDF文書から段落形式でテキストを抽出する

特定のテキスト（「プレーンテキスト」または「正規表現」を使用）を単一ページまたは全体の文書から検索することによって、PDF文書からテキストを取得できます。また、単一ページ、ページの範囲、または完全な文書の完全なテキストを取得することもできます。ただし、場合によっては、PDF文書から段落を抽出する必要があります。私たちは、PDF文書ページのテキスト内のセクションと段落を検索する機能を実装しました。段落をPDF文書から抽出するために使用できるParagraphAbsorberクラス（TextFragmentAbsorberやTextAbsorberのように）を導入しました。ParagraphAbsorberを使用する方法は次の2つです。

**PDFページ上のテキストのセクションと段落の境界を描画することによって:**

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraphWithDrawingTheBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentForExtract.pdf"))
    {
        var page = document.Pages[2];

        var absorber = new Aspose.Pdf.Text.ParagraphAbsorber();
        absorber.Visit(page);

        Aspose.Pdf.Text.PageMarkup markup = absorber.PageMarkups[0];

        foreach (Aspose.Pdf.Text.MarkupSection section in markup.Sections)
        {
            DrawRectangleOnPage(section.Rectangle, page);
            foreach (Aspose.Pdf.Text.MarkupParagraph paragraph in section.Paragraphs)
            {
                DrawPolygonOnPage(paragraph.Points, page);
            }
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithBorder_out.pdf");
    }
}

private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(2));
    page.Contents.Add(
        new Aspose.Pdf.Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}

private static void DrawPolygonOnPage(Aspose.Pdf.Point[] polygon, Aspose.Pdf.Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(1));
    page.Contents.Add(new Aspose.Pdf.Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}
```

**段落コレクションを反復処理してテキストを取得することによって:**

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraphByIteratingThroughParagraphsCollection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentForExtract.pdf"))
    {
        // Instantiate ParagraphAbsorber
        var absorber = new Aspose.Pdf.Text.ParagraphAbsorber();
        absorber.Visit(document);

        foreach (Aspose.Pdf.Text.PageMarkup markup in absorber.PageMarkups)
        {
            int i = 1;
            foreach (Aspose.Pdf.Text.MarkupSection section in markup.Sections)
            {
                int j = 1;
                foreach (Aspose.Pdf.Text.MarkupParagraph paragraph in section.Paragraphs)
                {
                    StringBuilder paragraphText = new StringBuilder();
                    foreach (List<Aspose.Pdf.Text.TextFragment> line in paragraph.Lines)
                    {
                        foreach (Aspose.Pdf.Text.TextFragment fragment in line)
                        {
                            paragraphText.Append(fragment.Text);
                        }
                        paragraphText.Append("\r\n");
                    }
                    paragraphText.Append("\r\n");

                    Console.WriteLine("Paragraph {0} of section {1} on page {2}:", j, i, markup.Number);
                    Console.WriteLine(paragraphText.ToString());

                    j++;
                }
                i++;
            }
        }
    }
}
```