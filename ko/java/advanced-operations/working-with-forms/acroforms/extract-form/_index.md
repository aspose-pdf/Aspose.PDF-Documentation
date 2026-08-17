---
title: AcroForm 추출 - Java의 PDF에서 양식 데이터 추출
linktitle: AcroForm 추출
type: docs
weight: 30
url: /java/extract-form/
description: Aspose.PDF for Java를 사용하여 PDF 문서의 AcroForm 필드에서 값을 추출합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에서 양식 필드 값 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 AcroForm 필드에서 데이터를 추출하는 방법을 보여줍니다. 예제에서는 Form 파사드를 사용하여 필드 이름을 반복하고, 각 현재 값을 읽고, 다운스트림 처리를 위해 결과를 맵에 저장합니다.
---

필드-값 추출 흐름에 대한 간단한 필드 이름이 필요한 경우 `Form` 외관을 사용하세요.


## 
모든 AcroForm 필드에서 값 추출


1. 
[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드가 있는 PDF 양식 문서를 엽니다.

1. 
[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드의 필드 이름을 반복하고 각 현재 필드 값을 맵으로 읽어옵니다.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
