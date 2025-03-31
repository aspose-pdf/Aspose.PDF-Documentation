---
title: PDFページの抽出
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/extract-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを抽出する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "Aspose.PDF for .NET FacadesのExtract PDF Pages機能は、ユーザーがPDF文書からページを選択的に抽出するための強化された機能を提供します。PdfFileEditorクラスを利用することで、ユーザーはファイルパスまたはストリームを介して指定された範囲またはページのセットを効率的に抽出でき、文書操作がよりスムーズで柔軟になります。この機能は、元のファイルを変更せずにPDFコンテンツをカスタマイズしたいユーザーに特に有益です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## ファイルパスを使用して2つの番号の間のPDFページを抽出

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用すると、PDFファイルから指定されたページ範囲を抽出できます。このオーバーロードでは、ディスクからPDFファイルを操作しながらページを抽出できます。このオーバーロードには、入力ファイルパス、開始ページ、終了ページ、および出力ファイルパスのパラメータが必要です。開始ページから終了ページまでのページが抽出され、出力はディスクに保存されます。以下のコードスニペットは、ファイルパスを使用して2つの番号の間のPDFページを抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## ファイルパスを使用してPDFページの配列を抽出

範囲のページを抽出したくない場合、特定のページのセットを抽出することもできます。[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用すると、それも可能です。最初に、抽出する必要のあるすべてのページ番号を含む整数配列を作成する必要があります。この[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドのオーバーロードには、入力PDFファイル、抽出するページの整数配列、および出力PDFファイルのパラメータが必要です。以下のコードスニペットは、ファイルパスを使用してPDFページを抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## ストリームを使用して2つの番号の間のPDFページを抽出

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用すると、ストリームを使用してページの範囲を抽出できます。このオーバーロードには、次のパラメータを渡す必要があります：入力ストリーム、開始ページ、終了ページ、および出力ストリーム。開始ページと終了ページの間で指定された範囲のページが入力ストリームから抽出され、出力ストリームに保存されます。以下のコードスニペットは、ストリームを使用して2つの番号の間のPDFページを抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## ストリームを使用してPDFページの配列を抽出

PDFストリームからページの配列を抽出し、出力ストリームに保存するには、[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドの適切なオーバーロードを使用します。範囲のページを抽出したくない場合、特定のページのセットを抽出することもできます。[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドを使用すると、それも可能です。最初に、抽出する必要のあるすべてのページ番号を含む整数配列を作成する必要があります。この[Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index)メソッドのオーバーロードには、入力ストリーム、抽出するページの整数配列、および出力ストリームのパラメータが必要です。以下のコードスニペットは、ストリームを使用してPDFページを抽出する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```