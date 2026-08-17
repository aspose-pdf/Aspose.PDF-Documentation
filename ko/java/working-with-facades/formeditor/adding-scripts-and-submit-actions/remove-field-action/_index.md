---
title: 필드 작업 제거
linktitle: 필드 작업 제거
type: docs
weight: 50
url: /java/remove-field-action/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java의 PDF 양식 필드에서 필드 작업을 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드 작업 제거
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 특정 필드와 관련된 작업을 제거하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
필드 작업 제거


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
대상 필드에 대해 `removeFieldAction(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
