---
title: Manipulate PDF Document in C#
linktitle: Manipulate PDF Document
type: docs
weight: 30
url: /net/manipulate-pdf-document/
description: This article contains information on how to validate PDF Document for PDF A Standard, how to work with TOC, how to set PDF expiry date, and etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate PDF Document",
    "alternativeHeadline": "How to manipulate PDF file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, dotnet, manipulate pdf file",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "This article contains information on how to validate PDF Document for PDF A Standard, how to work with TOC, how to set PDF expiry date, and etc."
}
</script>

## **Manipulate PDF Document in C#**

## Validate PDF Document for PDF A Standard (A 1A and A 1B)

To validate a PDF document for PDF/A-1a or PDF/A-1b compatibility, use the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class Validate method. This method allows you to specify the name of the file in which the result is to be saved and the required validation type [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) enumeration : PDF_A_1A or PDF_A_1B.

{{% alert color="primary" %}}

The output XML format is custom Aspose format. The XML contains a collection of tags with the name Problem; each tag contains the details of a particular problem. The Problem tag's ObjectID attribute represents the ID of the particular object this problem is related to. The Clause attribute represents a corresponding rule in the PDF specification.

{{% /alert %}}

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following code snippet shows you how to validate PDF document for PDF/A-1A.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document document = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validate PDF for PDF/A-1a
document.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

The following code snippet shows you how to validate PDF document for PDF/A-1b.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document document = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validate PDF for PDF/A-1b
document.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

{{% alert color="primary" %}}

Aspose.PDF for .NET can be used to determine if the loaded document is a valid PDF and also [if its encrypted or not](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). In order to further extend the capabilities of Document class, *IsPdfaCompliant* property is added to determine if the input file is PDF/A compliant and a property named *PdfaFormat* to identify the PDF/A format are introduced.

{{% /alert %}}

## Working with TOC

### Add TOC to Existing PDF

Aspose.PDF API allows you to add a table of content either when creating a PDF, or to an existing file. The ListSection class in the Aspose.Pdf.Generator namespace allows you to create a table of contents when creating a PDF from scratch. To add headings, which are elements of the TOC, use the Aspose.Pdf.Generator.Heading class.

To add a TOC to an existing PDF file, use the Heading class in the Aspose.PDF namespace. The Aspose.Pdf namespace can both create new and manipulate existing PDF files. To add a TOC to an existing PDF, use the Aspose.PDF namespace. The following code snippet shows how to create a table of contents inside an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Load an existing PDF files
Document document = new Document(dataDir + "AddTOC.pdf");

// Get access to first page of PDF file
Page tocPage = document.Pages.Insert(1);

// Create object to represent TOC information
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table Of Contents");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// Set the title for TOC
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// Create string objects which will be used as TOC elements
string[] titles = new string[4];
titles[0] = "First page";
titles[1] = "Second page";
titles[2] = "Third page";
titles[3] = "Fourth page";
for (int i = 0; i < 2; i++)
{
    // Create Heading object
    Heading heading2 = new Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Specify the destination page for heading object
    heading2.DestinationPage = document.Pages[i + 2];

    // Destination page
    heading2.Top = document.Pages[i + 2].Rect.Height;

    // Destination coordinate
    segment2.Text = titles[i];

    // Add heading to page containing TOC
    tocPage.Paragraphs.Add(heading2);
}

// Save the updated document
document.Save(dataDir + "TOC_out.pdf");
```

### Set different TabLeaderType for different TOC Levels

Aspose.PDF also allows setting different TabLeaderType for different TOC levels. You need to set LineDash property of FormatArray with the appropriate value of TabLeaderType enum as following.

```csharp
string outFile = "TOC.pdf";

Document document = new Document();
Page tocPage = document.Pages.Add();
TocInfo tocInfo = new TocInfo();

// Set LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("Table Of Contents");
title.TextState.FontSize = 30;
tocInfo.Title = title;

// Add the list section to the sections collection of the Pdf document
tocPage.TocInfo = tocInfo;
// Define the format of the four levels list by setting the left margins
// and text format settings of each level

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

// Create a section in the Pdf document
Page page = document.Pages.Add();

// Add four headings in the section
for (int Level = 1; Level <= 4; Level++)
{
    Heading heading2 = new Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "Sample Heading" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    // Add the heading into Table Of Contents.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// Save the Pdf
document.Save(outFile);
```

### Hide Page Numbers in TOC

In case if you do not want to display page numbers, along with the headings in TOC, you can use [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) property of [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) Class as false. Please check following code snippet to hide page numbers in the table of contents:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document document = new Document();
Page tocPage = document.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table Of Contents");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
// Add the list section to the sections collection of the Pdf document
tocPage.TocInfo = tocInfo;
// Define the format of the four levels list by setting the left margins and
// text format settings of each level

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = document.Pages.Add();
// Add four headings in the section
for (int Level = 1; Level != 5; Level++)
{ 
    Heading heading2 = new Heading(Level); 
    TextSegment segment2 = new TextSegment(); 
    heading2.TocPage = tocPage; 
    heading2.Segments.Add(segment2); 
    heading2.IsAutoSequence = true; 
    segment2.Text = "this is heading of level " + Level; 
    heading2.IsInList = true; 
    page.Paragraphs.Add(heading2); 
}

document.Save(outFile);
```

### Customize Page Numbers while adding TOC

It is common to customize the page numbering in the TOC while adding TOC in a PDF document. For example, we may need to add some prefix before page number like P1, P2, P3 and so on. In such a case, Aspose.PDF for .NET provides PageNumbersPrefix property of TocInfo class that can be used to customize page numbers as shown in the following code sample.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "CustomizePageNumbersAddingToC.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "CustomizePageNumbersAddingToC_out.pdf";
// Load an existing PDF files
Document document = new Document(inFile);
// Get access to first page of PDF file
Page tocPage = document.Pages.Insert(1);
// Create object to represent TOC information
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table Of Contents");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// Set the title for TOC
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i < document.Pages.Count; i++)
{
    // Create Heading object
    Heading heading2 = new Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // Specify the destination page for heading object
    heading2.DestinationPage = document.Pages[i + 1];
    // Destination page
    heading2.Top = document.Pages[i + 1].Rect.Height;
    // Destination coordinate
    segment2.Text = "Page " + i.ToString();
    // Add heading to page containing TOC
    tocPage.Paragraphs.Add(heading2);
}

// Save the updated document
document.Save(outFile);
```

## How to set PDF expiry date

We apply access privileges on PDF files so that a certain group of users can access particular features/objects of PDF documents. In order to restrict the PDF file access, we usually apply encryption and we may have a requirement to set PDF file expiration, so that the user accessing/viewing the document gets a valid prompt regarding PDF file expiry.

In order to accomplish the above stated requirement, we can use *JavascriptAction* object. Please take a look over the following code snippet.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instantiate Document object
Document document = new Document();
// Add page to pages collection of PDF file
document.Pages.Add();
// Add text fragment to paragraphs collection of page object
document.Pages[1].Paragraphs.Add(new TextFragment("Hello World..."));
// Create JavaScript object to set PDF expiry date
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('The file is expired. You need a new one.');");
// Set JavaScript as PDF open action
document.OpenAction = javaScript;

// Save PDF Document
document.Save(dataDir + "SetExpiryDate_out.pdf");
```

## Determine Progress of PDF File Generation

A customer asked us to add a feature that allows developers to determine the progress of PDF file generation. Here's the response to that request.

The field [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) of [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) class allows you to determine how PDF generation is going. The handler has the following types:

- DocSaveOptions.ConversionProgessEventHandler.
- DocSaveOptions.ProgressEventHandlerInfo.
- DocSaveOptions.ProgressEventType.

The code snippets below shows how to use CustomerProgressHandler.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Open document
Document document = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

document.Save(dataDir + "DetermineProgress_out.pdf", saveOptions);
```

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalised:
            Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }
}
```

## Flatten Fillable PDF

PDF documents often include forms with interactive fillable widgets such as radio buttons, checkboxes, text boxes, lists, etc. To make it uneditable for various application purposes, we need to flatten the PDF file.
Aspose.PDF provides the function to flatten your PDF in C# with just few line of code:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Load source PDF form
Document document = new Document(dataDir + "input.pdf");

// Flatten Flatten Fillable PDF 
if (document.Form.Fields.Count() > 0)
{
    foreach (var item in document.Form.Fields)
    {
        item.Flatten();
    }
}

// Save the updated document
document.Save(dataDir + "FlattenForms_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
