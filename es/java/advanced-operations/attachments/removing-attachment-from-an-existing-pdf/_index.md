---
title: Remove Attachments from PDF in Java
linktitle: Removing attachment from an existing PDF
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Learn how to remove one or all embedded attachments from PDF documents in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete PDF attachments programmatically with Java
Abstract: This article shows how to remove attachments from PDF files using Aspose.PDF for Java. The examples demonstrate deleting one embedded file by key and clearing the entire EmbeddedFiles collection before saving the updated document.
---
Attachments stored in a PDF document can be removed either individually or all at once through the `EmbeddedFiles` collection.

## Remove a single attachment

Use this example when one named embedded file should be deleted from the PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Delete the attachment by its key from the embedded files collection.
1. Save the updated output document.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## Remove all attachments

Use this approach when the entire embedded file collection should be cleared.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Delete all items from the embedded files collection.
1. Save the cleaned output document.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
