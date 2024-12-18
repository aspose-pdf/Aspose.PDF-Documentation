---
title: PDF 문서 열기
linktitle: 열기
type: docs
weight: 20
url: /ko/java/open-pdf-document/
description: Aspose.PDF for Java를 사용하여 PDF 파일을 여는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF 문서 열기

문서를 여는 방법은 여러 가지가 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

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


## 스트림에서 기존 PDF 문서 열기

```java
    public static void OpenDocumentStream() {
        String remoteURL = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
        String fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
        try (BufferedInputStream in = new BufferedInputStream(new java.net.URL(remoteURL + fileName).openStream())) {
            InputStream inputStream = in;
            Document pdfDocument = new Document(inputStream);
            System.out.println("페이지 수: " + pdfDocument.getPages().size());

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
```

## 암호화된 PDF 문서 열기

```java
   public static void OpenDocumentWithPassword() {
        String fileName = "C:\\tmp\\DocSite.pdf";
        String password = "Aspose2020";
        try {
            Document pdfDocument = new Document(fileName, password);
            System.out.println("페이지 수: " + pdfDocument.getPages().size());
        } catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }

}
```