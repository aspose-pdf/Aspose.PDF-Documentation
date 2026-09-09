---
title: ListBox 필드 만들기
linktitle: ListBox 필드 만들기
type: docs
weight: 40
url: /java/create-listbox-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서에 목록 상자 필드를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 목록 상자 필드 만들기
Abstract: 이 문서에서는 Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 기존 PDF를 바인딩하고, 목록 항목을 정의하고, 목록 상자 필드를 추가하고, 수정된 문서를 저장하는 방법을 보여줍니다.
---
`FormEditorExamples.createListBoxField(...)`을 사용하여 미리 정의된 항목이 포함된 목록 상자를 만듭니다.


## 
목록 상자 필드 만들기


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
`setItems(...)`으로 사용 가능한 목록 항목을 정의합니다.

3. 
기본값과 직사각형을 사용하여 목록 상자 필드를 추가합니다.
4. 업데이트된 문서를 저장합니다.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
