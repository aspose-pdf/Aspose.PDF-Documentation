---
title: 텍스트 필드 채우기
linktitle: 텍스트 필드 채우기
type: docs
weight: 10
url: /java/fill-text-fields/
description: Aspose.PDF의 Form Facade를 사용하여 Java로 PDF 양식의 텍스트 필드를 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java로 PDF의 텍스트 양식 필드 채우기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 텍스트 필드 값을 이름으로 설정하고, Aspose.PDF for Java의 Form 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

`FormExamples.fillTextFields(...)`을 사용하여 텍스트 기반 양식 필드를 채웁니다.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
