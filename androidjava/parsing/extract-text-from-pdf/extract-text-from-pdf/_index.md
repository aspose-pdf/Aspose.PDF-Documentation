---
title: Extracting raw text from PDF file 
linktitle: Extract text from PDF
type: docs
weight: 10
url: /androidjava/extract-text-from-all-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF for Android via Java. From entire pages, from a specific part, based on columns, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text From All the Pages of a PDF Document

Extracting text from a PDF document is a common requirement. In this example, you'll see how Aspose.PDF for Java allows extracting text from all the pages of a PDF document.
To extract text from all the PDF pages:

1. Create an object of the [TextAbsorber](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class.
1. Open the PDF using [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) class and call the [Accept](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) method of the [Pages](https://apireference.aspose.com/pdf/java/com.aspose.pdf/classes/PageCollection) collection.
1. The [TextAbsorber](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class absorbs the text from the document and returns in **Text** property.

The following code snippet shows you how to extract text from all pages of PDF document.

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

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

## Extract Highlighted Text from PDF Document

In various scenarios of text extraction from a PDF document, you can come up with a requirement to extract only highlighted text from PDF document. In order to implement the functionality, we have added TextMarkupAnnotation.GetMarkedText() and TextMarkupAnnotation.GetMarkedTextFragments() methods in API. You can extract highlighted text from PDF document by filtering TextMarkupAnnotation and using the mentioned methods. The following code snippet shows how you can extract highlighted text from PDF document.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## Access Text Fragment and Segment Elements from XML

Sometimes we need access to TextFragement or TextSegment items when processing PDF documents generated from XML. Aspose.PDF for Android via Java provides access to such items by name. The code snippet below shows how to use this functionality.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```
