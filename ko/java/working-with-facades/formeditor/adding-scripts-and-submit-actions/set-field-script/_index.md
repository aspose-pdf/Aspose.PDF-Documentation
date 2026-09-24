---
title: 필드 스크립트 설정
linktitle: 필드 스크립트 설정
type: docs
weight: 20
url: /java/set-field-script/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java의 PDF 양식 필드에서 JavaScript 작업을 할당하거나 업데이트하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java의 PDF 양식 필드에 JavaScript 동작 설정
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 초기 스크립트를 추가하고, 이를 업데이트된 스크립트로 바꾸고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 수정된 문서를 저장하는 방법을 보여줍니다.
---
## 필드 스크립트 설정


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
필드에 초기 JavaScript 작업을 추가합니다.

3. 
업데이트된 스크립트 텍스트로 바꾸세요.

4. 
업데이트된 문서를 저장합니다.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
