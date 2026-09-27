---
title: 양식 필드 이름 바꾸기
linktitle: 양식 필드 이름 바꾸기
type: docs
weight: 30
url: /ko/java/rename-form-fields/
description: Aspose.PDF의 Form Facade를 사용하여 Java에서 PDF 양식 필드의 이름을 바꾸는 방법을 알아보세요.
lastmod: "2026-09-24"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 문서의 양식 필드 이름 바꾸기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 기존 필드의 이름을 바꾸고, Aspose.PDF for Java에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
대화형 PDF 양식에서 필드 이름을 바꾸려면 `FormExamples.renameFormFields(...)`를 사용하세요.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
