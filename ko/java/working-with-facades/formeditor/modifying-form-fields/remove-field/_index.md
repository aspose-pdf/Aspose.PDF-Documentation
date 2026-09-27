---
title: 필드 제거
linktitle: 필드 제거
type: docs
weight: 40
url: /ko/java/remove-field/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java의 PDF 문서에서 기존 양식 필드를 제거하는 방법을 알아보세요.
lastmod: "2026-09-24"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드 삭제
Abstract: 이 문서에서는 Aspose.PDF for Java에서 FormEditor 파사드를 사용하여 기존 PDF를 바인딩하고, 지정된 필드를 제거하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 필드 제거

1. 소스 PDF를 `FormEditor` 파사드에 바인딩하세요.
2. 대상 필드 이름을 인수로 전달하여 `removeField(...)`를 호출하세요.
3. 업데이트된 문서를 저장하세요.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
