---
title: 여러 PDF 파일 연결
linktitle: 여러 PDF 파일 연결
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: 배열 기반 PdfFileEditor 연결 워크플로를 사용하여 Java에서 PDF 파일을 병합합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 여러 PDF 파일을 하나의 문서로 병합
Abstract: PDF 파일을 Java용 Aspose.PDF와 연결하는 방법을 알아보세요. 리포지토리 샘플은 두 개의 입력이 있는 배열 기반 `concatenate` 오버로드를 사용하며, 이 메서드는 소스 경로의 문자열 배열을 허용하므로 동일한 워크플로를 더 긴 파일 목록으로 확장할 수 있습니다.
---
## PDF 파일 연결



Java 샘플은 두 파일을 배열 기반 `concatenate` 오버로드에 전달하여 병합합니다.


### 
단계


1. 
`PdfFileEditor` 인스턴스를 생성합니다.

2. 
입력 PDF 경로로 문자열 배열을 만듭니다.
3. 입력 배열 및 출력 파일 경로를 사용하여 `concatenate`을 호출합니다.

4. 
병합된 문서를 저장합니다.


```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```


두 개 이상의 파일을 병합하려면 `concatenate`에 전달된 문자열 배열을 확장하세요.
