---
title: Work with PDF File Metadata in Java
linktitle: PDF File Metadata
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: Learn how to extract, update, and manage PDF file metadata, document information, and XMP properties in Java using Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Get and set PDF document information and XMP metadata in Java
Abstract: This article explains how to work with PDF metadata using Aspose.PDF for Java. Learn how to read document information such as author, title, and keywords, update file properties, inspect PDF version and privileges, set XMP metadata fields, and save metadata through both the DOM and facade APIs.
---
Aspose.PDF for Java provides two main ways to work with metadata:

- The DOM API through `Document`, `DocumentInfo`, and `document.getMetadata()`.
- The facade API through `PdfFileInfo`.

## Read document information with the DOM API

Use `DocumentInfo` when you need standard document properties such as author, title, subject, and dates:

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## Update document information

The `setFileInformation` example updates standard info fields and saves the modified PDF:

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
}
```

## Set XMP metadata and custom namespace prefixes

The metadata collection also supports namespaced XMP entries:

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
}
```

The related `setXmpMetadata` example adds fields such as `xmp:CreateDate`, `xmp:Nickname`, and a custom XMP property.

## Inspect PDF version, privileges, page metrics, and metadata with PdfFileInfo

`PdfFileInfo` provides facade-style access to metadata and file characteristics. The example set includes methods to:

- Read the PDF version with `getPdfVersion`.
- Inspect document permissions with `getDocumentPrivileges`.
- Get page width, height, rotation, and offsets.
- Read metadata and encryption state with `getPdfMetadata`.

For example, `getPdfMetadata` reads standard fields and checks whether the file is encrypted or a portfolio:

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    pdfInfo.close();
}
```

## Set, clear, and save metadata with XMP through the facade API

The `PdfFileInfoExamples` class also demonstrates:

- `setPdfMetadata` to update subject, title, keywords, creator, and a custom metadata key.
- `clearPdfMetadata` to remove stored info with `clearInfo()`.
- `saveInfoWithXmp` to save updated metadata as XMP with `saveNewInfoWithXmp(...)`.
