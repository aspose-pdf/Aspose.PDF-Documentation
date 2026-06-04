---
title: Add Attachments to PDF in Java
linktitle: Adding Attachment to a PDF document
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Learn how to add file attachments to PDF documents in Java using Aspose.PDF.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add embedded files to PDF documents with Java
Abstract: This article shows how to attach an external file to a PDF document using Aspose.PDF for Java. The example opens an existing PDF, creates a FileSpecification for the attachment, adds it to the document's EmbeddedFiles collection, and saves the updated file.
---
To attach a file to a PDF, load the source document, create a `FileSpecification`, add it to the embedded file collection, and save the result.

## Add an attachment to a PDF

The following example is based on `AttachmentsAddExamples.addAttachments`:

1. Open the source PDF document.
1. Create a FileSpecification for the file that will be attached.
1. Add or access the embedded file collection.
1. Save the updated PDF document.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(
                attachmentPath.toString(),
                "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
