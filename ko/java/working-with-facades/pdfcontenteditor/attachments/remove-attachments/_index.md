---
title: 첨부 파일 제거
linktitle: 첨부 파일 제거
type: docs
weight: 50
url: /java/remove-attachments/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java의 PDF에서 모든 문서 첨부 파일을 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 모든 PDF 첨부 파일 제거
Abstract: 이 문서에서는 PDF를 바인딩하고, 모든 문서 첨부 파일을 삭제하고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 파일을 저장하는 방법을 보여줍니다.
---
## 
모든 첨부 파일 제거


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
포함된 모든 첨부 파일을 제거하려면 `deleteAttachments()`으로 전화하세요.

3. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
