---
title: PDFをEPUB、LaTeX、テキスト、XPSに変換するC#
linktitle: PDFを他のフォーマットに変換する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ja/net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
description: このトピックでは、C#または.NETを使用してPDFファイルをEPUB、LaTeX、テキスト、XPSなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to EPUB, LaTeX, Text, XPS in C#",
    "alternativeHeadline": "Add PDF format conversion to EPUB, LaTeX, Text, XPS in C#",
    "abstract": "Aspose.PDF for .NETは、PDFファイルをEPUB、LaTeX、テキスト、XPS、Markdownなどのさまざまなフォーマットにシームレスに変換できる強力な機能を紹介します。この機能により、開発者はC#アプリケーションに多様なファイル形式の変換を簡単に統合できるため、より広いオーディエンスに対応し、さまざまなプラットフォーム向けにコンテンツを最適化できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1419",
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
    "url": "/net/convert-pdf-to-other-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-other-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFをEPUBに変換

{{% alert color="success" %}}
**PDFをEPUBにオンラインで変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査するために使用できるオンライン無料アプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供します。

[![Aspose.PDF PDFをEPUBに変換する無料アプリ](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="電子出版">EPUB</abbr>**は、国際デジタル出版フォーラム（IDPF）からの無料でオープンな電子書籍標準です。ファイルの拡張子は.epubです。
EPUBは再フロー可能なコンテンツのために設計されており、EPUBリーダーは特定の表示デバイスに最適化されたテキストを提供できます。EPUBは固定レイアウトのコンテンツもサポートしています。このフォーマットは、出版社や変換業者が社内で使用するため、また配布や販売のために使用できる単一のフォーマットとして意図されています。これはOpen eBook標準を置き換えます。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

Aspose.PDF for .NETは、PDFドキュメントをEPUB形式に変換する機能もサポートしています。Aspose.PDF for .NETには、[`Document.Save(..)`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save/index)メソッドの第二引数として使用できるEpubSaveOptionsというクラスがあります。これを使用してEPUBファイルを生成します。
次のコードスニペットを使用して、C#でこの要件を達成してみてください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoEPUB()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToEPUB.pdf"))
    {
        // Instantiate Epub Save options
        EpubSaveOptions options = new EpubSaveOptions();
        // Specify the layout for contents
        options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;

        // Save ePUB document
        document.Save(dataDir + "PDFToEPUB_out.epub", options);
    }
}
```

## PDFをLaTeX/TeXに変換

**Aspose.PDF for .NET**は、PDFをLaTeX/TeXに変換することをサポートしています。
LaTeXファイル形式は、特別なマークアップを持つテキストファイル形式であり、高品質な組版のためのTeXベースの文書作成システムで使用されます。

{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査するために使用できるオンライン無料アプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供します。

[![Aspose.PDF PDFをLaTeX/TeXに変換する無料アプリ](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDFファイルをTeXに変換するために、Aspose.PDFには、変換プロセス中に一時画像を保存するためのプロパティOutDirectoryPathを提供する[LaTeXSaveOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/latexsaveoptions)というクラスがあります。

次のコードスニペットは、C#を使用してPDFファイルをTEX形式に変換するプロセスを示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTeX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf"))
    {
        // Instantiate LaTex save option          
        LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

        // Specify the output directory
        string pathToOutputDirectory = dataDir;

        // Set the output directory path for save option object
        saveOptions.OutDirectoryPath = pathToOutputDirectory;

        // Save PDF document into LaTex format           
        document.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
    }
}
```

## PDFをテキストに変換

**Aspose.PDF for .NET**は、PDFドキュメント全体と単一ページをテキストファイルに変換することをサポートしています。

### PDFドキュメント全体をテキストファイルに変換

[TextAbsorber](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textabsorber)クラスの[Visit](https://reference.aspose.com/pdf/ja/net/aspose.pdf.text/textabsorber/methods/visit/index)メソッドを使用して、PDFドキュメントをTXTファイルに変換できます。

次のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        ta.Visit(document);

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt",ta.Text);
    }
}
```

{{% alert color="success" %}}
**PDFをテキストにオンラインで変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査するために使用できるオンライン無料アプリケーション["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)を提供します。

[![Aspose.PDF PDFをテキストに変換する無料アプリ](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### PDFページをテキストファイルに変換

Aspose.PDF for .NETを使用してPDFドキュメントをTXTファイルに変換できます。このタスクを解決するために、`TextAbsorber`クラスの`Visit`メソッドを使用する必要があります。

次のコードスニペットは、特定のページからテキストを抽出する方法を説明しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTXT()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var ta = new Aspose.Pdf.Text.TextAbsorber();
        var pages = new [] {1, 3, 4};
        foreach (var page in pages)
        {
            ta.Visit(document.Pages[page]);
        }
    
        // Save the extracted text in text file
        File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", ta.Text);
    }
}
```

## PDFをXPSに変換

**Aspose.PDF for .NET**は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する機能を提供します。C#を使用してPDFファイルをXPS形式に変換するために、提示されたコードスニペットを使用してみましょう。

{{% alert color="success" %}}
**PDFをXPSにオンラインで変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査するために使用できるオンライン無料アプリケーション["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)を提供します。

[![Aspose.PDF PDFをXPSに変換する無料アプリ](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイルタイプは、主にマイクロソフト社のXML Paper Specificationに関連付けられています。XML Paper Specification（XPS）は、以前はMetroというコード名で知られ、次世代印刷パス（NGPP）マーケティングコンセプトを包含するもので、文書作成と表示をWindowsオペレーティングシステムに統合するためのマイクロソフトの取り組みです。

PDFファイルをXPSに変換するために、Aspose.PDFには、XPSファイルを生成するために[Document.Save(..)](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save/index)メソッドの第二引数として使用される[XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions)というクラスがあります。

24.2リリース以降、Aspose.PDFは、結果のXPSでテキストを選択可能に保ちながら、検索可能なPDFをXPSに変換する機能を実装しました。テキストを保持するためには、XpsSaveOptions.SaveTransparentTextsプロパティをtrueに設定する必要があります。

次のコードスニペットは、PDFファイルをXPS形式に変換するプロセスを示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoXPS()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        var xpsOptions = new XpsSaveOptions
        {
            SaveTransparentTexts = true
        };

        // Save XPS document
        document.Save(dataDir + "PDFtoXPS_out.xps", xpsOptions);
    }
}
```

## PDFをMarkdownに変換

**Aspose.PDF for .NET**は、PDFファイルを<abbr title="Markdown">MD</abbr>形式に変換する機能を提供します。C#を使用してPDFファイルをMD形式に変換するために、提示されたコードスニペットを使用してみましょう。

Markdownは、最大限の人間の可読性と機械可読性を持つプレーンテキストフォーマットを表現するために設計された軽量マークアップ言語です。

### PDFからMarkdownコンバータによる画像使用の最適化

画像を含むディレクトリでは、画像の数がPDFファイル内の画像の数よりも少ないことに気付くでしょう。

Markdownファイルでは画像サイズを設定できないため、MarkdownSaveOptions.UseImageHtmlTagオプションなしでは、同じ種類の画像が異なるサイズで保存されます。

MarkdownSaveOptions.UseImageHtmlTagオプションを有効にすると、文書内でimgタグによってスケーリングされたユニークな画像が保存されます。

このコードは、PDFドキュメントを開き、Markdownファイルに変換するためのパラメータを設定し（"images"という名前のフォルダに画像を保存）、指定された出力パスに結果のMarkdownファイルを保存します。

次のコードスニペットは、PDFファイルをMD形式に変換するプロセスを示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        }
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options   
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

### PDFをMobiXmlに変換

MobiXMLは、モバイルプラットフォームで使用するために設計された人気のある電子書籍フォーマットです。
次のコードスニペットは、PDFドキュメントをMobiXMLファイルに変換する方法を説明しています。
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void ConvertPdfToMobiXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToXML.pdf"))
    {
        // Save PDF document in XML format
        document.Save(dataDir + "PDFToXML_out.xml", Aspose.Pdf.SaveFormat.MobiXml);
    }
}
```