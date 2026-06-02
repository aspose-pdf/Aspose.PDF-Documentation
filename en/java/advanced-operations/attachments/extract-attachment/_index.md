---
title: Extract Attachments from PDF
linktitle: Extract Attachments
type: docs
weight: 50
url: /java/extract-attachment/
description: Learn how to extract embedded files and file attachment annotations from PDF documents in Java using Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract one or all embedded files from a PDF with Java
Abstract: This article explains how to extract attachments from PDF documents with Aspose.PDF for Java. It covers extracting a single named attachment, saving every embedded file to an output folder, reading file metadata, and exporting content from a FileAttachment annotation on a page.
---
Aspose.PDF for Java supports several extraction flows depending on how attachments are stored in the document.

## Extract a single attachment by name

Use this approach when you know the embedded file name in advance:

1. Open the source PDF document used in this example.
2. Run the Aspose.PDF operations required to extract a single attachment by name.
3. Write the extracted output or inspect the returned values.

```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## Extract all embedded files

This example loops through the embedded file collection, resolves a usable file name, and writes each attachment to disk:

1. Open the source PDF document used in this example.
2. Run the Aspose.PDF operations required to extract all embedded files.
3. Write the extracted output or inspect the returned values.

```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

The full example also reads metadata such as description, MIME type, checksum, creation date, modification date, and size from `FileParams`.

## Extract a file attachment annotation

If the attachment is stored as a `FileAttachmentAnnotation`, inspect page annotations and export the associated file:

1. Open the source PDF document used in this example.
2. Run the Aspose.PDF operations required to extract a file attachment annotation.
3. Write the extracted output or inspect the returned values.

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }
    }
}
```
