---
title: 확인란 필드 채우기
linktitle: 확인란 필드 채우기
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: Aspose.PDF의 Form Facade를 사용하여 Java로 PDF 양식의 확인란 필드를 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 양식의 확인란 필드 값 설정
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 확인란 필드를 이름으로 설정하고, Java용 Aspose.PDF에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
양식에 확인란 값을 설정하려면 `FormExamples.fillCheckBoxFields(...)`을 사용하세요.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
