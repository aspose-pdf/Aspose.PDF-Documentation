---
title: Adding Attachment to PDF document 
linktitle: Adding Attachment to PDF document 
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: This page describes how to add an attachment to a PDF file with Java.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add attachments to a PDF file using Java
Abstract: The article provides a step-by-step guide on how to add attachments to a PDF file using Java. It begins by creating a `FileSpecification` object, which contains the file intended for attachment along with a description. This object is then added to a PDF document's `EmbeddedFiles` collection, which holds all attachments in the document. The article includes a code snippet demonstrating this process - it opens an existing PDF document, sets up a new file to be attached, adds it to the document's attachments, and saves the updated PDF. The example uses Aspose.PDF for Java to manage the attachment process.
SoftwareApplication: java
---

Attachments can contain a wide variety of information and can be of a variety of file types. This article explains how to add an attachment to a PDF file.

1. Create a [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) object that contains the file you want to attach, and file description.
1. Add the [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) object to a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) collection using the [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) method. The [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) collection contains all the attachments added to a PDF file.

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
