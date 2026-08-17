---
title: 모든 필드를 평면화
linktitle: 모든 필드를 평면화
type: docs
weight: 10
url: /java/flatten-all-fields/
description: Aspose.PDF의 Form Facade를 사용하여 Java에서 모든 PDF 양식 필드를 평면화하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 모든 대화형 양식 필드를 Java의 정적 콘텐츠로 변환
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 모든 양식 필드를 평면화하고, Java용 Aspose.PDF에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

모든 대화형 필드를 정적 페이지 콘텐츠로 변환해야 하는 경우 `FormExamples.flattenAllFields(...)`을 사용하세요.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
