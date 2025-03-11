---
title: PDFページの挿入
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/insert-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを挿入する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Aspose.PDF for .NET PdfFileEditorクラスを使用して、1つのPDFから別のPDFに特定のページを挿入する新機能でPDF管理を最適化します。この機能は、範囲ベースおよび配列ベースのページ挿入をサポートし、ファイルパスまたはストリームを介してドキュメントをシームレスに結合することでワークフローの効率を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## ファイルパスを使用して2つの番号の間にPDFページを挿入する

特定のページ範囲を1つのPDFから別のPDFに挿入するには、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)メソッドを使用します。そのためには、ページを挿入したい入力PDFファイル、挿入のためにページを取得するポートファイル、ページを挿入する場所、ポートファイルの挿入する必要があるページ範囲が必要です。この範囲は、開始ページと終了ページのパラメータで指定されます。最後に、指定されたページ範囲が挿入された出力PDFファイルが保存されます。以下のコードスニペットは、ファイルストリームを使用して2つの番号の間にPDFページを挿入する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## ファイルパスを使用してPDFページの配列を挿入する

特定のページを別のPDFファイルに挿入したい場合は、ページの整数配列を必要とする[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)メソッドのオーバーロードを使用できます。この配列では、入力PDFファイルに挿入したい特定のページを指定できます。そのためには、ページを挿入したい入力PDFファイル、挿入のためにページを取得するポートファイル、ページを挿入する場所、入力PDFファイルに挿入する必要があるポートファイルのページの整数配列が必要です。この配列には、入力PDFファイルに挿入したい特定のページのリストが含まれています。最後に、指定されたページの配列が挿入された出力PDFファイルが保存されます。以下のコードスニペットは、ファイルパスを使用してPDFページの配列を挿入する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## ストリームを使用して2つの番号の間にPDFページを挿入する

ストリームを使用してページ範囲を挿入したい場合は、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index)メソッドの適切なオーバーロードを使用するだけです。そのためには、ページを挿入したい入力PDFストリーム、挿入のためにページを取得するポートストリーム、ページを挿入する場所、入力PDFストリームに挿入する必要があるポートストリームのページ範囲が必要です。この範囲は、開始ページと終了ページのパラメータで指定されます。最後に、指定されたページ範囲が挿入された出力PDFストリームが保存されます。以下のコードスニペットは、ストリームを使用して2つの番号の間にPDFページを挿入する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## ストリームを使用してPDFページの配列を挿入する

ストリームを使用して、ページの配列を別のPDFファイルに挿入することもできます。これは、ページの整数配列を必要とするInsertメソッドの適切なオーバーロードを使用することで実現できます。この配列では、入力PDFストリームに挿入したい特定のページを指定できます。そのためには、ページを挿入したい入力PDFストリーム、挿入のためにページを取得するポートストリーム、ページを挿入する場所、入力PDFファイルに挿入する必要があるポートストリームのページの整数配列が必要です。この配列には、入力PDFストリームに挿入したい特定のページのリストが含まれています。最後に、指定されたページの配列が挿入された出力PDFストリームが保存されます。以下のコードスニペットは、ストリームを使用してPDFページの配列を挿入する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```