---
title: PDFのブックレットを作成する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ja/net/make-booklet-of-pdf/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDFでPDFのブックレットを作成する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "Aspose.PDFのPDFのブックレット作成機能を使用すると、PdfFileEditorクラスを利用してPDFファイルから簡単にブックレットを作成できます。この機能はファイルパスとストリームの両方をサポートしており、ページサイズのカスタマイズや出力制御を強化するための左ページと右ページの指定が可能です。この強力なツールはブックレット作成プロセスを効率化し、PDF操作のための必須リソースとなります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## ファイルパスを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFファイルのブックレットを作成し、出力PDFファイルに保存することができます。このオーバーロードを使用すると、ファイルパスを使用してブックレットを作成できます。以下のコードスニペットは、ファイルパスを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## ページサイズとファイルパスを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFファイルのブックレットを作成し、出力PDFファイルに保存することができます。このオーバーロードを使用すると、ファイルパスを使用してブックレットを作成できます。また、このオーバーロードを使用して出力PDFファイルのページサイズを設定することもできます。以下のコードスニペットは、ページサイズとファイルパスを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## ページサイズ、指定された左ページと右ページ、およびファイルパスを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFファイルのブックレットを作成し、出力PDFファイルに保存することができます。このオーバーロードを使用すると、ファイルパスを使用してブックレットを作成できます。また、このオーバーロードを使用して出力PDFファイルのページサイズを設定し、出力PDFファイルの左側と右側に特定のページを指定することもできます。以下のコードスニペットは、ページサイズ、指定された左ページと右ページ、およびファイルパスを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## 指定された左ページと右ページ、およびファイルパスを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFファイルのブックレットを作成し、出力PDFファイルに保存することができます。このオーバーロードを使用すると、ファイルパスを使用してブックレットを作成できます。また、このオーバーロードを使用して出力PDFファイルの左側と右側に特定のページを指定することもできます。以下のコードスニペットは、指定された左ページと右ページ、およびファイルパスを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## ストリームを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFストリームのブックレットを作成し、出力PDFストリームに保存することができます。このオーバーロードを使用すると、ファイルパスの代わりにストリームを使用してブックレットを作成できます。以下のコードスニペットは、ストリームを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## ページサイズとストリームを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFストリームのブックレットを作成し、出力PDFストリームに保存することができます。このオーバーロードを使用すると、ファイルパスの代わりにストリームを使用してブックレットを作成できます。また、このオーバーロードを使用して出力PDFストリームのページサイズを設定することもできます。以下のコードスニペットは、ページサイズとストリームを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## ページサイズ、指定された左ページと右ページ、およびストリームを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFストリームのブックレットを作成し、出力PDFストリームに保存することができます。このオーバーロードを使用すると、ファイルパスの代わりにストリームを使用してブックレットを作成できます。また、このオーバーロードを使用して出力PDFファイルのページサイズを設定し、出力PDFストリームの左側と右側に特定のページを指定することもできます。以下のコードスニペットは、ページサイズ、指定された左ページと右ページ、およびストリームを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## 指定された左ページと右ページ、およびストリームを使用してPDFのブックレットを作成する

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、入力PDFストリームのブックレットを作成し、出力PDFストリームに保存することができます。このオーバーロードを使用すると、ファイルパスの代わりにストリームを使用してブックレットを作成できます。また、このオーバーロードを使用して出力PDFストリームの左側と右側に特定のページを指定することもできます。以下のコードスニペットは、指定された左ページと右ページ、およびストリームを使用してブックレットを作成する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```