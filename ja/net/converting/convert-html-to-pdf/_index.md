---
title: HTMLをPDFに変換する .NET
linktitle: HTMLをPDFファイルに変換する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してHTMLをPDFおよびMHTMLをPDFに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "Aspose.PDF for .NETの変換機能により、HTMLおよびMHTMLドキュメントを高品質のPDFファイルにシームレスに変換できます。高度なカスタマイズオプションを使用することで、ユーザーはフォントの埋め込み、メディアクエリ、外部リソースの管理を制御でき、ウェブページやローカルHTMLファイルがPDF形式に正確にレンダリングされることを保証し、特定のニーズに合わせた柔軟性を提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 概要 

この記事では、**C#を使用してHTMLをPDFに変換する方法**を説明します。以下のトピックをカバーしています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

_形式_: **HTML**
- [C# HTMLをPDFに変換](#csharp-html-to-pdf)
- [C# HTMLをPDFに変換する](#csharp-html-to-pdf)
- [C# HTMLをPDFに変換する方法](#csharp-html-to-pdf)

_形式_: **MHTML**
- [C# MHTMLをPDFに変換](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFに変換する](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFに変換する方法](#csharp-mhtml-to-pdf)

_形式_: **Webページ**
- [C# WebページをPDFに変換](#csharp-webpage-to-pdf)
- [C# WebページをPDFに変換する](#csharp-webpage-to-pdf)
- [C# WebページをPDFに変換する方法](#csharp-webpage-to-pdf)

## C# HTMLをPDFに変換

**Aspose.PDF for .NET**は、既存のHTMLドキュメントをシームレスにPDFに変換できるPDF操作APIです。HTMLをPDFに変換するプロセスは柔軟にカスタマイズできます。

## HTMLをPDFに変換

以下のC#コードサンプルは、HTMLドキュメントをPDFに変換する方法を示しています。

<a name="csharp-html-to-pdf"><strong>手順: C#でHTMLをPDFに変換する</strong></a>

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/)クラスのインスタンスを作成します。
2. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)オブジェクトを初期化します。
3. **Document.Save()**メソッドを呼び出して出力PDFドキュメントを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**オンラインでHTMLをPDFに変換してみる**

Asposeは、機能と品質を調査できるオンライン無料アプリケーション["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)を提供しています。

[![Aspose.PDF HTMLをPDFに変換する無料アプリを使用](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## HTMLからPDFへの高度な変換

HTML変換エンジンには、変換プロセスを制御するためのいくつかのオプションがあります。

### メディアクエリのサポート

メディアクエリは、異なるデバイスに合わせたスタイルシートを提供するための一般的な手法です。デバイスタイプは[`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype)プロパティを使用して設定できます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### フォントの埋め込みを有効（無効）にする

HTMLページは、フォント（ローカルフォルダのフォント、Google Fontsなど）を使用することがよくあります。ドキュメント内のフォントの埋め込みを制御するために、[`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts)プロパティを使用することもできます。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### 外部リソースの読み込みを管理する

変換エンジンは、HTMLドキュメントに関連する特定のリソースの読み込みを制御するメカニズムを提供します。
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions)クラスには、リソースローダーの動作を定義できる[`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)プロパティがあります。
すべてのPNG画像を単一の画像`test.jpg`に置き換え、他のリソースの外部URLを内部に置き換える必要があると仮定します。
これを行うために、カスタムローダー`SamePictureLoader`を定義し、[`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)をこの名前にポイントします。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## ウェブページをPDFに変換

ウェブページを変換することは、ローカルHTMLドキュメントを変換することとは少し異なります。ウェブページの内容をPDF形式に変換するには、まずHttpClientインスタンスを使用してHTMLページの内容を取得し、Streamオブジェクトを作成し、その内容をDocumentオブジェクトに渡してPDF形式で出力をレンダリングします。

ウェブサーバーにホストされているウェブページをPDFに変換する場合：

<a name="csharp-webpage-to-pdf"><strong>手順: C#でWebページをPDFに変換する</strong></a>

1. HttpClientオブジェクトを使用してページの内容を読み取ります。
1. [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions)オブジェクトをインスタンス化し、ベースURLを設定します。
1. ストリームオブジェクトを渡しながらDocumentオブジェクトを初期化します。
1. 必要に応じて、ページサイズや向きを設定します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### ウェブページをPDFに変換するための資格情報を提供する

時々、認証とアクセス権が必要なHTMLファイルの変換を行う必要があります。これにより、認証されたユーザーのみがページの内容を取得できるようになります。また、HTML内で参照されるリソースやデータが外部サーバーから取得されるシナリオも含まれます。これに対応するために、[`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions)クラスに[`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials)プロパティが追加されました。以下のコードスニペットは、HTMLファイルをPDFに変換する際にHTMLおよびその関連リソースに資格情報を渡す手順を示しています。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### すべてのHTMLコンテンツを単一ページにレンダリングする

Aspose.PDF for .NETは、HTMLファイルをPDF形式に変換する際にすべてのコンテンツを単一ページにレンダリングする機能を提供します。たとえば、出力サイズが1ページを超えるHTMLコンテンツがある場合、出力データを単一のPDFページにレンダリングするオプションを使用できます。このオプションを使用するために、HtmlLoadOptionsクラスはIsRenderToSinglePageフラグで拡張されました。以下のコードスニペットは、この機能を使用する方法を示しています。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### SVGデータを含むHTMLをレンダリングする

Aspose.PDF for .NETは、HTMLページをPDFドキュメントに変換する機能を提供します。HTMLは、ページにSVGグラフィック要素をタグとして追加することを許可するため、Aspose.PDFもそのようなデータを結果のPDFファイルに変換することをサポートしています。以下のコードスニペットは、SVGグラフィックタグを含むHTMLファイルをタグ付きPDFドキュメントに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## MHTMLをPDFに変換 

{{% alert color="success" %}}
**オンラインでMHTMLをPDFに変換してみる**

Aspose.PDF for .NETは、機能と品質を調査できるオンライン無料アプリケーション["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)を提供しています。

[![Aspose.PDF MHTMLをPDFに変換する無料アプリを使用](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIMEで集約されたHTMLドキュメント">MHTML</abbr>は、MIME HTMLの略で、通常は外部リンク（画像、Flashアニメーション、Javaアプレット、音声ファイルなど）で表されるリソースをHTMLコードと組み合わせて単一のファイルにするために使用されるウェブページアーカイブ形式です。MHTMLファイルの内容は、MIMEタイプmultipart/relatedを使用して、HTMLメールメッセージのようにエンコードされます。Aspose.PDF for .NETは、HTMLファイルをPDF形式に変換でき、Aspose.PDF for .NET 9.0.0のリリースにより、MHTMLファイルをPDF形式に変換する新機能が導入されました。次のコードスニペットは、C#を使用してMHTMLファイルをPDF形式に変換する方法を示しています。

<a name="csharp-mhtml-to-pdf"><strong>手順: C#でMHTMLをPDFに変換する</strong></a>

1. [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/)クラスのインスタンスを作成します。
2. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)オブジェクトを初期化します。
3. **Document.Save()**メソッドを呼び出して出力PDFドキュメントを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## 参照 

この記事では、これらのトピックもカバーしています。コードは上記と同じです。

_形式_: **HTML**
- [C# HTMLをPDFに変換するコード](#csharp-html-to-pdf)
- [C# HTMLをPDFに変換するAPI](#csharp-html-to-pdf)
- [C# HTMLをPDFにプログラムで変換する](#csharp-html-to-pdf)
- [C# HTMLをPDFに変換するライブラリ](#csharp-html-to-pdf)
- [C# HTMLをPDFとして保存する](#csharp-html-to-pdf)
- [C# HTMLからPDFを生成する](#csharp-html-to-pdf)
- [C# HTMLからPDFを作成する](#csharp-html-to-pdf)
- [C# HTMLをPDFに変換するコンバータ](#csharp-html-to-pdf)

_形式_: **MHTML**
- [C# MHTMLをPDFに変換するコード](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFに変換するAPI](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFにプログラムで変換する](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFに変換するライブラリ](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFとして保存する](#csharp-mhtml-to-pdf)
- [C# MHTMLからPDFを生成する](#csharp-mhtml-to-pdf)
- [C# MHTMLからPDFを作成する](#csharp-mhtml-to-pdf)
- [C# MHTMLをPDFに変換するコンバータ](#csharp-mhtml-to-pdf)

_形式_: **ウェブページ**
- [C# WebページをPDFに変換するコード](#csharp-webpage-to-pdf)
- [C# WebページをPDFに変換するAPI](#csharp-webpage-to-pdf)
- [C# WebページをPDFにプログラムで変換する](#csharp-webpage-to-pdf)
- [C# WebページをPDFに変換するライブラリ](#csharp-webpage-to-pdf)
- [C# WebページをPDFとして保存する](#csharp-webpage-to-pdf)
- [C# WebページからPDFを生成する](#csharp-webpage-to-pdf)
- [C# WebページからPDFを作成する](#csharp-webpage-to-pdf)
- [C# WebページをPDFに変換するコンバータ](#csharp-webpage-to-pdf)