---
title: PDFページの分割
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/split-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを分割する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "Aspose.PDF for .NETの新しいPDFページ分割機能により、ユーザーはPdfFileEditorクラスを使用してPDFドキュメントをさまざまなセグメントに効率的に分割できます。この機能は、最初のページから指定されたページまでの分割、大量セットへの分割、さらには個々のページの分離をサポートし、ファイルパスまたはストリームを介してPDF操作の多様なオプションを提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## ファイルパスを使用して最初からPDFページを分割

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、指定されたページ番号で終了する最初のページからPDFファイルを分割することができます。ディスクからPDFファイルを操作したい場合は、このメソッドに入力および出力PDFファイルのファイルパスを渡すことができます。以下のコードスニペットは、ファイルパスを使用して最初からPDFページを分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## ファイルストリームを使用して最初からPDFページを分割

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、指定されたページ番号で終了する最初のページからPDFファイルを分割することができます。ストリームからPDFファイルを操作したい場合は、このメソッドに入力および出力PDFストリームを渡すことができます。以下のコードスニペットは、ファイルストリームを使用して最初からPDFページを分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## ファイルパスを使用してPDFページをバルクに分割

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、PDFファイルを複数のページセットに分割することができます。この例では、2つのページセット（1, 2）と（5, 6）が必要です。ディスクからPDFファイルにアクセスする場合は、入力PDFをファイルパスとして渡す必要があります。このメソッドはMemoryStreamの配列を返します。この配列をループして、個々のページセットを別々のファイルとして保存できます。以下のコードスニペットは、ファイルパスを使用してPDFページをバルクに分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## ストリームを使用してPDFページをバルクに分割

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、PDFファイルを複数のページセットに分割することができます。この例では、2つのページセット（1, 2）と（5, 6）が必要です。ディスクからファイルにアクセスする代わりに、このメソッドにストリームを渡すことができます。このメソッドはMemoryStreamの配列を返します。この配列をループして、個々のページセットを別々のファイルとして保存できます。以下のコードスニペットは、ストリームを使用してPDFページをバルクに分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## ファイルパスを使用してPDFページを最後まで分割

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittoend/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、指定されたページ番号からPDFファイルの最後まで分割し、新しいPDFとして保存することができます。これを行うには、ファイルパスを使用して、入力および出力ファイルパスと分割を開始するページ番号を渡す必要があります。出力PDFはディスクに保存されます。以下のコードスニペットは、ファイルパスを使用してPDFページを最後まで分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## ストリームを使用してPDFページを最後まで分割

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittoend/index) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスのもので、指定されたページ番号からPDFファイルの最後まで分割し、新しいPDFとして保存することができます。これを行うには、ストリームを使用して、入力および出力ストリームと分割を開始するページ番号を渡す必要があります。出力PDFは出力ストリームに保存されます。以下のコードスニペットは、ストリームを使用してPDFページを最後まで分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## ファイルパスを使用してPDFを個々のページに分割

{{% alert color="primary" %}}

PDFドキュメントを分割して、結果をオンラインで表示することができます。このリンクをクリックしてください：

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

PDFファイルを個々のページに分割するには、[SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) メソッドにPDFをファイルパスとして渡す必要があります。このメソッドは、PDFファイルの個々のページを含むMemoryStreamの配列を返します。このMemoryStreamの配列をループして、個々のページを別々のPDFファイルとしてディスクに保存できます。以下のコードスニペットは、ファイルパスを使用してPDFを個々のページに分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## ストリームを使用してPDFを個々のページに分割

PDFファイルを個々のページに分割するには、[SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) メソッドにPDFをストリームとして渡す必要があります。このメソッドは、PDFファイルの個々のページを含むMemoryStreamの配列を返します。このMemoryStreamの配列をループして、個々のページを別々のPDFファイルとしてディスクに保存することも、後でアプリケーションで使用するためにメモリストリームに保持することもできます。以下のコードスニペットは、ストリームを使用してPDFを個々のページに分割する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```