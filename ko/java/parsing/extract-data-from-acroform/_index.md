---
title: Java를 사용하여 AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF를 사용하면 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있습니다. AcroForms에서 데이터를 추출하고 이를 JSON, XML 또는 FDF 형식으로 저장하는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 통해 AcroForm에서 데이터를 추출하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에서 AcroForm 데이터를 추출하고 내보내는 방법을 설명합니다. 모든 양식 필드 읽기, 이름으로 필드 값 검색, 필드 데이터를 JSON으로 내보내기, 양식 데이터를 XML, FDF 및 XFDF 형식으로 쓰기 등을 다룹니다.
---
## 
모든 양식 필드 추출



전체 문서 개체 모델을 통해 작업하지 않고 필드 이름과 값을 읽으려면 `com.aspose.pdf.facades.Form`을 사용하세요.


1. 
전체 문서 객체 모델을 순회하지 않고도 AcroForm 필드를 읽을 수 있도록 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드로 소스 PDF 양식을 엽니다.

1. 
양식에 있는 모든 필드 식별자를 수집하려면 `getFieldNames()`으로 전화하세요.

1. 
해당 필드 이름을 반복하고 `getField(fieldName)`을 호출하여 각 필드 값을 읽습니다.

1. 
추출된 키-값 쌍에서 출력 문자열을 작성하고 집계된 양식 데이터를 인쇄합니다.

1. 
`finally` 블록에서 [양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드를 닫습니다.


```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## 
이름으로 필드 값 검색


1. 
[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드를 사용하여 소스 PDF 양식을 엽니다.

1. 
AcroForm 데이터에서 현재 값을 읽으려면 요청된 필드 이름으로 `getField(fieldName)`을 호출하세요.

1. 
추출된 필드 값을 인쇄합니다.

1. 
`finally` 블록에서 [양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드를 닫습니다.


```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## 
양식 필드를 JSON으로 내보내기


1. 
[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드를 사용하여 소스 PDF 양식을 엽니다.

1. 
AcroForm에서 사용 가능한 모든 필드 식별자를 수집하려면 `getFieldNames()`으로 전화하세요.

1. 
해당 필드를 반복하고, 이름과 값을 이스케이프하고, JSON 개체 문자열을 빌드합니다.

1. 
JSON 결과를 출력 파일에 씁니다.

1. 
`finally` 블록에서 [양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드를 닫습니다.


```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## 
양식 데이터를 XML, FDF 및 XFDF로 내보내기


1. 
아직 문서를 바인딩하지 않고 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하세요.

1. 
XML 파일의 출력 스트림을 열고 `bindPdf(...)`을 사용하여 소스 PDF를 Facade에 바인딩합니다.

1. 
`exportXml(stream)`을 호출하면 현재 양식 필드 데이터가 XML로 직렬화됩니다.

1. 
내보내기가 완료된 후 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 닫습니다.


```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

1. 
아직 문서를 바인딩하지 않고 [양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 만듭니다.

1. 
FDF 파일의 출력 스트림을 열고 `bindPdf(...)`을 사용하여 소스 PDF를 Facade에 바인딩합니다.

1. 
양식 필드 데이터가 FDF 형식으로 직렬화되도록 `exportFdf(stream)`을 호출하세요.

1. 
내보내기가 완료된 후 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 닫습니다.


```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

1. 
아직 문서를 바인딩하지 않고 [양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 만듭니다.

1. 
XFDF 파일의 출력 스트림을 열고 `bindPdf(...)`을 사용하여 소스 PDF를 Facade에 바인딩합니다.

1. 
`exportXfdf(stream)`을 호출하면 양식 필드 데이터가 XFDF 형식으로 직렬화됩니다.

1. 
내보내기가 완료된 후 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 닫습니다.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
