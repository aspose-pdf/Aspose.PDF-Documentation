---
title: 내부 필드 복사
linktitle: 내부 필드 복사
type: docs
weight: 70
url: /java/copy-inner-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 동일한 PDF 문서 내의 새 위치에 양식 필드를 복사하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java의 동일한 문서 내에서 PDF 양식 필드 복사
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 필드를 다른 페이지 및 위치에 복제하고, Java용 Aspose.PDF의 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 동일한 PDF 내의 필드 복사


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
소스 필드 이름, 새 필드 이름, 페이지 및 좌표를 사용하여 `copyInnerField(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
