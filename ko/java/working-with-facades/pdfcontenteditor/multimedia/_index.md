---
title: 멀티미디어
linktitle: 멀티미디어
type: docs
weight: 70
url: /java/pdfcontenteditor-multimedia/
description: Aspose.PDF의 Java PdfContentEditor 파사드에서 사용할 수 있는 현재 멀티미디어 범위를 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: PdfContentEditor를 사용한 Java의 멀티미디어 주석 작업 흐름
Abstract: 이 섹션에서는 현재 Java PdfContentEditor 예제 세트에서 지원되는 멀티미디어 관련 작업 흐름을 다룹니다. 저장소에는 직접적인 영화 주석 예제가 포함되어 있지만 지원되지 않는 사운드 주제는 명시적인 범위 메모로 유지됩니다.
---

현재 Java `PdfContentEditorExamples` 클래스는 `addMovieAnnotation(...)`을 직접 지원합니다.


## 
영화 주석 추가


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
주석 사각형, 동영상 파일 경로 및 페이지 번호를 사용하여 `createMovie(...)`으로 전화하세요.

3. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
