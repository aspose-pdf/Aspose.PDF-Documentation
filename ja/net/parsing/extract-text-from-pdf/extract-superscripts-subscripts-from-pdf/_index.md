---
title: PDFからスーパースクリプトとサブスクリプトのテキストを抽出する
linktitle: スーパースクリプトとサブスクリプトを抽出する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/extract-superscripts-subscripts-from-pdf/
description: この記事では、C#でAspose.PDFを使用してPDFからスーパースクリプトとサブスクリプトのテキストを抽出するさまざまな方法について説明します。
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "Aspose.PDF for .NETライブラリを使用してPDF文書からスーパースクリプトとサブスクリプトのテキストを抽出する新機能により、ユーザーは技術文書に見られる専門的なテキストフォーマットを正確に取得できます。この強化により、開発者はこれらのテキスト要素を簡単に操作するためのツールを提供され、数式や化学仕様の処理が簡素化されます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## スーパースクリプトとサブスクリプトのテキストを抽出する

PDF文書からテキストを抽出することは一般的な作業です。しかし、そのテキストを抽出すると、技術文書や記事に典型的な**スーパースクリプトとサブスクリプト**が表示されないことがあります。サブスクリプトまたはスーパースクリプトは、通常のテキストの行の下または上に配置された文字、数字、または文字です。通常、他のテキストよりも小さいです。

**サブスクリプトとスーパースクリプト**は、数式、数学的表現、化合物の仕様で最もよく使用されます。同じテキストの一節に多くのものがある場合、それらを編集するのは難しいです。
最新のリリースの1つで、**Aspose.PDF for .NET**ライブラリはPDFからスーパースクリプトとサブスクリプトのテキストを抽出するサポートを追加しました。

**TextFragmentAbsorber**クラスを使用すると、見つかったテキストで何でもできるようになります。つまり、全体のテキストを単純に使用できます。次のコードスニペットを試してください：

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

または、**TextFragments**を個別に使用して、座標やサイズでソートするなど、さまざまな操作を行うことができます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```