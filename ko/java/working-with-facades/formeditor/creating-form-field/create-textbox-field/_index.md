---
title: TextBox 필드 만들기
linktitle: TextBox 필드 만들기
type: docs
weight: 10
url: /java/create-textbox-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서에 텍스트 상자 필드를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 텍스트 양식 필드 만들기
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 기본값이 있는 텍스트 필드를 추가하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 수정된 문서를 저장하는 방법을 보여줍니다.
---

PDF 양식에 텍스트 필드를 추가하려면 `FormEditorExamples.createTextBoxField(...)`을 사용하십시오.


## 
텍스트 상자 필드 만들기


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
`FieldType.Text`, 필드 이름, 기본값, 페이지 번호 및 직사각형을 사용하여 각 텍스트 필드를 추가합니다.

3. 
업데이트된 문서를 저장합니다.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
