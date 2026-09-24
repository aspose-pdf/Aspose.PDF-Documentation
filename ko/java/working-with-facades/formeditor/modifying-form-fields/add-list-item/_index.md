---
title: 목록 항목 추가
linktitle: 목록 항목 추가
type: docs
weight: 10
url: /java/add-list-item/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서의 목록 필드에 항목을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java의 PDF 양식 필드에 목록 항목 추가
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 목록 필드에 새 항목을 추가하고, Java용 Aspose.PDF의 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 목록 필드에 항목 추가


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
대상 필드와 새 표시/값 쌍에 대해 `addListItem(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
