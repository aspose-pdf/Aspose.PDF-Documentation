---
title: 두 개의 PDF 파일 연결
linktitle: 두 개의 PDF 파일 연결
type: docs
weight: 60
url: /java/concatenate-two-files/
description: PdfFileEditor 외관을 사용하여 두 개의 PDF 파일을 Java의 하나의 문서로 병합합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 두 개의 PDF 파일을 단일 출력 문서로 연결합니다.
Abstract: Java용 Aspose.PDF를 사용하여 두 PDF 파일을 연결하는 방법을 알아보세요. Java 예제에서는 PdfFileEditor와 배열 기반 `concatenate` 오버로드를 사용하여 두 개의 소스 문서를 하나의 출력 PDF로 결합합니다.
---
## 
두 개의 PDF 파일을 연결합니다



이 문서는 `PdfFileEditorExamples.java`의 `mergePdfDocuments` 예제에 직접 매핑됩니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
두 개의 입력 파일 경로를 문자열 배열로 전달합니다.

3. 
배열 및 출력 파일 경로를 사용하여 `concatenate`을 호출하세요.

4. 
병합된 PDF를 저장합니다.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
