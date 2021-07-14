---
title: Extract PDF pages
type: docs
weight: 40
url: /net/extract-pdf-pages/
description: This section explains how to extract PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2021-06-05"
draft: false
---

## Extract PDF Pages between Two Numbers Using File Paths

[Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method of [PdfFileEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to extract specified range of pages from a PDF file. This overload allows you to extract pages while manipulating the PDF files from the disk. This overload requires following parameters: intput file path, start page, end page, and output file path. The pages from the start page to end page will be extracted and output will be saved on the disk.The following code snippet shows you how to extract PDF pages between two numbers using file paths.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extract Array of PDF Pages Using File Paths

If you do not want to extract a range of pages, rather a set of particular pages, [Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method allows you to do that as well. You first need to create an integer array with all the page numbers which need to be extracted. This overload of [Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method takes following parameters: input PDF file, integer array of pages to be extracted, and output PDF file. The following code snippet shows you how to extract PDF pages using file paths.

```csharp
public static void Extract_PDFPages_Streams()
{
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // Extract pages
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## Extract PDF Pages between Two Numbers Using Streams

[Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method of [PdfFileEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to extract a range of pages using streams. You need to pass the following paramteres to this overload: intput stream, start page, end page, and output stream. The pages specified by the range between start page and end page will be extracted from the intput stream and saved to the output stream.The following code snippet shows you how to extract PDF pages between two numbers using streams.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extract Array of PDF Pages Using Streams

An array of pages can be extracted from the PDF stream and saved in the output stream using appropriate overload of [Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method. If you do not want to extract a range of pages, rather a set of particular pages, [Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method allows you to do that as well. You first need to create an integer array with all the page numbers which need to be extracted. This overload of [Extract](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) method takes following parameters: input stream, integer array of pages to be extracted and output stream.
The following code snippet shows you how to extract PDF pages using streams.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extract pages
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```
