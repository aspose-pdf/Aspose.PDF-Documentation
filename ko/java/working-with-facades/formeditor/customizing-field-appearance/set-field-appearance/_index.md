---
title: 필드 모양 설정
linktitle: 필드 모양 설정
type: docs
weight: 40
url: /java/set-field-appearance/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 양식 필드의 시각적 모양 플래그를 변경하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드 표시 플래그 변경
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 필드에 모양 플래그를 적용하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
필드 표시 플래그 설정


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
대상 필드와 선택한 주석 플래그에 대해 `setFieldAppearance(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
