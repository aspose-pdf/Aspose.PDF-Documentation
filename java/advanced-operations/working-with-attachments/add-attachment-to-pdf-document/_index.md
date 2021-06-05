---
title: Adding Attachment to PDF document 
linktitle: Adding Attachment to PDF document 
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: This page describes how to add an attachment to a PDF file with Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Attachments can contain a wide variety of information and can be of a variety of file types. This article explains how to add an attachment to a PDF file.

1. Create a [FileSpecification](https://apireference.aspose.com/java/pdf/com.aspose.pdf/FileSpecification) object that contains the file you want to attach, and file description.
1. Add the [FileSpecification](https://apireference.aspose.com/java/pdf/com.aspose.pdf/FileSpecification) object to a [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/Document) object’s [EmbeddedFiles](https://apireference.aspose.com/java/pdf/com.aspose.pdf/EmbeddedFileCollection) collection using the [add(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf/FileSpecification) method. The [EmbeddedFiles](https://apireference.aspose.com/java/pdf/com.aspose.pdf/EmbeddedFileCollection) collection contains all the attachments added to a PDF file.

The following code snippet shows you how to add an attachment in a PDF document.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // Open a document
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Set up a new file to be added as attachment
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "Sample text file");
  // Add an attachment to document's attachment collection
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // Save the updated document
  pdfDocument.save("output.pdf");
    }
}
```
