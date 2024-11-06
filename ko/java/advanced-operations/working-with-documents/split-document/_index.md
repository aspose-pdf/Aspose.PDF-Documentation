---
title: Split PDF programmatically
linktitle: Split PDF files
type: docs
weight: 60
url: ko/java/split-document/
description: 이 주제는 Java 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 PDF 파일을 분할하고 온라인에서 결과를 확인할 수 있습니다. 이 링크를 방문하세요: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

이 주제는 Java 애플리케이션에서 Aspose.PDF for Java를 사용하여 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. Java를 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 컬렉션을 통해 PDF 문서의 페이지를 순회합니다.

1. 각 반복마다 새로운 Document 객체를 생성하고 개별 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체를 빈 문서에 추가합니다.
1. Save 메소드를 사용하여 새 PDF를 저장합니다.

다음 Java 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // 문서 디렉토리의 경로.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // 모든 페이지를 순회
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```