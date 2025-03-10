---
title: PDFをHTMLに変換する .NET
linktitle: PDFをHTML形式に変換する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDF C#ライブラリを使用してPDFファイルをHTML形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "PDF文書をHTML形式にシームレスに変換する強力な新機能をAspose.PDF for .NETで紹介します。この機能は、マルチページ出力、SVG画像管理、透明テキストレンダリングのオプションをサポートしており、開発者はわずか数行のC#コードでPDFをWeb準備済みのコンテンツに簡単に変換できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1368",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの機能を確認してください。"
}
</script>

## 概要

この記事では、**C#を使用してPDFをHTMLに変換する方法**を説明します。以下のトピックをカバーしています。

_形式_: **HTML**
- [C# PDFをHTMLに変換](#csharp-pdf-to-html)
- [C# PDFをHTMLに変換する](#csharp-pdf-to-html)
- [C# PDFファイルをHTMLに変換する方法](#csharp-pdf-to-html)

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## PDFをHTMLに変換

**Aspose.PDF for .NET**は、さまざまなファイル形式をPDF文書に変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。この記事では、PDFファイルを<abbr title="HyperText Markup Language">HTML</abbr>に変換する方法について説明します。Aspose.PDF for .NETは、InLineHtmlアプローチを使用してHTMLファイルをPDF形式に変換する機能を提供します。PDFファイルをHTML形式に変換する機能に関する多くのリクエストがあり、この機能を提供しました。この機能はXHTML 1.0もサポートしています。

**Aspose.PDF for .NET**は、PDFファイルをHTMLに変換する機能をサポートしています。Aspose.PDFライブラリで達成できる主なタスクは以下の通りです。

- PDFをHTMLに変換する。
- 出力をマルチページHTMLに分割する。
- SVGファイルを保存するフォルダーを指定する。
- 変換中にSVG画像を圧縮する。
- 画像をPNG背景として保存する。
- 画像フォルダーを指定する。
- 本文コンテンツのみを持つ後続ファイルを作成する。
- 透明テキストのレンダリング。
- PDF文書のレイヤーのレンダリング。

{{% alert color="success" %}}
**PDFをHTMLにオンラインで変換してみる**

Aspose.PDF for .NETは、機能と品質を調査するために試すことができるオンライン無料アプリケーション["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)を提供します。

[![Aspose.PDF PDFをHTMLに変換する無料アプリ](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NETは、ソースPDFファイルをHTMLに変換するための2行のコードを提供します。[`SaveFormat列挙型`](https://reference.aspose.com/pdf/net/aspose.pdf/saveformat)には、ソースファイルをHTMLとして保存するための値Htmlが含まれています。以下のコードスニペットは、PDFファイルをHTMLに変換するプロセスを示しています。

<a name="csharp-pdf-to-html"><strong>手順: C#でPDFをHTMLに変換する</strong></a>

1. ソースPDF文書を持つ[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Document.Save()**メソッドを呼び出して、**SaveFormat.Html**形式で保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### 出力をマルチページHTMLに分割する

複数ページの大きなPDFファイルをHTML形式に変換する際、出力は単一のHTMLページとして表示されます。非常に長くなる可能性があります。ページサイズを制御するために、PDFからHTMLへの変換中に出力を複数ページに分割することが可能です。以下のコードスニペットを使用してみてください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### SVGファイルを保存するフォルダーを指定する

PDFからHTMLへの変換中に、SVG画像を保存するフォルダーを指定することが可能です。[`HtmlSaveOptionクラス`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions)の[`SpecialFolderForSvgImagesプロパティ`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages)を使用して、特別なSVG画像ディレクトリを指定します。このプロパティは、変換中に遭遇したSVG画像を保存するディレクトリへのパスを取得または設定します。パラメーターが空またはnullの場合、SVGファイルは他の画像ファイルと一緒に保存されます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### 変換中にSVG画像を圧縮する

PDFからHTMLへの変換中にSVG画像を圧縮するには、以下のコードを使用してみてください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### 画像をPNG背景として保存する

画像を保存するためのデフォルトの出力形式はSVGです。変換中に、PDFからの一部の画像はSVGベクター画像に変換されます。これは遅くなる可能性があります。代わりに、各ページのために1つのPNG背景ファイルに変換することができます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### 画像を保存するフォルダーを指定する

PDFからHTMLへの変換中に、画像を保存するフォルダーを指定することもできます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### 本文コンテンツのみを持つ後続ファイルを作成する

最近、PDFファイルをHTMLに変換し、ユーザーが各ページの`<body>`タグの内容のみを取得できる機能を導入するよう求められました。これにより、CSS、`<html>`、`<head>`の詳細を持つ1つのファイルと、他のファイルには`<body>`の内容のみが含まれることになります。

この要件を満たすために、HtmlSaveOptionsクラスに新しいプロパティHtmlMarkupGenerationModeが導入されました。

以下の簡単なコードスニペットを使用すると、出力HTMLをページに分割できます。出力ページでは、すべてのHTMLオブジェクトは現在の位置に正確に配置される必要があります（フォント処理と出力、CSS作成と出力、画像作成と出力）。ただし、このアプローチを使用する場合、CSSへのリンクはあなたのコードの責任です。なぜなら、`<link>`のようなものは削除されるからです。この目的のために、File.ReadAllText()を介してCSSを読み取り、AJAXを介してWebページに送信し、jQueryによって適用されるようにすることができます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### 透明テキストのレンダリング

ソースPDFファイルに前景画像によって影が付けられた透明テキストが含まれている場合、テキストレンダリングの問題が発生する可能性があります。このようなシナリオに対応するために、SaveShadowedTextsAsTransparentTextsおよびSaveTransparentTextsプロパティを使用できます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### PDF文書のレイヤーのレンダリング

PDFからHTMLへの変換中に、PDF文書のレイヤーを別のレイヤータイプの要素としてレンダリングできます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```

## 関連情報

この記事では、以下のトピックもカバーしています。コードは上記と同じです。

_形式_: **HTML**
- [C# PDFをHTMLに変換するコード](#csharp-pdf-to-html)
- [C# PDFをHTMLに変換するAPI](#csharp-pdf-to-html)
- [C# PDFをHTMLにプログラムで変換する](#csharp-pdf-to-html)
- [C# PDFをHTMLに変換するライブラリ](#csharp-pdf-to-html)
- [C# PDFをHTMLとして保存する](#csharp-pdf-to-html)
- [C# PDFからHTMLを生成する](#csharp-pdf-to-html)
- [C# PDFからHTMLを作成する](#csharp-pdf-to-html)
- [C# PDFをHTMLコンバータ](#csharp-pdf-to-html)