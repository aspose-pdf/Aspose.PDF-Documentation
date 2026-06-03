---
title: Get PDF Metadata
type: docs
weight: 20
url: /java/get-pdf-metadata/
description: Learn how to read PDF metadata in Java with the PdfFileInfo facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Retrieving PDF Metadata Using Aspose.PDF for Java.
Abstract: Learn how to retrieve PDF metadata with Aspose.PDF for Java. The Java example reads standard fields such as subject, title, keywords, creator, creation date, and modification date, along with file status flags and a custom `Reviewer` metadata entry.
---
## Get PDF metadata

This example reads standard document information, file status flags, and a custom metadata key.

### Steps

1. Create a `PdfFileInfo` object for the source PDF.
2. Read the standard metadata fields such as subject, title, keywords, and creator.
3. Inspect file state flags such as whether the file is valid, encrypted, password protected, or a portfolio.
4. Read a custom metadata value with `getMetaInfo`.
5. Close the `PdfFileInfo` instance.

### Java example

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
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
