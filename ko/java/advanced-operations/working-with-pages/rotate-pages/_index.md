---
title: Java에서 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 110
url: /java/rotate-pages/
description: PDF 페이지를 회전하고 Java에서 페이지 방향을 변경하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java로 PDF 페이지 회전
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 페이지를 회전하는 방법을 설명합니다. 이 예에서는 문서의 모든 페이지를 반복하고 90도 회전을 적용한 다음 업데이트된 PDF를 저장합니다.
---
하나 이상의 페이지에서 방향을 변경해야 하는 경우 페이지 회전 API를 사용하세요.


## 
모든 페이지를 90도 회전



문서의 모든 페이지를 시계 방향으로 회전해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
모든 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 개체를 반복하고 회전 값을 설정합니다.
1. 업데이트된 PDF를 저장합니다.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
