---
title: Java를 사용하여 주석 가져오기 및 내보내기
linktitle: 주석 가져오기 및 내보내기
type: docs
weight: 80
url: /java/import-export-annotations/
description: Java용 Aspose.PDF를 사용하여 한 PDF 문서의 주석을 다른 PDF 문서로 복사하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java 문서 간에 PDF 주석을 전송합니다.
Abstract: 이 문서에서는 소스 PDF에서 주석을 복사하고 Aspose.PDF for Java를 사용하여 새 PDF 문서로 내보내는 방법을 설명합니다. 워크플로는 소스 파일을 로드하고, 대상 문서를 만들고, 페이지를 추가하고, 첫 번째 소스 페이지에서 주석을 복사하고, 결과를 저장합니다.
---
## 
한 PDF에서 다른 PDF로 주석 복사


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가합니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 각 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/)을 추가합니다.

1. 
대상 페이지의 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 항목을 읽거나 반복합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

1. 
첫 번째 원본 페이지에 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 항목을 열거하고 각각 대상 페이지에 추가합니다.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
