---
title: CheckBox 필드 만들기
linktitle: CheckBox 필드 만들기
type: docs
weight: 20
url: /java/create-checkbox-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서에 확인란 양식 필드를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 체크박스 필드 만들기
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 지정된 위치에 확인란 필드를 추가하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 수정된 문서를 저장하는 방법을 보여줍니다.
---

`FormEditorExamples.createCheckBoxField(...)`을 사용하여 PDF 양식에 확인란 필드를 추가합니다.


## 
체크박스 필드 생성


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
`FieldType.CheckBox`이 포함된 확인란 필드, 필드 이름, 캡션, 페이지 및 직사각형을 추가합니다.

3. 
업데이트된 문서를 저장합니다.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
