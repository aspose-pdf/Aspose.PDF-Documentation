---
title: 프로그래밍 방식으로 PDF 문서 만들기
linktitle: PDF 작성
type: docs
weight: 10
url: /java/create-document/
description: Aspose.PDF를 사용하여 Java에서 처음부터 PDF 문서를 만드는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 PDF 파일 생성
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 PDF 파일을 만드는 방법을 보여줍니다. 이 예제에서는 새 Document 개체를 만들고, 페이지를 추가하고, 샘플 텍스트가 포함된 TextFragment를 삽입하고, 결과를 PDF 파일로 저장합니다.
---
코드로 PDF 파일을 생성하는 것은 보고서, 송장 및 생성된 비즈니스 문서에 대한 일반적인 요구 사항입니다. Java용 Aspose.PDF는 처음부터 문서를 작성하는 직접적인 방법을 제공합니다.


## 
Java에서 PDF 파일을 만드는 방법



프로그래밍 방식으로 PDF 문서를 생성하려면:


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.
1. 페이지 단락에 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 추가합니다.

1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 출력 파일로 저장합니다.


## 
간단한 PDF 문서 만들기



다음 Java 예제는 `CreatePdfDocumentExamples.java`을 기반으로 합니다.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
