---
title: Extract Text from PDF File
type: docs
weight: 30
url: /net/extract-text/
description: This section explains how to extract text from pdf using PdfExtractor class.
lastmod: "2021-06-05"
---

In this article, we’ll look into the details of extracting text from a PDF file. All of these extraction features are provided at one place, in [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class. We’ll see how to use these features in our code.

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class provides three types of extraction capabilities. These three categories are Text, Images and Attachments. In order to perform extraction under each of these three categories PdfExtractor provide various methods which work together to give you the final output.

For example, in order to extract text you can use three methods i.e. [ExtractText, GetText, HasNextPageText and GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). Now, in order to start extracting text, first of all, you need to call [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index) method; this will extract the text from the PDF file and will store it into memory. After that, [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) method will take this extracted text and save on to the disk at specified location in a file. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) helps you loop through each page and check whether the next page has any text or not. If it contains some text then [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) will help you save the text of an individual page into the file.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Create an object of the PdfExtractor class
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Bind the input PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtractText
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extract the text into separate files
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```

To Extract the Text Extraction Mode use the following code:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // Create an object of the PdfExtractor class
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Bind the input PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtractText
    // pdfExtractor.ExtractTextMode = 0; //pure mode
    pdfExtractor.ExtractTextMode = 1; //raw mode
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extract the text into separate files
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
