---
title: PDFをMicrosoft Word文書に変換する方法（.NET）
linktitle: PDFをWordに変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: PDFをMicrosoft Word形式に変換するためのC#コードの書き方を学び、PDFからDOC（DOCX）への変換を調整します。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NETは、C#を使用してPDFファイルをMicrosoft Word形式（DOCおよびDOCX）に変換するための強力な機能を紹介します。この機能は、文書の編集を向上させるだけでなく、テキスト認識とフォーマットの柔軟なオプションを提供し、元のPDFと結果のWord文書の間の高い忠実度を確保します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1495",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 概要

この記事では、**C#を使用してPDFをMicrosoft Word文書に変換する方法**について説明します。以下のトピックをカバーしています。

_形式_: **DOC**

- [C# PDFをDOCに変換](#csharp-pdf-to-doc)
- [C# PDFをDOCに変換する方法](#csharp-pdf-to-doc)

_形式_: **DOCX**

- [C# PDFをDOCXに変換](#csharp-pdf-to-docx)
- [C# PDFをDOCXに変換する方法](#csharp-pdf-to-docx)

_形式_: **Word**

- [C# PDFをWordに変換](#csharp-pdf-to-docx)
- [C# PDFをWordに変換する方法](#csharp-pdf-to-doc)

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## PDFからDOCおよびDOCXへの変換

最も人気のある機能の1つは、PDFからMicrosoft Word DOCへの変換であり、コンテンツ管理をより簡単にします。**Aspose.PDF for .NET**を使用すると、PDFファイルをDOCおよびDOCX形式に迅速かつ効率的に変換できます。

## PDFをDOC（Microsoft Word 97-2003）ファイルに変換

PDFファイルをDOC形式に簡単に変換し、完全な制御を行います。Aspose.PDF for .NETは柔軟で、さまざまな変換をサポートしています。たとえば、PDF文書のページを画像に変換することは非常に人気のある機能です。

多くの顧客がPDFからDOCへの変換をリクエストしています。PDFファイルをMicrosoft Word文書に変換することです。顧客は、PDFファイルは簡単に編集できないのに対し、Word文書は編集可能であるため、これを望んでいます。一部の企業は、ユーザーがPDFとして始まったファイル内のテキスト、表、画像を操作できるようにしたいと考えています。

物事をシンプルで理解しやすくする伝統を守り、Aspose.PDF for .NETを使用すると、ソースPDFファイルを2行のコードでDOCファイルに変換できます。この機能を実現するために、SaveFormatという列挙型を導入し、その値.Docを使用してソースファイルをMicrosoft Word形式に保存できます。

以下のC#コードスニペットは、PDFファイルをDOC形式に変換する方法を示しています。

<a name="csharp-pdf-to-doc"><strong>手順: C#でPDFをDOCに変換する</strong></a>

1. ソースPDF文書を使用して[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Document.Save()**メソッドを呼び出して、**SaveFormat.Doc**形式で保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### DocSaveOptionsクラスの使用

[`DocSaveOptions`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/docsaveoptions)クラスは、PDFファイルをDOC形式に変換するための多数のプロパティを提供します。これらのプロパティの中で、ModeはPDFコンテンツの認識モードを指定するために使用できます。このプロパティには、RecognitionMode列挙型から任意の値を選択できます。これらの値にはそれぞれ特定の利点と制限があります。

- [`Textbox`](https://reference.aspose.com/pdf/ja/net/aspose.pdf.docsaveoptions/recognitionmode)モードは高速で、PDFファイルの元の外観を保持するのに適していますが、結果の文書の編集可能性は制限される可能性があります。元のPDF内の視覚的にグループ化されたテキストブロックは、出力文書内のテキストボックスに変換されます。これにより、元の文書に最大限似た出力文書が得られますが、出力文書は完全にテキストボックスで構成されており、Microsoft Wordで編集するのは非常に難しいです。
- [`Flow`](https://reference.aspose.com/pdf/ja/net/aspose.pdf.docsaveoptions/recognitionmode)は完全認識モードであり、エンジンがグループ化と多層分析を実行して、著者の意図に従って元の文書を復元し、簡単に編集可能な文書を生成します。制限は、出力文書が元の文書とは異なる外観になる可能性があることです。

[`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity)プロパティは、テキスト要素間の相対的な近接性を制御するために使用できます。これは、距離がフォントサイズによって規定されることを意味します。大きなフォントは音節間に大きなスペースを持つことができ、依然として1つの全体と見なされます。これはフォントサイズのパーセンテージとして指定されます。たとえば、1 = 100%です。これは、12ptの2文字が12pt離れて配置されている場合、近接していることを意味します。
- [`RecognitionBullets`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/docsaveoptions/properties/recognizebullets)は、変換中に箇条書きの認識をオンにするために使用されます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみる**

Aspose.PDF for .NETは、オンラインの無料アプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、機能と品質を調査することができます。

[![PDFをDOCに変換](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCX（Microsoft Word 2007-2024）ファイルに変換

Aspose.PDF for .NET APIを使用すると、C#および任意の.NET言語を使用してPDF文書をDOCXに読み取り、変換できます。DOCXは、Microsoft Word文書のためのよく知られた形式で、その構造はプレーンバイナリからXMLとバイナリファイルの組み合わせに変更されました。DocxファイルはWord 2007以降のバージョンで開くことができますが、以前のバージョンのMS WordではDOCファイル拡張子をサポートしていません。

以下のC#コードスニペットは、PDFファイルをDOCX形式に変換する方法を示しています。

<a name="csharp-pdf-to-docx"><strong>手順: C#でPDFをDOCXに変換する</strong></a>

1. ソースPDF文書を使用して[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. **Document.Save()**メソッドを呼び出して、**SaveFormat.DocX**形式で保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### 拡張モードでPDFをDOCXに変換

PDFからDOCXへの変換の結果を向上させるために、`EnhancedFlow`モードを使用できます。
FlowとEnhanced Flowの主な違いは、テーブル（境界線の有無にかかわらず）が実際のテーブルとして認識され、背景に画像があるテキストとしてではないことです。
番号付きリストやその他の多くの小さな要素も認識されます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換してみる**

Aspose.PDF for .NETは、オンラインの無料アプリケーション["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF PDFからWordへの変換無料アプリ](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 関連情報

この記事では、以下のトピックもカバーしています。コードは上記と同じです。

_形式_: **Word**

- [C# PDFをWordに変換するコード](#csharp-pdf-to-docx)
- [C# PDFをWordに変換するAPI](#csharp-pdf-to-docx)
- [C# PDFをWordにプログラムで変換する](#csharp-pdf-to-docx)
- [C# PDFをWordライブラリ](#csharp-pdf-to-docx)
- [C# PDFをWordとして保存](#csharp-pdf-to-docx)
- [C# PDFからWordを生成](#csharp-pdf-to-docx)
- [C# PDFからWordを作成](#csharp-pdf-to-docx)
- [C# PDFをWordに変換する](#csharp-pdf-to-docx)

_形式_: **DOC**

- [C# PDFをDOCに変換するコード](#csharp-pdf-to-doc)
- [C# PDFをDOCに変換するAPI](#csharp-pdf-to-doc)
- [C# PDFをDOCにプログラムで変換する](#csharp-pdf-to-doc)
- [C# PDFをDOCライブラリ](#csharp-pdf-to-doc)
- [C# PDFをDOCとして保存](#csharp-pdf-to-doc)
- [C# PDFからDOCを生成](#csharp-pdf-to-doc)
- [C# PDFからDOCを作成](#csharp-pdf-to-doc)
- [C# PDFをDOCに変換する](#csharp-pdf-to-doc)

_形式_: **DOCX**

- [C# PDFをDOCXに変換するコード](#csharp-pdf-to-docx)
- [C# PDFをDOCXに変換するAPI](#csharp-pdf-to-docx)
- [C# PDFをDOCXにプログラムで変換する](#csharp-pdf-to-docx)
- [C# PDFをDOCXライブラリ](#csharp-pdf-to-docx)
- [C# PDFをDOCXとして保存](#csharp-pdf-to-docx)
- [C# PDFからDOCXを生成](#csharp-pdf-to-docx)
- [C# PDFからDOCXを作成](#csharp-pdf-to-docx)
- [C# PDFをDOCXに変換する](#csharp-pdf-to-docx)