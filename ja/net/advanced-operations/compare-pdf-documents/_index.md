---
title: PDF文書の比較
linktitle: PDFの比較
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ja/net/compare-pdf-documents/
description: 24.7リリース以降、PDF文書の内容を注釈マークと並べて出力で比較することが可能です
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "Aspose.PDF for .NETの新しいPDF比較機能により、ユーザーは特定のページまたは全体の内容を通じて、2つのPDF文書間の違いを効率的に特定できます。並べて出力し、追加の変更マーカーやさまざまな比較モードなどのカスタマイズ可能なオプションを使用することで、この強力なツールは、改訂を追跡しレビューするのを容易にし、コラボレーションを強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "592",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

すべての比較ツールは、[Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/)ライブラリで利用可能です。

## PDF文書を比較する方法

PDF文書を扱う際、2つの文書の内容を比較して違いを特定する必要がある場合があります。Aspose.PDF for .NETライブラリは、この目的のために強力なツールセットを提供します。この記事では、いくつかの簡単なコードスニペットを使用してPDF文書を比較する方法を探ります。

Aspose.PDFの比較機能を使用すると、2つのPDF文書をページごとに比較できます。特定のページまたは全体の文書を比較することができます。結果として得られる比較文書は、違いを強調表示し、2つのファイル間の変更を特定しやすくします。

以下は、Aspose.PDF for .NETライブラリを使用してPDF文書を比較する可能な方法のリストです：

1. **特定ページの比較** - 2つのPDF文書の最初のページを比較します。

1. **全体文書の比較** - 2つのPDF文書の全体の内容を比較します。

1. **PDF文書をグラフィカルに比較する**：

- GetDifferenceメソッドを使用してPDFを比較 - 変更がマークされた個別の画像。

- CompareDocumentsToPdfメソッドを使用してPDFを比較 - 変更がマークされた画像を含むPDF文書。

## 特定ページの比較

最初のコードスニペットは、2つのPDF文書の最初のページを比較する方法を示しています。

1. 文書の初期化。
コードは、それぞれのファイルパス（documentPath1とdocumentPath2）を使用して2つのPDF文書を初期化することから始まります。パスは現在空の文字列として指定されていますが、実際にはこれを実際のファイルパスに置き換えます。

2. 比較プロセス。

- ページ選択 - 比較は各文書の最初のページに制限されています（'Pages[1]'）。
- 比較オプション：

'AdditionalChangeMarks = true' - このオプションは、追加の変更マーカーが表示されることを保証します。これらのマーカーは、現在比較しているページにない場合でも、他のページに存在する可能性のある違いを強調表示します。

'ComparisonMode = ComparisonMode.IgnoreSpaces' - このモードは、テキスト内のスペースを無視し、単語内の変更にのみ焦点を当てるように比較者に指示します。

3. 2つのページ間の違いを強調表示した結果の比較文書は、'resultPdfPath'で指定されたファイルパスに保存されます。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## 全体文書の比較

2番目のコードスニペットは、2つのPDF文書の全体の内容を比較する範囲を拡大します。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

これらのスニペットによって生成された比較結果は、Adobe Acrobatのようなビューワーで開くことができるPDF文書です。Adobe Acrobatで2ページ表示を使用すると、変更が並べて表示されます：

- 削除 - これは左のページに記載されています。
- 挿入 - これは右のページに記載されています。

'AdditionalChangeMarks'を'true'に設定することで、現在表示されているページに変更がない場合でも、他のページで発生する可能性のある変更のマーカーを確認できます。

**Aspose.PDF for .NET**は、特定のページを比較する必要がある場合でも、全体文書を比較する必要がある場合でも、PDF文書を比較するための堅牢なツールを提供します。'AdditionalChangeMarks'やさまざまな'ComparisonMode設定'のようなオプションを使用することで、比較プロセスを特定のニーズに合わせて調整できます。結果の文書は、変更の明確な並べて表示を提供し、改訂を追跡し、文書の正確性を確保するのを容易にします。

## GraphicalPdfComparerを使用してPDF文書を比較する

文書でコラボレーションする際、特にプロフェッショナルな環境では、同じファイルの複数のバージョンができることがよくあります。

[GraphicalPdfComparer](https://reference.aspose.com/pdf/ja/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/)クラスを使用してPDF文書とページを比較できます。このクラスは、ページのグラフィックコンテンツの変更を比較するのに適しています。

Aspose.PDF for .NETを使用すると、文書とページを比較し、比較結果をPDF文書または画像ファイルに出力することができます。

次のクラスプロパティを設定できます：

- 解像度 - 出力画像および比較中に生成される画像のDPI単位での解像度。
- 色 - 変更マーカーの色。
- 閾値 - 変更の閾値（パーセント）。デフォルト値はゼロです。ゼロ以外の値を設定すると、あなたにとって重要でないグラフィックの変更を無視できます。

このクラスには、さらなる処理に適した形でページ画像の違いを取得するメソッドがあります：**ImagesDifference GetDifference(Page page1, Page page2)**。

このメソッドは、比較される最初のページの画像と違いの配列を含む[ImagesDifference](https://reference.aspose.com/pdf/ja/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/)クラスのオブジェクトを返します。違いの配列と元の画像は、**RGB24bpp**ピクセル形式です。

ImagesDifferenceを使用すると、異なる画像を生成し、違いの配列を元の画像に追加することで、比較される2番目のページの画像を取得できます。これを行うには、**ImagesDifference.GetDestinationImageおよびImagesDifference.DifferenceToImage**メソッドを使用します。

### GetDifferenceメソッドを使用してPDFを比較する

提供されたコードは、2つのPDF文書を比較し、それらの違いの視覚的表現を生成する[GetDifference](https://reference.aspose.com/pdf/ja/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods)メソッドを定義しています。

このメソッドは、2つのPDFファイルの最初のページを比較し、2つのPNG画像を生成します：

- 1つの画像（diffPngFilePath）は、ページ間の違いを赤で強調表示します。
- もう1つの画像（destPngFilePath）は、宛先（2番目の）PDFページの視覚的表現です。

このプロセスは、文書の2つのバージョン間の変更や違いを視覚的に比較するのに役立ちます。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### CompareDocumentsToPdfメソッドを使用してPDFを比較する

提供されたコードスニペットは、2つの文書を比較し、比較結果のPDFレポートを生成する[CompareDocumentsToPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/)メソッドを使用しています。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```