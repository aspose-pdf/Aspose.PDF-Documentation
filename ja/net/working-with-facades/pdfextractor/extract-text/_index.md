---
title: PDFファイルからテキストを抽出する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/extract-text/
description: このセクションでは、PdfExtractorクラスを使用してPDFからテキストを抽出する方法を説明します。
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "PdfExtractorクラスは、複数のメソッドを通じてPDFファイルから効率的にテキストを抽出することを可能にし、ユーザーがテキスト、画像、および添付ファイルを簡単に取得できるようにします。ExtractText、GetText、GetNextPageTextなどのメソッドを利用することで、開発者は個々のページまたは全体の文書からテキストコンテンツをシームレスに抽出して保存し、PDF操作タスクを効率化できます。柔軟な抽出モードが利用可能で、この機能は出力形式に対する制御を強化し、PDFデータを扱うすべての人にとって不可欠なツールとなります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

この記事では、PDFファイルからテキストを抽出する詳細について見ていきます。これらの抽出機能はすべて、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスにまとめられています。これらの機能をコードでどのように使用するかを見ていきましょう。

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)クラスは、3種類の抽出機能を提供します。これらの3つのカテゴリは、テキスト、画像、および添付ファイルです。これらの3つのカテゴリのそれぞれで抽出を行うために、PdfExtractorはさまざまなメソッドを提供しており、最終的な出力を得るために連携して機能します。

たとえば、テキストを抽出するには、[ExtractText、GetText、HasNextPageText、GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index)の3つのメソッドを使用できます。テキストの抽出を開始するには、まず[ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index)メソッドを呼び出す必要があります。これにより、PDFファイルからテキストが抽出され、メモリに保存されます。その後、[GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index)メソッドがこの抽出されたテキストを取得し、指定された場所にファイルとしてディスクに保存します。[HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext)は、各ページをループして次のページにテキストがあるかどうかを確認するのに役立ちます。テキストが含まれている場合、[GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index)が個々のページのテキストをファイルに保存するのに役立ちます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

テキスト抽出モードを抽出するには、次のコードを使用します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```