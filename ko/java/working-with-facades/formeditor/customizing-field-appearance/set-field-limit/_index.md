---
title: 필드 제한 설정
linktitle: 필드 제한 설정
type: docs
weight: 50
url: /java/set-field-limit/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 양식 필드의 최대 문자 제한을 설정하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드의 문자 제한 설정
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 필드의 최대 문자 제한을 설정하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
필드 글자 수 제한 설정


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
대상 필드 및 최대 문자 수를 확인하려면 `setFieldLimit(...)`으로 전화하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
