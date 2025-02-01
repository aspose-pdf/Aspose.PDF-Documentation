---
title: Extracting raw text from PDF file 
linktitle: Extract text from PDF
type: docs
weight: 10
url: /java/extract-text-from-all-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF for Java. From entire pages, from a specific part, based on columns, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: This article explores various methods for extracting text from PDF documents using Aspose.PDF for Java. It provides detailed instructions and code examples for different scenarios, including extracting text from all pages, specific regions, and highlighted sections. The article discusses the use of classes such as `TextAbsorber` and `TextDevice`, and explains how to set extraction options and handle output. Additionally, it covers advanced features like adjusting text extraction based on columns using the `ScaleFactor` and accessing text fragments and segments from XML. These techniques are essential for developers needing to manipulate and extract data from PDF files programmatically.
---

## Extract Text From All the Pages of a PDF Document

Extracting text from a PDF document is a common requirement. In this example, you'll see how Aspose.PDF for Java allows extracting text from all the pages of a PDF document.
To extract text from all the PDF pages:

1. Create an object of the [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class.
1. Open the PDF using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class and call the [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) method of the [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) collection.
1. The [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class absorbs the text from the document and returns in **Text** property.

The following code snippet shows you how to extract text from all pages of PDF document.

```java
public static void ExtractFromAllPages(){
    // The path to the documents directory.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // Open document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Create TextAbsorber object to extract text
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // Accept the absorber for all the pages
    pdfDocument.getPages().accept(textAbsorber);
    
    // Get the extracted text
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // Write a line of text to the file
        writer.write(extractedText);            
        // Close the stream
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```

## Extract Text from Pages using Text Device

You can use the **TextDevice** class to extract text from a PDF file. TextDevice uses [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) in its implementation, thus, in fact, they do the same thing but TextDevice just implemented to unify the "Device" approach to extract anything from the page ImageDevice, PageDevice, etc. TextAbsorber may extract text from Page, entire PDF or XForm, this TextAbsorber is more universal

### Extract text from all pages

The following steps and code snippet shows you how to extract text from a PDF using the text device.

1. Create an object of Document class with input PDF file specified
1. Create an object of TextDevice class
1. Use object of TextExtractOptions class to specify extraction options
1. Use the Process method of TextDevice class to convert contents to the text
1. Save the text to the output file

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // open document
    Document pdfDocument = new Document("input.pdf");
    // text file in which extracted text will be saved
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // iterate through all the pages of PDF file
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // create text device
        TextDevice textDevice = new TextDevice();
        // set text extraction options - set text extraction mode (Raw or
        // Pure)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // get the text from pages of PDF and save it to OutputStream object
        textDevice.process(page, text_stream);
    }
    // close stream object
    text_stream.close();
}
```

## Extract Text from a particular page region

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class provides the capability to extract text from a particular or all pages of a PDF document. This class returns the extracted text in the **Text** property. However, if we have the requirement to extract text from a particular page region, we can use the **Rectangle** property of [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). The Rectangle property takes a Rectangle object as a value and using this property, we can specify the region of the page from which we need to extract the text.

The [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) method of a page is called to extract the text. Create objects of [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) and [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) classes. Call [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) method on the individual page, as **Page** Index, of the **Document** object. The **Index** is the particular page number from where text needs to be extracted. You can get text from the **Text** property of the [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class. The following code snippet shows you how to extract text from an individual page.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // open document
    Document doc = new Document("page_0001.pdf");
    // create TextAbsorber object to extract text
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // accept the absorber for first page
    doc.getPages().get_Item(1).accept(absorber);
    // get the extracted text
    String extractedText = absorber.getText();
    // create a writer and open the file
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // write extracted contents
    writer.write(extractedText);
    // Close writer
    writer.close();
}
```

## Extract text based on columns

A PDF file may comprise of Text, Image, Annotations, Attachments, Graphs, etc elements and Aspose.PDF for .NET offers the feature to Add as well as manipulate all of these elements. This API is remarkable when comes to Text addition and extraction from PDF document and we may come across a scenario where a PDF document is comprised of more than one columns (multi-column) PDF document and we need to extract the page contents while honoring the same layout, then Aspose.PDF for .NET is the right choice to accomplish this requirement. One approach is to reduce the font size of contents inside the PDF document and then perform text extraction. The following code snippet shows the steps to reduce text size and then try extracting text from PDF document.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // open document
    Document doc = new Document("page_0001.pdf");
    // create TextAbsorber object to extract text
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // accept the absorber for first page
    doc.getPages().get_Item(1).accept(absorber);
    // get the extracted text
    String extractedText = absorber.getText();
    // create a writer and open the file
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // write extracted contents
    writer.write(extractedText);
    // Close writer
    writer.close();
}
```

### Second approach - Using ScaleFactor

In this new release, we also have introduced several improvements in TextAbsorber and in the internal text formatting mechanism. So now during the text extraction using ‘Pure’ mode, you may specify the ScaleFactor option and it can be another approach to extract text from a multi-column PDF document besides the above-stated approach. This scale factor may be set to adjust the grid which is used for the internal text formatting mechanism during text extraction. Specifying the ScaleFactor values between 1 and 0.1 (including 0.1) has the same effect as font reduction.

Specifying the ScaleFactor values between 0.1 and -0.1 is treated as zero value, but it makes the algorithm to calculate scale factor needed during extracting text automatically. The calculation is based on average glyph width of the most popular font on the page, but we cannot guarantee that in extracted text no string of column reaches the start of the next column. Please note that if ScaleFactor value is not specified, the default value of 1.0 will be used. It means no scaling will be carried out. If the specified ScaleFactor value is more than 10 or less than -0.1, the default value of 1.0 will be used.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width ( about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Setting of zero allows to algorithm choose scale factor automatically
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```

{{% alert color="primary" %}}

Please note that there is no direct correspondence between the new ScaleFactor and the old coefficient of manually font reducing. However, by default algorithm takes into account the value of font size that has already reduced due to some internal reasons. For example, reducing font size from 10 to 7 has the same effect as setting a scale factor to 5/8 (= 0.625).

{{% /alert %}}

## Extract Highlighted Text from PDF Document

In various scenarios of text extraction from a PDF document, you can come up with a requirement to extract only highlighted text from PDF document. In order to implement the functionality, we have added TextMarkupAnnotation.GetMarkedText() and TextMarkupAnnotation.GetMarkedTextFragments() methods in API. You can extract highlighted text from PDF document by filtering TextMarkupAnnotation and using the mentioned methods. The following code snippet shows how you can extract highlighted text from PDF document.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // Loop through all the annotations
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // Filter TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // Retrieve highlighted text fragments
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // Display highlighted text
                System.out.println(tf.getText());
            }
        }
    }        
}
```

## Access Text Fragment and Segment Elements from XML

Sometimes we need access to TextFragement or TextSegment items when processing PDF documents generated from XML. Aspose.PDF for .NET provides access to such items by name. The code snippet below shows how to use this functionality.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```
