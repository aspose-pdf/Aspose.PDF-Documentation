---
title: 필드 정렬 설정
linktitle: 필드 정렬 설정
type: docs
weight: 20
url: /ko/java/set-field-alignment/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 양식 필드의 가로 텍스트 정렬을 설정하는 방법을 알아보세요.
lastmod: "2026-09-24"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드 정렬 설정
Abstract: 이 문서에서는 Aspose.PDF for Java에서 FormEditor 파사드를 사용하여 기존 PDF를 바인딩하고, 수평 필드 정렬을 설정하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 수평 필드 정렬 설정

1. 소스 PDF를 `FormEditor` 파사드에 바인딩하세요.
2. 대상 필드와 원하는 정렬 상수에 대해 `setFieldAlignment(...)`를 호출하세요.
3. 업데이트된 문서를 저장하세요.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
