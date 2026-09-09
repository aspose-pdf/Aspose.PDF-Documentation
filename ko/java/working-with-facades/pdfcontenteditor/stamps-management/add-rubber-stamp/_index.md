---
title: 고무 스탬프 추가
linktitle: 고무 스탬프 추가
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 PDF 문서에 도장 주석을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF에 도장 추가
Abstract: 이 문서에서는 PDF를 바인딩하고, 레이블 텍스트와 색상으로 도장 주석을 만들고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 고무 스탬프 추가


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
`createRubberStamp(...)`으로 전화하여 페이지 번호, 직사각형, 제목, 내용, 색상을 알려주세요.

3. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
