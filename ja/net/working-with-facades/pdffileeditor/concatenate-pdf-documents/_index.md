---
title: C#でPDFドキュメントを連結する
linktitle: PDFドキュメントを連結する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/concatenate-pdf-documents/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFドキュメントを連結する方法を説明します。
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "Aspose.PDF for .NETの機能により、開発者はC#のPdfFileEditorクラスを使用して複数のPDFドキュメントを効率的に連結できます。この機能は、ファイルパスやMemoryStreamsを介してファイルをマージし、PDFフォーム内のフィールド名をユニークに保ち、最終ドキュメント内に目次を生成することをサポートし、ドキュメント管理と統合のための効率的なソリューションを提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
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
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## **概要**

この記事では、C#を使用して異なるPDFファイルを単一のPDFにマージ、結合、または連結する方法を説明します。以下のトピックをカバーしています。

- [C#でPDFファイルをマージする](#concatenate-pdf-files-using-file-paths)
- [C#でPDFファイルを結合する](#concatenate-pdf-files-using-file-paths)
- [C#で複数のPDFファイルを1つのPDFにマージする](#concatenate-array-of-pdf-files-using-file-paths)
- [C#で複数のPDFファイルを1つのPDFに結合する](#concatenate-array-of-pdf-files-using-file-paths)
- [C#でフォルダー内のすべてのPDFファイルをマージする](#concatenating-all-pdf-files-in-particular-folder)
- [C#でフォルダー内のすべてのPDFファイルを結合する](#concatenating-all-pdf-files-in-particular-folder)
- [C#でファイルパスを使用してPDFファイルをマージする](#concatenate-pdf-files-using-file-paths)
- [C#でストリームを使用してPDFファイルを結合する](#concatenate-array-of-pdf-files-using-streams)
- [C#でフォルダー内のすべてのPDFファイルを連結する](#concatenate-pdf-files-in-folder)

## ファイルパスを使用してPDFファイルを連結する

[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)は、複数のPDFファイルを連結するための[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades)のクラスです。ファイルストリームを使用してファイルを連結するだけでなく、メモリストリームを使用しても連結できます。この記事では、メモリストリームを使用してファイルを連結するプロセスを説明し、コードスニペットを使用して示します。

[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)クラスの[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドを使用して、2つのPDFファイルを連結できます。[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドでは、最初の入力PDF、2番目の入力PDF、および出力PDFの3つのパラメーターを渡すことができます。最終的な出力PDFには、両方の入力PDFファイルが含まれます。

以下のC#コードスニペットは、ファイルパスを使用してPDFファイルを連結する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

場合によっては、多くのアウトラインがある場合、ユーザーはCopyOutlinesをfalseに設定して、連結のパフォーマンスを向上させることができます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf", dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## メモリストリームを使用して複数のPDFファイルを連結する

[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)クラスの[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドは、ソースPDFファイルと宛先PDFファイルをパラメーターとして受け取ります。これらのパラメーターは、ディスク上のPDFファイルへのパスであるか、メモリストリームである可能性があります。この例では、最初に2つのファイルストリームを作成して、ディスクからPDFファイルを読み取ります。次に、これらのファイルをバイト配列に変換します。PDFファイルのバイト配列はメモリストリームに変換されます。PDFファイルからメモリストリームを取得したら、それらを連結メソッドに渡して、単一の出力ファイルにマージできます。

以下のC#コードスニペットは、メモリストリームを使用して複数のPDFファイルを連結する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    string document1Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf";
    string document2Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        using (var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write))
                        {
                            // Write byte array contents in the output file stream
                            output.Write(data, 0, data.Length);
                        }
                    }
                }
            }
        }
    }
}
```

## ファイルパスを使用してPDFファイルの配列を連結する

複数のPDFファイルを連結したい場合は、PDFファイルの配列を渡すことができる[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドのオーバーロードを使用できます。最終的な出力は、配列内のすべてのファイルから作成されたマージファイルとして保存されます。以下のC#コードスニペットは、ファイルパスを使用してPDFファイルの配列を連結する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "Concatenate1.pdf";
    filesArray[1] = dataDir + "Concatenate2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## ストリームを使用してPDFファイルの配列を連結する

PDFファイルの配列を連結することは、ディスク上に存在するファイルに限られません。ストリームからPDFファイルの配列を連結することもできます。複数のPDFファイルを連結したい場合は、[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドの適切なオーバーロードを使用できます。最初に、入力ストリームの配列と出力PDF用の1つのストリームを作成し、次に[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドを呼び出します。出力は出力ストリームに保存されます。以下のC#コードスニペットは、ストリームを使用してPDFファイルの配列を連結する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    var document1Path = dataDir + "Concatenate1.pdf";
    var document2Path = dataDir + "Concatenate2.pdf";
    var resultPdfPath = dataDir + "ConcatenateArrayOfPdfUsingStreams_out.pdf";

    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Output stream
    using (var outputStream = new FileStream(resultPdfPath, FileMode.Create))
    {
        using (var stream1 = new FileStream(document1Path, FileMode.Open))
        {
            using (var stream2 = new FileStream(document2Path, FileMode.Open))
            {
                // Array of streams
                var inputStreams = new Stream[2];
                inputStreams[0] = stream1;
                inputStreams[1] = stream2;
                // Concatenate file
                pdfEditor.Concatenate(inputStreams, outputStream);
            }   
        }
    }
}
```

## 特定のフォルダー内のすべてのPDFファイルを連結する

特定のフォルダー内のすべてのPDFファイルをランタイムで読み取り、ファイル名を知らなくても連結することができます。連結したいPDFドキュメントを含むディレクトリのパスを提供してください。

この機能を実現するために、以下のC#コードスニペットを使用してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatingAllPdfFilesInParticularFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    var fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    var resultPdfPath = dataDir + "ConcatenatingAllPdfFilesInParticularFolder_out.pdf";
    // Instantiate PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, resultPdfPath);
}
```

## PDFフォームを連結し、フィールド名をユニークに保つ

[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades)の[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)クラスは、PDFファイルを連結する機能を提供します。連結するPDFファイルに同じフィールド名を持つフォームフィールドがある場合、Aspose.PDFは、結果のPDFファイル内のフィールドをユニークに保つ機能を提供し、フィールド名をユニークにするためのサフィックスを指定することもできます。[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)の[KeepFieldsUnique](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique)プロパティをtrueに設定すると、PDFフォームが連結されるときにフィールド名がユニークになります。また、[UniqueSuffix](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix)プロパティを使用して、フォームが連結されるときにフィールド名をユニークにするために追加されるサフィックスのユーザー定義形式を指定できます。この文字列には、結果のファイル内の数字に置き換えられる`%NUM%`サブストリングが含まれている必要があります。

この機能を実現するための簡単なコードスニペットを以下に示します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFormsAndKeepFieldsUnique()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf";
    var inputFile2 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf";
    var outFile = dataDir + "ConcatenatePDFForms_out.pdf";
    // Open PDF documents
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // To keep unique field Id for all the fields 
    fileEditor.KeepFieldsUnique = true;
    // Format of the suffix which is added to field name to make it unique when forms are concatenated.
    fileEditor.UniqueSuffix = "_%NUM%";
    // Concatenate the files into a resultant Pdf file
    fileEditor.Concatenate(inputFile1, inputFile2, outFile);
}
```

## PDFファイルを連結し、目次を作成する

## PDFファイルを連結する

PDFファイルをマージする方法についての情報は、以下のコードスニペットを参照してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenateInput1.pdf";
    var inputFile2 = dataDir + "ConcatenateInput2.pdf";
    var outFile = dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf";
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    // Open PDF documents
    using (var outputStream = new FileStream(outFile, FileMode.Create))
    {
        using (var stream1 = new FileStream(inputFile1, FileMode.Open))
        {
            using (var stream2 = new FileStream(inputFile2, FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(stream1, stream2, outputStream);
            }
        }
    }
}
```

### 空白ページを挿入する

PDFファイルがマージされた後、目次を作成するための空白ページをドキュメントの先頭に挿入できます。この要件を達成するために、マージされたファイルを**Document**オブジェクトにロードし、Page.Insert(...)メソッドを呼び出して空白ページを挿入する必要があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertBlankPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Insert a blank page at the beginning of concatenated file to display Table of Contents
    using (var document = new Aspose.Pdf.Document(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"))
    {
        // Insert a blank page in a PDF
        document.Pages.Insert(1);
    }
}
```

### テキストスタンプを追加する

目次を作成するために、最初のページに[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)および[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp)オブジェクトを使用してテキストスタンプを追加する必要があります。Stampクラスは、[FormattedText](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formattedtext)を追加するための`BindLogo(...)`メソッドを提供し、`SetOrigin(..)`メソッドを使用してこれらのテキストスタンプを追加する位置を指定できます。この記事では、2つのPDFファイルを連結しているため、これらの個々のドキュメントを指す2つのテキストスタンプオブジェクトを作成する必要があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampForTableOfContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    var inputPdfFile = Path.Combine(dataDir, "ConcatenateInput1.pdf");
    // Set Text Stamp to display string Table Of Contents
    var stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent, Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(inputPdfFile).GetPageWidth(1) / 3, 700);
    // Set particular pages
    stamp.Pages = new[] { 1 };
}
```

### ローカルリンクを作成する

次に、連結されたファイル内のページへのリンクを追加する必要があります。この要件を達成するために、[PdfContentEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor)クラスの`CreateLocalLink(..)`メソッドを使用できます。以下のコードスニペットでは、リンクの周りの矩形が表示されないように、4番目の引数としてTransparentを渡しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLocalLinks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Now we need to add Heading for Table Of Contents and links for documents
    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
    // Bind PDF document
    contentEditor.BindPdf(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf");
    // Create link for first document
    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
}
```

### 完全なコード

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CompleteCode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create a MemoryStream object to hold the resultant PDf file
    using (var concatenatedStream = new MemoryStream())
    {
        using (var fs1 = new FileStream(dataDir + "ConcatenateInput1.pdf", FileMode.Open))
        {
            using (var fs2 = new FileStream(dataDir + "ConcatenateInput2.pdf", FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(fs1, fs2, concatenatedStream);
            }
        }

        using (var concatenatedPdfDocument = new Aspose.Pdf.Document(concatenatedStream))
        {
            // Insert a blank page at the beginning of concatenated file to display Table of Contents
            concatenatedPdfDocument.Pages.Insert(1);

            // Hold the result file with empty page added
            using (var documentWithBlankPage = new MemoryStream())
            {
                // Save PDF document
                concatenatedPdfDocument.Save(documentWithBlankPage);

                using (var documentWithTocHeading = new MemoryStream())
                {
                    // Add Table Of Contents logo as stamp to PDF file
                    var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp();
                    // Bind PDF document
                    fileStamp.BindPdf(documentWithBlankPage);

                    // Set Text Stamp to display string Table Of Contents
                    var stamp = new Aspose.Pdf.Facades.Stamp();
                    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(documentWithBlankPage).GetPageWidth(1) / 3, 700);
                    // Set particular pages
                    stamp.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(stamp);

                    // Create stamp text for first item in Table Of Contents
                    var document1Link = new Aspose.Pdf.Facades.Stamp();
                    document1Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("1 - Link to Document 1", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document1Link.SetOrigin(150, 650);
                    // Set particular pages on which stamp should be displayed
                    document1Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document1Link);

                    // Create stamp text for second item in Table Of Contents
                    var document2Link = new Aspose.Pdf.Facades.Stamp();
                    document2Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("2 - Link to Document 2", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document2Link.SetOrigin(150, 620);
                    // Set particular pages on which stamp should be displayed
                    document2Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document2Link);

                    // Save PDF document
                    fileStamp.Save(documentWithTocHeading);
                    fileStamp.Close();

                    // Now we need to add Heading for Table Of Contents and links for documents
                    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
                    // Bind PDF document
                    contentEditor.BindPdf(documentWithTocHeading);
                    // Create link for first document
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
                    // Create link for Second document
                    // We have used   new PdfFileInfo("d:/pdftest/Input1.pdf").NumberOfPages + 2   as PdfFileInfo.NumberOfPages(..) returns the page count for first document
                    // And 2 is because, second document will start at Input1+1 and 1 for the page containing Table Of Contents.
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 620, 100, 20),
                        new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "ConcatenateInput1.pdf").NumberOfPages + 2, 1, System.Drawing.Color.Transparent);
                    // Save PDF document
                    contentEditor.Save(dataDir + "Concatenated_Table_Of_Contents_out.pdf");
                }
            }
        }
    }
}
```

## フォルダー内のPDFファイルを連結する

[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades)の[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)クラスは、PDFファイルを連結する機能を提供します。特定のフォルダー内のすべてのPDFファイルをランタイムで読み取り、ファイル名を知らなくても連結することができます。連結したいPDFドキュメントを含むディレクトリのパスを提供してください。

この機能を実現するために、以下のC#コードスニペットを使用してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "ConcatenatePdfFilesInFolder_out.pdf");
}
```