---
title: 라디오 버튼 필드 채우기
linktitle: 라디오 버튼 필드 채우기
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: Aspose.PDF의 Form Facade를 사용하여 Java가 포함된 PDF 양식에서 라디오 버튼 값을 선택하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 라디오 버튼 필드 옵션을 선택하세요.
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 인덱스별로 라디오 버튼 옵션을 선택하고, Java용 Aspose.PDF에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

라디오 버튼 옵션을 선택하려면 `FormExamples.fillRadioButtonFields(...)`을 사용하세요.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
