---
title: ComboBox 필드 만들기
linktitle: ComboBox 필드 만들기
type: docs
weight: 30
url: /java/create-combobox-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서에 콤보 상자 필드를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 콤보 상자 필드 만들기
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 콤보 상자 필드를 추가하고, 항목으로 채우고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 수정된 문서를 저장하는 방법을 보여줍니다.
---
콤보 상자를 만들고 선택 가능한 항목을 추가하려면 `FormEditorExamples.createComboBoxField(...)`을 사용하세요.


## 
콤보 상자 필드 만들기


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
기본값과 대상 사각형을 사용하여 콤보 상자 필드를 추가합니다.

3. 
선택 가능한 콤보 상자 항목을 추가합니다.
4. 업데이트된 문서를 저장합니다.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
