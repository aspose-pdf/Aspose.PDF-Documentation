---
title: Convert text to PDF
linktitle: Convert text to PDF
type: docs
weight: 20
url: /net/convert-text-to-pdf/
lastmod: "2020-12-16"
description: Aspose.PDF for .NET allows you to convert plain text file to PDF or to convert pre-formatted text file to PDF. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** support the feature converting plain text and pre-formatted text file to PDF format. 

Converting text to PDF means adding text fragments to the PDF page. As for text files, we are dealing with 2 types of text: pre-formatting (for example, 25 lines with 80 characters per line) and non-formatted text (plain text). Depending on our needs, we can control this addition ourselves or entrust it to the library's algorithms.

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

## Convert plain text file to PDF

In case of the plain text file, we can use the following technique:

1. use a TextReader to read the whole text;
1. instantiate Document object and add a new page in Pages collection;
1. create a new object of TextFragment and pass TextReader object to its constructor;
1. add TextFragment object as paragraph in Paragraphs collection. If the amount of text is larger than the page, library algorithm automatically adds extra pages;
1. use Save method of Document class;

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Read the source text file
TextReader tr = new StreamReader(dataDir + "log.txt");

// Instantiate a Document object by calling its empty constructor
Document pdfDocument= new Document();

// Add a new page in Pages collection of Document
Page page = pdfDocument.Pages.Add();

// Create an instance of TextFragmet and pass the text from reader object to its constructor as argument
TextFragment text = new TextFragment(tr.ReadToEnd());

// Add a new text paragraph in paragraphs collection and pass the TextFragment object
page.Paragraphs.Add(text);

// Save resultant PDF file
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```

## Convert pre-formatted text file to PDF

Converting pre-formatted text is like plain text but you need to make some additional actions such as setting margins, font type and size. Obviously that font should be monospace (Courier New).

Follow these steps to convert pre-formatted text to PDF with C#:

1. Read the whole text as an array of strings;
1. Instantiate Document object and add a new page in Pages collection;
1. Run loop through an array of strings and add each string as a paragraph in Paragraph collection

In this case, the library's algorithm also adds extra pages, but we can control this process ourselves.
Following example shows how to convert pre-formatted text file (80x25) to PDF document with page size A4.

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // Read the text file as array of string
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // Instantiate a Document object by calling its empty constructor
    Document pdfDocument= new Document();

    // Add a new page in Pages collection of Document
    Page page = pdfDocument.Pages.Add();

    // Set left and right margins for better presentation
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // check if line contains "form feed" character
        // see https://en.wikipedia.org/wiki/Page_break
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // Create an instance of TextFragment and
            // pass the line to its
            // constructor as argument
            TextFragment text = new TextFragment(line);

            // Add a new text paragraph in paragraphs collection and pass the TextFragment object
            page.Paragraphs.Add(text);
        }
    }

    // Save resultant PDF file
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
