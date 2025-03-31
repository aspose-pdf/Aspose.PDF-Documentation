---
title: .NETでさまざまな画像形式をPDFに変換
linktitle: 画像をPDFに変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: C# .NETを使用して、CDR、DJVU、BMP、CGM、JPEG、DICOM、PNG、TIFF、EMF、SVGなどのさまざまな画像形式をPDFに変換します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert various Images formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple Image Formats to PDF with C#",
    "abstract": "BMP、CGM、DICOM、EMF、JPG、PNG、SVG、TIFF、CDR、DJVUなどのさまざまな画像形式を高品質のPDF文書にシームレスに変換できる強力な機能をAspose.PDF for .NETで紹介します。この機能は、.NETアプリケーション内での画像からPDFへの変換を統合するための簡単な方法を提供し、多様なグラフィックコンテンツの効率的な処理を保証します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5228",
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
    "url": "/net/convert-images-format-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-images-format-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 概要

この記事では、C#を使用してさまざまな画像形式をPDFに変換する方法を説明します。これらのトピックをカバーしています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

_形式_: **BMP**
- [C# BMPをPDFに変換](#csharp-bmp-to-pdf)
- [C# BMPをPDFに変換する](#csharp-bmp-to-pdf)
- [C# BMP画像をPDFに変換する方法](#csharp-bmp-to-pdf)

_形式_: **CGM**
- [C# CGMをPDFに変換](#csharp-cgm-to-pdf)
- [C# CGMをPDFに変換する](#csharp-cgm-to-pdf)
- [C# CGM画像をPDFに変換する方法](#csharp-cgm-to-pdf)

_形式_: **DICOM**
- [C# DICOMをPDFに変換](#csharp-dicom-to-pdf)
- [C# DICOMをPDFに変換する](#csharp-dicom-to-pdf)
- [C# DICOM画像をPDFに変換する方法](#csharp-dicom-to-pdf)

_形式_: **EMF**
- [C# EMFをPDFに変換](#csharp-emf-to-pdf)
- [C# EMFをPDFに変換する](#csharp-emf-to-pdf)
- [C# EMF画像をPDFに変換する方法](#csharp-emf-to-pdf)

_形式_: **GIF**
- [C# GIFをPDFに変換](#csharp-gif-to-pdf)
- [C# GIFをPDFに変換する](#csharp-gif-to-pdf)
- [C# GIF画像をPDFに変換する方法](#csharp-gif-to-pdf)

_形式_: **JPG**
- [C# JPGをPDFに変換](#csharp-jpg-to-pdf)
- [C# JPGをPDFに変換する](#csharp-jpg-to-pdf)
- [C# JPG画像をPDFに変換する方法](#csharp-jpg-to-pdf)

_形式_: **PNG**
- [C# PNGをPDFに変換](#csharp-png-to-pdf)
- [C# PNGをPDFに変換する](#csharp-png-to-pdf)
- [C# PNG画像をPDFに変換する方法](#csharp-png-to-pdf)

_形式_: **SVG**
- [C# SVGをPDFに変換](#csharp-svg-to-pdf)
- [C# SVGをPDFに変換する](#csharp-svg-to-pdf)
- [C# SVG画像をPDFに変換する方法](#csharp-svg-to-pdf)

_形式_: **TIFF**
- [C# TIFFをPDFに変換](#csharp-tiff-to-pdf)
- [C# TIFFをPDFに変換する](#csharp-tiff-to-pdf)
- [C# TIFF画像をPDFに変換する方法](#csharp-tiff-to-pdf)

_形式_: **CDR**
- [C# CDRをPDFに変換](#csharp-cdr-to-pdf)
- [C# CDRをPDFに変換する](#csharp-cdr-to-pdf)
- [C# CDR画像をPDFに変換する方法](#csharp-cdr-to-pdf)

_形式_: **DJVU**
- [C# DJVUをPDFに変換](#csharp-djvu-to-pdf)
- [C# DJVUをPDFに変換する](#csharp-djvu-to-pdf)
- [C# DJVU画像をPDFに変換する方法](#csharp-djvu-to-pdf)

この記事でカバーされているその他のトピック
- [関連情報](#see-also)


## C# 画像をPDFに変換

**Aspose.PDF for .NET**は、さまざまな形式の画像をPDFファイルに変換することを可能にします。当社のライブラリは、BMP、CGM、DICOM、EMF、JPG、PNG、SVG、TIFF形式など、最も一般的な画像形式を変換するためのコードスニペットを示しています。

## BMPをPDFに変換

**Aspose.PDF for .NET**ライブラリを使用して、BMPファイルをPDF文書に変換します。

<abbr title="Bitmap Image File">BMP</abbr>画像は、拡張子を持つファイルです。BMPは、ビットマップデジタル画像を保存するために使用されるビットマップ画像ファイルを表します。これらの画像はグラフィックアダプタに依存せず、デバイス独立ビットマップ（DIB）ファイル形式とも呼ばれます。
Aspose.PDF for .NET APIを使用してBMPをPDFファイルに変換できます。したがって、BMP画像を変換するための次の手順に従うことができます。

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>手順: C#でBMPをPDFに変換する</strong></a>

1. 新しい[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスオブジェクトを初期化します。
2. 入力**BMP**画像を読み込みます。
3. 最後に、出力PDFファイルを保存します。

次のコードスニペットは、これらの手順に従い、C#を使用してBMPをPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertBMPtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load BMP file
        image.File = dataDir + "BMPtoPDF.bmp";
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "BMPtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**BMPをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF BMPをPDFに変換する無料アプリを使用](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGMをPDFに変換

<abbr title="Computer Graphics Metafile">CGM</abbr>は、CAD（コンピュータ支援設計）およびプレゼンテーショングラフィックスアプリケーションで一般的に使用されるコンピュータグラフィックスメタファイル形式のファイル拡張子です。CGMは、プログラムの読み取り速度に最適なバイナリ（最良）、最小のファイルサイズを生成し、データ転送を高速化する文字ベース、またはテキストエディタでファイルを読み取り、変更できるクリアテキストエンコーディングの3つの異なるエンコーディング方法をサポートするベクターグラフィックス形式です。

CGMファイルをPDF形式に変換するための次のコードスニペットを確認してください。

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>手順: C#でCGMをPDFに変換する</strong></a>

1. [CgmLoadOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/cgmloadoptions)クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスのインスタンスを作成します。
3. 希望のファイル名で文書を保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCGMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.CgmLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CGMtoPDF.cgm", option))
    {
        // Save PDF document
        document.Save(dataDir + "CGMtoPDF_out.pdf");
    }
}
```

## DICOMをPDFに変換

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>形式は、デジタル医療画像および検査された患者の文書の作成、保存、送信、視覚化のための医療業界標準です。

**Aspose.PDF for .NET**は、DICOMおよびSVG画像を変換することを可能にしますが、技術的な理由からPDFに追加する画像のタイプを指定する必要があります。

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>手順: C#でDICOMをPDFに変換する</strong></a>

1. Imageクラスのオブジェクトを作成します。
2. 画像をページの段落コレクションに追加します。
3. [FileType](https://reference.aspose.com/pdf/ja/net/aspose.pdf/image/properties/filetype)プロパティを指定します。
4. ファイルのパスまたはソースを指定します。
    - 画像がハードドライブの場所にある場合は、Image.Fileプロパティを使用してパスを指定します。
    - 画像がMemoryStreamに配置されている場合は、画像を保持するオブジェクトをImage.ImageStreamプロパティに渡します。

次のコードスニペットは、Aspose.PDFを使用してDICOMファイルをPDF形式に変換する方法を示しています。DICOM画像を読み込み、PDFファイルのページに画像を配置し、出力をPDFとして保存する必要があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDICOMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        
        var image = new Aspose.Pdf.Image
        {
            FileType = ImageFileType.Dicom,
            File = dataDir + "DICOMtoPDF.dcm"
        };
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "DICOMtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**DICOMをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF DICOMをPDFに変換する無料アプリを使用](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMFをPDFに変換

<abbr title="Enhanced metafile format">EMF</abbr>は、デバイスに依存しないグラフィカル画像を保存します。EMFのメタファイルは、保存された画像を出力デバイスでレンダリングできるようにするために、時系列で可変長のレコードで構成されています。さらに、以下の手順を使用してEMFをPDF画像に変換できます。

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>手順: C#でEMFをPDFに変換する</strong></a>

1. まず、[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスオブジェクトを初期化します。
2. **EMF**画像ファイルを読み込みます。
3. 読み込んだEMF画像をページに追加します。
4. PDF文書を保存します。

さらに、次のコードスニペットは、C#を使用してEMFをPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEMFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load EMF file
        image.File = dataDir + "EMFtoPDF.emf";

        // Specify page dimension properties
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Height = image.BitmapSize.Height;

        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "EMFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**EMFをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF EMFをPDFに変換する無料アプリを使用](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIFをPDFに変換

**Aspose.PDF for .NET**ライブラリを使用してGIFファイルをPDF文書に変換します。

<abbr title="Graphics Interchange Format">GIF</abbr>は、256色以下の形式で圧縮データを品質を損なうことなく保存することができます。ハードウェアに依存しないGIF形式は、1987年（GIF87a）にCompuServeによってビットマップ画像をネットワーク経由で送信するために開発されました。
Aspose.PDF for .NET APIを使用してGIFをPDFファイルに変換できます。したがって、GIF画像を変換するための次の手順に従うことができます。

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>手順: C#でGIFをPDFに変換する</strong></a>

1. 新しい[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスオブジェクトを初期化します。
2. 入力**GIF**画像を読み込みます。
3. 最後に、出力PDFファイルを保存します。

次のコードスニペットは、これらの手順に従い、C#を使用してGIFをPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertGIFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample GIF image file
        image.File = dataDir + "GIFtoPDF.gif";
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "GIFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**GIFをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF GIFをPDFに変換する無料アプリを使用](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## JPGをPDFに変換

JPGをPDFに変換する方法を考える必要はありません。なぜなら、**Aspose.PDF for .NET**ライブラリが最適な解決策を提供しているからです。

Aspose.PDF for .NETを使用してJPG画像をPDFに非常に簡単に変換できます。次の手順に従ってください。

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>手順: C#でJPGをPDFに変換する</strong></a>

1. [Document](https://reference.aspose.com/page/net/aspose.page/document)クラスのオブジェクトを初期化します。
2. PDF文書に新しいページを追加します。
3. **JPG**画像を読み込み、段落に追加します。
4. 出力PDFを保存します。

次のコードスニペットは、C#を使用してJPG画像をPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load input JPG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Add image on a page
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

次に、**ページの高さと幅が同じ**で画像をPDFに変換する方法を示します。画像の寸法を取得し、それに応じてPDF文書のページ寸法を設定します。

1. 入力画像ファイルを読み込みます。
1. ページの高さ、幅、およびマージンを設定します。
1. 出力PDFファイルを保存します。

次のコードスニペットは、C#を使用して同じページの高さと幅で画像をPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load JPEG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**JPGをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF JPGをPDFに変換する無料アプリを使用](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNGをPDFに変換

**Aspose.PDF for .NET**は、PNG画像をPDF形式に変換する機能をサポートしています。次のコードスニペットを確認して、タスクを実現してください。

<abbr title="Portable Network Graphics">PNG</abbr>は、ロスレス圧縮を使用するラスタ画像ファイル形式の一種であり、ユーザーの間で人気があります。

以下の手順を使用してPNGをPDF画像に変換できます。

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>手順: C#でPNGをPDFに変換する</strong></a>

1. 入力**PNG**画像を読み込みます。
2. 高さと幅の値を読み取ります。
3. 新しい[Document](https://reference.aspose.com/page/net/aspose.page/document)オブジェクトを作成し、ページを追加します。
4. ページの寸法を設定します。
5. 出力ファイルを保存します。

さらに、次のコードスニペットは、C#を使用して.NETアプリケーションでPNGをPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPNGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load PNG file
        image.File = dataDir + "PNGtoPDF.png";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "PNGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**PNGをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF PNGをPDFに変換する無料アプリを使用](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVGをPDFに変換

**Aspose.PDF for .NET**は、SVG画像をPDF形式に変換する方法と、ソース<abbr title="Scalable Vector Graphics">SVG</abbr>ファイルの寸法を取得する方法を説明します。

スケーラブルベクターグラフィックス（SVG）は、静的および動的（インタラクティブまたはアニメーション）の2次元ベクターグラフィックス用のXMLベースのファイル形式の仕様のファミリーです。SVG仕様は、1999年からWorld Wide Web Consortium（W3C）によって開発されているオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。これは、検索、インデックス作成、スクリプト化、必要に応じて圧縮できることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeなどの描画プログラムを使用して作成する方が便利です。

{{% alert color="success" %}}
**SVG形式をPDFにオンラインで変換してみてください**

Aspose.PDF for .NETは、オンライン無料アプリケーション["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF SVGをPDFに変換する無料アプリを使用](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

SVGファイルをPDFに変換するには、[`LoadOptions`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/loadoptions)オブジェクトを初期化するために使用される[SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions)というクラスを使用します。後で、このオブジェクトはDocumentオブジェクトの初期化中に引数として渡され、PDFレンダリングエンジンがソース文書の入力形式を決定するのに役立ちます。

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>手順: C#でSVGをPDFに変換する</strong></a>

1. [`SvgLoadOptions`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/loadoptions)クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して[`Document`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスのインスタンスを作成します。
3. 希望のファイル名で文書を保存します。

次のコードスニペットは、Aspose.PDF for .NETを使用してSVGファイルをPDF形式に変換するプロセスを示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.SvgLoadOptions();
    // Open SVG file 
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", option))
    {
        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
}
```

## SVGの寸法を取得

ソースSVGファイルの寸法を取得することも可能です。この情報は、SVGが出力PDFのページ全体をカバーする場合に役立ちます。SvgLoadOptionクラスのAdjustPageSizeプロパティがこの要件を満たします。このプロパティのデフォルト値はfalseです。値がtrueに設定されている場合、出力PDFはソースSVGと同じサイズ（寸法）になります。

次のコードスニペットは、ソースSVGファイルの寸法を取得し、PDFファイルを生成するプロセスを示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    var loadopt = new Aspose.Pdf.SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    // Open SVG file
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", loadopt))
    {
        document.Pages[1].PageInfo.Margin.Top = 0;
        document.Pages[1].PageInfo.Margin.Left = 0;
        document.Pages[1].PageInfo.Margin.Bottom = 0;
        document.Pages[1].PageInfo.Margin.Right = 0;

        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
    
}
```

### SVGのサポートされている機能

<table>
    <thead>
        <tr>
            <th>
                <p>SVGタグ</p>
            </th>
            <th>
                <p>サンプル使用</p>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>circle</p>
            </td>
            <td>
                <code><pre>&lt circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt </pre></code>
            </td>
        </tr>
        <tr>
            <td>
                <p>defs</p>
            </td>
            <td>
                <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                    stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                    cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                    &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                    x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                    x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                    x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
            </td>
        </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    参照された文字データ&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
                    text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    マスクされたテキスト&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ellipse&nbsp;</p>
            </td>
            <td>
                <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g&nbsp;</p>
            </td>
            <td>
                <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt;&nbsp; <br>
                    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
                    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
                    y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
                    <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>image</p>
            </td>
            <td>
                <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
                    /&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>line</p>
            </td>
            <td>
                <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>path</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>style</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polygon</p>
            </td>
            <td>
                <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
                    /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polyline</p>
            </td>
            <td>
                <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
                    -3,1 -3,-5"/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>rect&nbsp;</p>
            </td>
            <td>
                <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>svg</p>
            </td>
            <td>
                <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>text</p>
            </td>
            <td>
                <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
                    y="30" pointer-events="none"&gt;マップタイトル&lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>font</p>
            </td>
            <td>
                <p>&lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br>
                    &nbsp;&nbsp;&nbsp; サンプルテキスト&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tspan</p>
            </td>
            <td>
                <p>&lt;tspan dy="25" x="25"&gt;6つのインクカラー入力値。ここでは&lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>

## TIFFをPDFに変換

**Aspose.PDF**ファイル形式は、単一フレームまたはマルチフレーム<abbr title="Tag Image File Format">TIFF</abbr>画像をサポートしています。つまり、TIFF画像をPDFに変換することができます。

TIFFまたはTIF、タグ付き画像ファイル形式は、このファイル形式標準に準拠したさまざまなデバイスで使用されるラスタ画像を表します。TIFF画像は、異なる画像を持つ複数のフレームを含むことができます。Aspose.PDFファイル形式もサポートされており、単一フレームまたはマルチフレームTIFF画像を扱うことができます。

TIFFをPDFに変換する方法は、他のラスタファイル形式のグラフィックスと同様です。

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>手順: C#でTIFFをPDFに変換する</strong></a>

1. 新しい[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスオブジェクトを作成し、ページを追加します。
2. 入力**TIFF**画像を読み込みます。
3. PDF文書を保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample Tiff image file
        image.File = dataDir + "TIFFtoPDF.tiff";
        document.Pages[1].Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

マルチページTIFF画像をマルチページPDF文書に変換し、幅やアスペクト比などのパラメータを制御する必要がある場合は、次の手順に従ってください。

1. Documentクラスのインスタンスを作成します。
1. 入力TIFF画像を読み込みます。
1. フレームのFrameDimensionを取得します。
1. 各フレームのために新しいページを追加します。
1. 最後に、画像をPDFページに保存します。

次のコードスニペットは、C#を使用してマルチページまたはマルチフレームTIFF画像をPDFに変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        using (var bitmap = new System.Drawing.Bitmap(File.OpenRead(dataDir + "TIFFtoPDF.tif")))
        {
            // Convert multi page or multi frame TIFF to PDF
            var dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
            var frameCount = bitmap.GetFrameCount(dimension);

            // Iterate through each frame
            for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
            {
                var page = document.Pages.Add();

                bitmap.SelectActiveFrame(dimension, frameIdx);

                using (var currentImage = new MemoryStream())
                {
                    bitmap.Save(currentImage, ImageFormat.Tiff);

                    var imageht = new Aspose.Pdf.Image
                    {
                        ImageStream = currentImage,
                        //Apply some other options
                        //ImageScale = 0.5
                    };
                    page.Paragraphs.Add(imageht);
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

## CDRをPDFに変換

<abbr title="CDR">CDR</abbr>は、Corel Corporationによって開発されたファイル形式で、主にベクターグラフィック画像や図面に使用されます。CDRファイル形式は、ほとんどの画像編集プログラムによって認識されます。CDR形式は、Corel Drawアプリケーションのデフォルト形式です。

CDRファイルをPDF形式に変換するための次のコードスニペットを確認してください。

<a name="csharp-cdr-to-pdf" id="csharp-cdr-to-pdf"><strong>手順: C#でCDRをPDFに変換する</strong></a>

1. [CdrLoadOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/cdrloadoptions/)クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスのインスタンスを作成します。
3. 希望のファイル名で文書を保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCDRtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open CDR file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.cdr", new CdrLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## DJVUをPDFに変換

<abbr title="DJVU">DjVu</abbr>は、LizardTechによって開発された圧縮画像形式です。このファイル形式は、特にテキスト、画像、インデックス付きカラー画像、線画の組み合わせを含むさまざまな種類のスキャンされた文書を保存するために設計されました。

DJVUファイルをPDF形式に変換するための次のコードスニペットを確認してください。

<a name="csharp-djvu-to-pdf" id="csharp-djvu-to-pdf"><strong>手順: C#でDJVUをPDFに変換する</strong></a>

1. [DjvuLoadOptions](https://reference.aspose.com/pdf/ja/net/aspose.pdf/djvuloadoptions/)クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)クラスのインスタンスを作成します。
3. 希望のファイル名で文書を保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDJVUtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open DJVU file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.djvu", new DjvuLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## HEICをPDFに変換

HEICファイルは、高効率コンテナ画像ファイル形式で、複数の画像を単一のファイルにコレクションとして保存できます。
HEIC画像を読み込むには、https://www.nuget.org/packages/FileFormat.Heic/ nugetパッケージへの参照を追加する必要があります。
Aspose.PDFを使用してHEIC画像をPDFに変換します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```

## 適用対象

|**プラットフォーム**|**サポート**|**コメント**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## 関連情報

この記事では、これらのトピックもカバーしています。コードは上記と同じです。

_形式_: **BMP**
- [C# BMPをPDFに変換するコード](#csharp-bmp-to-pdf)
- [C# BMPをPDFに変換するAPI](#csharp-bmp-to-pdf)
- [C# BMPをPDFにプログラムで変換する](#csharp-bmp-to-pdf)
- [C# BMPをPDFに変換するライブラリ](#csharp-bmp-to-pdf)
- [C# BMPをPDFとして保存する](#csharp-bmp-to-pdf)
- [C# BMPからPDFを生成する](#csharp-bmp-to-pdf)
- [C# BMPからPDFを作成する](#csharp-bmp-to-pdf)
- [C# BMPをPDFに変換するコンバータ](#csharp-bmp-to-pdf)

_形式_: **CGM**
- [C# CGMをPDFに変換するコード](#csharp-cgm-to-pdf)
- [C# CGMをPDFに変換するAPI](#csharp-cgm-to-pdf)
- [C# CGMをPDFにプログラムで変換する](#csharp-cgm-to-pdf)
- [C# CGMをPDFに変換するライブラリ](#csharp-cgm-to-pdf)
- [C# CGMをPDFとして保存する](#csharp-cgm-to-pdf)
- [C# CGMからPDFを生成する](#csharp-cgm-to-pdf)
- [C# CGMからPDFを作成する](#csharp-cgm-to-pdf)
- [C# CGMをPDFに変換するコンバータ](#csharp-cgm-to-pdf)

_形式_: **DICOM**
- [C# DICOMをPDFに変換するコード](#csharp-dicom-to-pdf)
- [C# DICOMをPDFに変換するAPI](#csharp-dicom-to-pdf)
- [C# DICOMをPDFにプログラムで変換する](#csharp-dicom-to-pdf)
- [C# DICOMをPDFに変換するライブラリ](#csharp-dicom-to-pdf)
- [C# DICOMをPDFとして保存する](#csharp-dicom-to-pdf)
- [C# DICOMからPDFを生成する](#csharp-dicom-to-pdf)
- [C# DICOMからPDFを作成する](#csharp-dicom-to-pdf)
- [C# DICOMをPDFに変換するコンバータ](#csharp-dicom-to-pdf)

_形式_: **EMF**
- [C# EMFをPDFに変換するコード](#csharp-emf-to-pdf)
- [C# EMFをPDFに変換するAPI](#csharp-emf-to-pdf)
- [C# EMFをPDFにプログラムで変換する](#csharp-emf-to-pdf)
- [C# EMFをPDFに変換するライブラリ](#csharp-emf-to-pdf)
- [C# EMFをPDFとして保存する](#csharp-emf-to-pdf)
- [C# EMFからPDFを生成する](#csharp-emf-to-pdf)
- [C# EMFからPDFを作成する](#csharp-emf-to-pdf)
- [C# EMFをPDFに変換するコンバータ](#csharp-emf-to-pdf)

_形式_: **DjVu**
- [C# DjVuをPDFに変換するコード](#csharp-djvu-to-pdf)
- [C# DjVuをPDFに変換するAPI](#csharp-djvu-to-pdf)
- [C# DjVuをPDFにプログラムで変換する](#csharp-djvu-to-pdf)
- [C# DjVuをPDFに変換するライブラリ](#csharp-djvu-to-pdf)
- [C# DjVuをPDFとして保存する](#csharp-djvu-to-pdf)
- [C# DjVuからPDFを生成する](#csharp-djvu-to-pdf)
- [C# DjVuからPDFを作成する](#csharp-djvu-to-pdf)
- [C# DjVuをPDFに変換するコンバータ](#csharp-djvu-to-pdf)

_形式_: **CDR**
- [C# CDRをPDFに変換するコード](#csharp-cdr-to-pdf)
- [C# CDRをPDFに変換するAPI](#csharp-cdr-to-pdf)
- [C# CDRをPDFにプログラムで変換する](#csharp-cdr-to-pdf)
- [C# CDRをPDFに変換するライブラリ](#csharp-cdr-to-pdf)
- [C# CDRをPDFとして保存する](#csharp-cdr-to-pdf)
- [C# CDRからPDFを生成する](#csharp-cdr-to-pdf)
- [C# CDRからPDFを作成する](#csharp-cdr-to-pdf)
- [C# CDRをPDFに変換するコンバータ](#csharp-cdr-to-pdf)