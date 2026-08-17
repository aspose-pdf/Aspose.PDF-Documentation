---
title: 필드 이동
linktitle: 필드 이동
type: docs
weight: 30
url: /java/move-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서의 기존 양식 필드를 이동하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: PDF 양식 필드를 Java의 새 위치로 이동
Abstract: 이 문서에서는 Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 기존 PDF를 바인딩하고, 필드를 새 좌표로 이동하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
필드 이동


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
대상 필드 이름과 새 직사각형 좌표를 사용하여 `moveField(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
