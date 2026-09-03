---
title: 목록 항목 삭제
linktitle: 목록 항목 삭제
type: docs
weight: 20
url: /java/del-list-item/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서의 목록 필드에서 항목을 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java의 PDF 양식 필드에서 목록 항목 삭제
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 목록 필드에서 특정 항목을 제거하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 목록 필드에서 항목 삭제


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
제거할 대상 필드 및 항목에 대해 `delListItem(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
