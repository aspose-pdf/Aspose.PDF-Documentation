---
title: 필드 이름 바꾸기
linktitle: 필드 이름 바꾸기
type: docs
weight: 50
url: /java/rename-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서의 기존 양식 필드 이름을 바꾸는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드 이름 바꾸기
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 지정된 필드의 이름을 바꾸고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
필드 이름 바꾸기


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
현재 필드 이름과 새 필드 이름을 사용하여 `renameField(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
