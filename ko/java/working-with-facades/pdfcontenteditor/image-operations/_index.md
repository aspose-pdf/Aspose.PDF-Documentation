---
title: 이미지 작업
linktitle: 이미지 작업
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: Aspose.PDF의 PdfContentEditor 파사드에서 사용할 수 있는 현재 Java 이미지 작업 적용 범위를 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: PdfContentEditor를 사용한 Java의 이미지 편집 작업 흐름
Abstract: 이 섹션에서는 현재 Java PdfContentEditor 예제 세트에서 지원되는 이미지 관련 작업 흐름을 다룹니다. 저장소에는 이미지 교체에 대한 직접적인 예가 포함되어 있으며, 지원되지 않는 이미지 삭제 주제는 명시적인 범위 참고 사항으로 유지됩니다.
---

현재 Java `PdfContentEditorExamples` 클래스는 `replaceImage(...)`을 직접 지원합니다.


## 
이미지 교체


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
페이지 번호, 이미지 인덱스, 교체 이미지 경로를 `replaceImage(...)`으로 전화하세요.

3. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
