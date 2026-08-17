---
title: N-Up PDF 문서 만들기
linktitle: N-Up PDF 문서 만들기
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: PdfFileEditor 외관을 사용하여 Java에서 2x2 N-Up PDF 레이아웃을 만듭니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java의 기존 문서에서 N-Up PDF 레이아웃 생성
Abstract: Java용 Aspose.PDF를 사용하여 N-Up PDF 문서를 만드는 방법을 알아보세요. Java 예제에서는 PdfFileEditor를 사용하여 각 출력 시트에 4개의 소스 페이지를 배치하고 오류 검사를 위한 부울 반환 변형도 보여줍니다.
---
## 
N-Up PDF 문서 만들기



Java 샘플은 `PdfFileEditor.makeNUp`을 사용하여 기존 PDF에서 2x2 레이아웃을 작성합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
입력 파일, 출력 파일, 열과 행 수를 사용하여 `makeNUp`을 호출합니다.

3. 
생성된 문서를 저장합니다.

4. 
명시적인 성공 확인을 원하는 경우 부울 반환 변형을 호출하고 `false` 결과를 처리합니다.


### 
자바 예

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
