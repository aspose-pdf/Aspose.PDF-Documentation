---
title: 양식 값 읽기
linktitle: 양식 값 읽기
type: docs
weight: 60
url: /java/reading-form-values/
description: Aspose.PDF의 Form Facade를 사용하여 Java에서 PDF 양식 필드 이름과 값을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 필드 이름 및 값 읽기
Abstract: 이 섹션에서는 Aspose.PDF for Java에 대해 설정된 현재 Form Facade 예제에 구현된 Java 양식 읽기 워크플로를 다룹니다. 저장소는 일반적인 필드 검사 예를 제공하고 아직 일치하는 Java 샘플이 없는 특수 페이지에 대해 명시적인 범위 참고 사항을 사용합니다.
---

Java `FormExamples` 클래스는 Facades API에 의해 노출되는 주요 양식 처리 작업 흐름을 보여줍니다.


## 
필드 값 가져오기



필드 이름과 현재 값을 검사하려면 `FormExamples.inspectFormFields(...)`을 사용하세요.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
