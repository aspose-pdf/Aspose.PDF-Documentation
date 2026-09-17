---
title: 문서 작업 추가
linktitle: 문서 작업 추가
type: docs
weight: 10
url: /java/add-document-action/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 PDF에 문서 열기 작업을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF에 문서 열기 작업 추가
Abstract: 이 문서에서는 PDF를 바인딩하고, 문서 열기 이벤트에 JavaScript 작업을 연결하고, Java용 Aspose.PDF에서 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 문서 열기 작업 추가


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
`DOCUMENT_OPEN` 이벤트와 JavaScript 동작 텍스트를 사용하여 `addDocumentAdditionalAction(...)`을 호출합니다.

3. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
