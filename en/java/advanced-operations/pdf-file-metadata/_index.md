---
title: Work with PDF File Metadata in Java
linktitle: PDF File Metadata
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: Learn how to extract, update, and manage PDF file metadata, document information, and XMP properties in Java using Aspose.PDF.
lastmod: "2026-06-09"
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

## Get PDF file information

Use this example when you need to read standard document information fields such as author, title, subject, or keywords.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Access the [DocumentInfo](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/documentinfo/) object.
1. Read the required metadata fields and output their values.

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

## Set metadata with a namespace prefix

Use this example when you need to add or update an XMP property by using a registered namespace prefix.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Register the required XMP namespace and add the metadata item.
1. Save the updated document.

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## Update document information fields

Use this example when you want to write standard PDF file properties such as author, title, producer, or creation date.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Access [DocumentInfo](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/documentinfo/) and assign new metadata values.
1. Save the document with the updated file information.

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
    System.out.println("File information saved to " + outputFile);
}
```

## Set XMP metadata properties

Use this example when you need to store additional XMP entries, including custom metadata values.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add the required XMP metadata items through `document.getMetadata()`.
1. Save the output file.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
