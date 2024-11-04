---
title: 프로그램적으로 PDF 페이지 삭제하기
linktitle: PDF 페이지 삭제
type: docs
weight: 40
url: /java/delete-pages/
description: Java 라이브러리를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Java를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection)에서 특정 페이지를 삭제하려면 delete() 메서드를 호출하고 삭제하려는 특정 페이지의 인덱스를 지정합니다. 그런 다음 save 메서드를 호출하여 업데이트된 PDF 파일을 저장합니다.

## PDF 파일에서 페이지 삭제

1. Delete 메서드를 호출하고 페이지의 인덱스를 지정합니다.
1. Save 메서드를 호출하여 업데이트된 PDF 파일을 저장합니다.
다음 코드 스니펫은 Java를 사용하여 PDF 파일에서 특정 페이지를 삭제하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 특정 페이지 삭제
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // 업데이트된 PDF 저장
    pdfDocument.save(_dataDir);    

  }
```