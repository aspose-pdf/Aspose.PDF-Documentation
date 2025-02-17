---
title: Open PDF Document
linktitle: Open
type: docs
weight: 20
url: /java/open-pdf-document/
description: Learn how to open a PDF file with Aspose.PDF for Java.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to open a PDF file with Aspose.PDF for Java.
Abstract: The article provides a guide on how to open existing PDF documents using the Aspose.PDF library in Java. It details three methods for opening PDFs - by specifying a file name, from a stream, and by accessing encrypted documents with a password. The first method demonstrates opening a PDF by specifying its file path and printing the number of pages. The second method involves opening a PDF from a remote URL stream, utilizing a `BufferedInputStream` to handle the input stream and output the page count. The third method explains how to access an encrypted PDF by supplying the required password and retrieving its page count. Each code example includes error handling to manage exceptions that may occur during the document opening process.
SoftwareApplication: java 
---

## Open existing PDF document

There are several ways to open a document. The easiest is to specify a file name.

```java
package com.aspose.pdf.examples;

import java.io.InputStream;
import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;
import com.aspose.pdf.internal.pcl.util.BufferedInputStream;

public final class BasicOperationsOpen {

    private BasicOperationsOpen() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        OpenDocument();
        OpenDocumentStream();
        OpenDocumentWithPassword();
    }

    public static void OpenDocument() {
        String fileName = _dataDir+"/tourguidev2_gb_tags.pdf";
        Document pdfDocument = new Document(fileName);
        System.out.println("Pages +" + pdfDocument.getPages().size());
    }

```

## Open existing PDF document from stream

```java
    public static void OpenDocumentStream() {
        String remoteURL = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
        String fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
        try (BufferedInputStream in = new BufferedInputStream(new java.net.URL(remoteURL + fileName).openStream())) {
            InputStream inputStream = in;
            Document pdfDocument = new Document(inputStream);
            System.out.println("Pages +" + pdfDocument.getPages().size());

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
```

## Open encrypted PDF document

```java
   public static void OpenDocumentWithPassword() {
        String fileName = "C:\\tmp\\DocSite.pdf";
        String password = "Aspose2020";
        try {
            Document pdfDocument = new Document(fileName, password);
            System.out.println("Pages +" + pdfDocument.getPages().size());
        } catch (Exception  e)
        {
            System.out.println(e.getMessage());
        }
    }

}
```
