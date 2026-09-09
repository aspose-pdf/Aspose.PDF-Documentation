---
title: 외부 필드 복사
linktitle: 외부 필드 복사
type: docs
weight: 80
url: /java/copy-outer-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 한 PDF 문서의 양식 필드를 다른 PDF 문서로 복사하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java 문서 간에 PDF 양식 필드 복사
Abstract: 이 문서에서는 대상 PDF를 생성하고, 이를 FormEditor 파사드에 바인딩하고, 다른 문서의 필드를 복사하고, Java용 Aspose.PDF를 사용하여 결과를 저장하는 방법을 보여줍니다.
---
## 다른 PDF에서 필드 복사


1. 
최소한 한 페이지가 포함된 대상 PDF를 만듭니다.

2. 
대상 PDF를 `FormEditor` 파사드에 바인딩합니다.

3. 
원본 문서 경로, 필드 이름, 대상 페이지 및 좌표를 사용하여 `copyOuterField(...)`으로 전화하세요.

4. 
업데이트된 대상 문서를 저장합니다.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
