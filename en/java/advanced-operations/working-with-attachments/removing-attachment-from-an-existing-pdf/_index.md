---
title: Removing attachment from an existing PDF 
linktitle: Removing attachment from an existing PDF
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF can remove attachments from your PDF documents. Use Java PDF API to remove attachments in PDF files with Aspose.PDF library.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Removing attachment from an existing PDF using Aspose.PDF for Java
Abstract: Aspose.PDF provides functionality to remove attachments from PDF files. Attachments within a PDF are stored in the Document object's EmbeddedFiles collection. To delete all attachments, one can invoke the delete method on the EmbeddedFiles collection and subsequently save the updated document using the Document object's save method. The provided Java code snippet demonstrates this process - it opens a PDF document, deletes all its attachments, and saves the modified document.
SoftwareApplication: java
---

Aspose.PDF can remove attachments from PDF files. A PDF document's attachments are held in the Document object's EmbeddedFiles collection.

A PDF document's attachments are held in the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) collection.

To delete all attachments associated with a PDF file:

1. Call the [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) collection's delete(..) method.
1. Save the updated file using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's save method.

The following code snippet shows how to delete all the attachments from a PDF document.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // Open a document
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Delete all attachments
  pdfDocument.getEmbeddedFiles().delete();
  // Save the updated file
  pdfDocument.save("output.pdf");

    }
```
