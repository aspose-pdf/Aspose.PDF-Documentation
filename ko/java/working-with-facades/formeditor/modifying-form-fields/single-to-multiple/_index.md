---
title: 단일 대 다중
linktitle: 단일 대 다중
type: docs
weight: 60
url: /java/single-to-multiple/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java의 PDF 문서에서 한 줄 텍스트 필드를 여러 줄 필드로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 한 줄 PDF 필드를 여러 줄로 변환
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 한 줄 필드를 여러 줄 필드로 변환하고, Aspose.PDF for Java의 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 한 줄 필드를 여러 줄로 변환


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
대상 필드 이름은 `single2Multiple(...)`으로 전화하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
