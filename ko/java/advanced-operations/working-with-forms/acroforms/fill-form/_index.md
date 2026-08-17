---
title: AcroForm 채우기 - Java를 사용하여 PDF 양식 채우기
linktitle: AcroForm 채우기
type: docs
weight: 20
url: /java/fill-form/
description: Java용 Aspose.PDF를 사용하여 PDF 문서의 AcroForm 필드를 채웁니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 파일의 AcroForm 필드를 Java로 채우기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 AcroForm 필드를 채우는 방법을 설명합니다. 이 예에서는 Form Facade를 통해 PDF를 로드하고, 필드 이름을 값 맵과 일치시키고, 일치하는 필드를 업데이트하고, 완성된 문서를 저장합니다.
---

`Form` 외관은 기존 AcroForm에서 필드 채우기를 자동화하는 데 사용할 수 있습니다.


## 
AcroForm 필드를 새 값으로 채우기


1. 
[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드가 있는 PDF 양식 문서를 엽니다.

1. 
양식 필드를 반복하고 제공된 값으로 일치하는 항목을 업데이트합니다.

1. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
