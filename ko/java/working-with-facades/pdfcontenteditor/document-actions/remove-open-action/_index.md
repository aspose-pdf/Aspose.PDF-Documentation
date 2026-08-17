---
title: 열린 작업 제거
linktitle: 열린 작업 제거
type: docs
weight: 20
url: /java/remove-open-action/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java의 PDF에서 문서 열기 작업을 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 문서 열기 작업 제거
Abstract: 이 문서에서는 PDF를 바인딩하고, 문서 열기 작업을 제거하고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
문서 열기 작업 제거


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
`removeDocumentOpenAction()`으로 전화하세요.

3. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
