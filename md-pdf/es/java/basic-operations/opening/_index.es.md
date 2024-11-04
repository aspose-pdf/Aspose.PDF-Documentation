---
title: Abrir Documento PDF
linktitle: Abrir
type: docs
weight: 20
url: /java/open-pdf-document/
description: Aprende cómo abrir un archivo PDF con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir documento PDF existente

Hay varias maneras de abrir un documento. La más fácil es especificar un nombre de archivo.

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
        System.out.println("Páginas +" + pdfDocument.getPages().size());
    }

```


## Abrir documento PDF existente desde un flujo

```java
    public static void OpenDocumentStream() {
        String remoteURL = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
        String fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
        try (BufferedInputStream in = new BufferedInputStream(new java.net.URL(remoteURL + fileName).openStream())) {
            InputStream inputStream = in;
            Document pdfDocument = new Document(inputStream);
            System.out.println("Páginas +" + pdfDocument.getPages().size());

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
```

## Abrir documento PDF cifrado

```java
   public static void OpenDocumentWithPassword() {
        String fileName = "C:\\tmp\\DocSite.pdf";
        String password = "Aspose2020";
        try {
            Document pdfDocument = new Document(fileName, password);
            System.out.println("Páginas +" + pdfDocument.getPages().size());
        } catch (Exception  e)
        {
            System.out.println(e.getMessage());
        }
    }

}
```