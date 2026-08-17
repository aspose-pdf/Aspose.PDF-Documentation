---
title: 첨부파일 추가
linktitle: 첨부파일 추가
type: docs
weight: 10
url: /java/add-attachment/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 PDF 문서에 외부 파일을 첨부하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF에 첨부 파일 추가
Abstract: 이 문서에서는 PDF를 바인딩하고, 첨부 파일을 스트림으로 열고, 설명과 함께 문서 첨부 파일을 추가하고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 파일을 저장하는 방법을 보여줍니다.
---
## 
문서 첨부 추가


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
첨부 파일을 입력 스트림으로 엽니다.

3. 
스트림, 파일 이름, 설명과 함께 `addDocumentAttachment(...)`으로 전화하세요.

4. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
