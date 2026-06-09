---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: Learn how to open a PDF file in Java using Aspose.PDF from a file path, a stream, or with a password.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Opening PDF documents using the Aspose.PDF library in Java
Abstract: This article shows how to open existing PDF documents in Java using Aspose.PDF. It covers opening a PDF by file path, opening a PDF from an InputStream, and opening a password-protected document, with each example reading the page count from the loaded document.
---

Aspose.PDF for Java supports several ways to load an existing PDF document depending on where the source data comes from.

## Open a PDF document in Java

You can open a PDF document:

1. Open a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) directly from a file path.
1. Open a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) from an `InputStream`.
1. Open an encrypted [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) by supplying the password.

## Open document from file

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## Open document from stream

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## Open an encrypted document

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
