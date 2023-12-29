---
title: Extract text from PDF C#
linktitle: Extract text from PDF
type: docs
weight: 10
url: /net/extract-text-from-all-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF in C#. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text From All the Pages of a PDF Document

Extracting text from a PDF document is a common requirement. In this example, you’ll see how Aspose.PDF for .NET allows extracting text from all the pages of a PDF document. You need to create an object of the **TextAbsorber** class. After that, open the PDF using **Document** class and call the **Accept** method of the **Pages** collection. The **TextAbsorber** class absorbs the text from the document and returns in **Text** property. The following code snippet shows you how to extract text from all pages of PDF document.

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Create TextAbsorber object to extract text
TextAbsorber textAbsorber = new TextAbsorber();
// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textAbsorber);
// Get the extracted text
string extractedText = textAbsorber.Text;
// Create a writer and open the file
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Write a line of text to the file
tw.WriteLine(extractedText);
// Close the stream
tw.Close();
```

Call the **Accept** method on a particular page of the Document object. The Index is the particular page number from where text needs to be extracted.

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// Create TextAbsorber object to extract text
TextAbsorber textAbsorber = new TextAbsorber();
 
// Accept the absorber for a particular page
pdfDocument.Pages[1].Accept(textAbsorber);

// Get the extracted text
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// Create a writer and open the file
TextWriter tw = new StreamWriter(dataDir);

// Write a line of text to the file
tw.WriteLine(extractedText);

// Close the stream
tw.Close();
```

## Extract Text from Pages using Text Device

You can use the **TextDevice** class to extract text from a PDF file. TextDevice uses TextAbsorber in its implementation, thus, in fact, they do the same thing but TextDevice just implemented to unify the "Device" approach to extract anything from the page ImageDevice, PageDevice, etc. TextAbsorber may extract text from Page, entire PDF or XForm, this TextAbsorber is more universal

### Extract text from all pages

The following steps and code snippet shows you how to extract text from a PDF using the text device.

1. Create an object of Document class with input PDF file specified
1. Create an object of TextDevice class
1. Use object of TextExtractOptions class to specify extraction options
1. Use the Process method of TextDevice class to convert contents to the text
1. Save the text to the output file

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document( dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// String to hold extracted text
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // Create text device
        TextDevice textDevice = new TextDevice();

        // Set text extraction options - set text extraction mode (Raw or Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // Convert a particular page and save text to the stream
        textDevice.Process(pdfPage, textStream);
        // Convert a particular page and save text to the stream
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // Close memory stream
        textStream.Close();

        // Get text from memory stream
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// Save the extracted text in text file
File.WriteAllText(dataDir, builder.ToString());
```

## Extract Text from a particular page region

**TextAbsorber** class provides the capability to extract text from a particular or all pages of a PDF document. This class returns the extracted text in the **Text** property. However, if we have the requirement to extract text from a particular page region, we can use the **Rectangle** property of **TextSearchOptions.** The Rectangle property takes a Rectangle object as a value and using this property, we can specify the region of the page from which we need to extract the text.

The **Accept** method of a page is called to extract the text. Create objects of **Document** and **TextAbsorber** classes. Call **Accept** method on the individual page, as **Page** Index, of the **Document** object. The **Index** is the particular page number from where text needs to be extracted. You can get text from the **Text** property of the **TextAbsorber** class. The following code snippet shows you how to extract text from an individual page.

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Create TextAbsorber object to extract text
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// Accept the absorber for first page
pdfDocument.Pages[1].Accept(absorber);

// Get the extracted text
string extractedText = absorber.Text;
// Create a writer and open the file
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Write a line of text to the file
tw.WriteLine(extractedText);
// Close the stream
tw.Close();
```

## Extract text based on columns

A PDF file may comprise of Text, Image, Annotations, Attachments, Graphs, etc elements and Aspose.PDF for .NET offers the feature to Add as well as manipulate all of these elements. This API is remarkable when comes to Text addition and extraction from PDF document and we may come across a scenario where a PDF document is comprised of more than one columns (multi-column) PDF document and we need to extract the page contents while honoring the same layout, then Aspose.PDF for .NET is the right choice to accomplish this requirement. One approach is to reduce the font size of contents inside the PDF document and then perform text extraction. The following code snippet shows the steps to reduce text size and then try extracting text from PDF document.

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // Need to reduce font size at least for 70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```

### Second approach - Using ScaleFactor

In this new release, we also have introduced several improvements in TextAbsorber and in the internal text formatting mechanism. So now during the text extraction using ‘Pure’ mode, you may specify the ScaleFactor option and it can be another approach to extract text from a multi-column PDF document besides the above-stated approach. This scale factor may be set to adjust the grid which is used for the internal text formatting mechanism during text extraction. Specifying the ScaleFactor values between 1 and 0.1 (including 0.1) has the same effect as font reduction.

Specifying the ScaleFactor values between 0.1 and -0.1 is treated as zero value, but it makes the algorithm to calculate scale factor needed during extracting text automatically. The calculation is based on average glyph width of the most popular font on the page, but we cannot guarantee that in extracted text no string of column reaches the start of the next column. Please note that if ScaleFactor value is not specified, the default value of 1.0 will be used. It means no scaling will be carried out. If the specified ScaleFactor value is more than 10 or less than -0.1, the default value of 1.0 will be used.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width ( about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// Setting scale factor to 0.5 is enough to split columns in the majority of documents
// Setting of zero allows to algorithm choose scale factor automatically
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```

{{% alert color="primary" %}}

Please note that there is no direct correspondence between the new ScaleFactor and the old coefficient of manually font reducing. However, by default algorithm takes into account the value of font size that has already reduced due to some internal reasons. For example, reducing font size from 10 to 7 has the same effect as setting a scale factor to 5/8 (= 0.625).

{{% /alert %}}

## Extract Highlighted Text from PDF Document

In various scenarios of text extraction from a PDF document, you can come up with a requirement to extract only highlighted text from PDF document. In order to implement the functionality, we have added TextMarkupAnnotation.GetMarkedText() and TextMarkupAnnotation.GetMarkedTextFragments() methods in API. You can extract highlighted text from PDF document by filtering TextMarkupAnnotation and using the mentioned methods. The following code snippet shows how you can extract highlighted text from PDF document. 

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// Loop through all the annotations
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // Filter TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // Retrieve highlighted text fragments
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // Display highlighted text
            Console.WriteLine(tf.Text);
        }
    }
}
```

## Access Text Fragment and Segment Elements from XML

Sometimes we need access to TextFragement or TextSegment items when processing PDF documents generated from XML. Aspose.PDF for .NET provides access to such items by name. The code snippet below shows how to use this functionality.

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
