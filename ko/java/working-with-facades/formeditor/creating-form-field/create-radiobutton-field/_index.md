---
title: RadioButton 필드 만들기
linktitle: RadioButton 필드 만들기
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서에 라디오 버튼 필드를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 라디오 버튼 필드 만들기
Abstract: 이 문서에서는 Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 기존 PDF를 바인딩하고, 라디오 버튼 레이아웃 설정을 구성하고, 라디오 버튼 필드를 만들고, 수정된 문서를 저장하는 방법을 보여줍니다.
---

`FormEditorExamples.createRadioButtonField(...)`을 사용하여 사전 정의된 옵션이 있는 라디오 버튼 필드를 만듭니다.


## 
라디오 버튼 필드 생성


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
라디오 버튼 간격, 방향 및 항목 크기를 구성합니다.

3. 
라디오 버튼 항목을 정의합니다.

4. 
기본 선택 및 직사각형을 사용하여 라디오 버튼 필드를 추가합니다.

5. 
업데이트된 문서를 저장합니다.

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
