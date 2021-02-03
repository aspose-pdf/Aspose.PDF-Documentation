---
title: Open PDF document programmatically
linktitle: Open
type: docs
weight: 20
url: /java/open-pdf-document/
description: Learn how to open a PDF file with Aspose.PDF for Java.
aliases:
    - /java/opening-a-pdf-document/
lastmod: "2021-02-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
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
