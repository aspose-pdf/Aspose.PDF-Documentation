---
title: 양식 데이터 가져오기 및 내보내기
linktitle: 양식 데이터 가져오기 및 내보내기
type: docs
weight: 80
url: /java/import-export-form-data/
description: Java용 Aspose.PDF를 사용하여 AcroForm 필드 데이터를 XML, FDF, XFDF 및 JSON 형식으로 가져오고 내보냅니다.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 양식 데이터 가져오기 및 내보내기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 AcroForm 데이터를 외부 형식과 교환하는 방법을 설명합니다. Form Facade를 통해 XML, FDF 및 XFDF 데이터를 가져오고 내보내고 양식 필드 값을 JSON으로 추출하는 방법을 다룹니다.
---
Aspose.PDF for Java는 대화형 양식에 대한 몇 가지 일반적인 데이터 교환 형식을 지원합니다.


## 
XML에서 양식 데이터 가져오기



양식 값이 XML 파일에 저장되어 있고 PDF 양식에 적용되어야 하는 경우 이 예를 사용하십시오.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
XML 입력 스트림을 열고 데이터를 양식으로 가져옵니다.
1. 업데이트된 PDF 문서를 저장합니다.


```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
양식 데이터를 XML로 내보내기



현재 AcroForm 값을 XML 형식으로 저장해야 하는 경우 이 예를 사용하십시오.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
XML 파일의 출력 스트림을 엽니다.
1. 양식 데이터를 XML로 내보냅니다.


```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## 
FDF에서 양식 데이터 가져오기



양식 값이 FDF 교환 형식으로 도착하는 경우 이 예를 사용하십시오.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
FDF 입력 스트림을 열고 데이터를 가져옵니다.
1. 채워진 PDF 문서를 저장합니다.


```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
양식 데이터를 FDF로 내보내기



PDF 양식 값을 FDF 파일로 공유해야 하는 경우 이 예를 사용하십시오.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
FDF 파일의 출력 스트림을 엽니다.
1. 양식 데이터를 FDF 형식으로 내보냅니다.


```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## 
XFDF에서 양식 데이터 가져오기



양식 데이터가 XFDF 형식으로 제공되어 PDF로 병합되어야 하는 경우 이 예를 사용하십시오.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
XFDF 입력 스트림을 열고 값을 가져옵니다.
1. 업데이트된 PDF 문서를 저장합니다.


```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
양식 데이터를 XFDF로 내보내기



AcroForm 값에 대한 XML 기반 교환 파일이 필요한 경우 이 예를 사용하십시오.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
XFDF 파일의 출력 스트림을 엽니다.
1. 현재 양식 값을 XFDF로 내보냅니다.


```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## 
양식 필드를 JSON으로 추출



양식 값을 경량 JSON 표현으로 내보내야 하는 경우 이 예를 사용하세요.


1. 
[양식](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) 파사드가 포함된 PDF를 엽니다.

1. 
필드 이름을 반복하고 해당 값을 JSON 텍스트로 직렬화합니다.
1. JSON 콘텐츠를 대상 파일에 씁니다.


```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
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
JSON 추출 도우미 재사용



기본 JSON 내보내기 루틴에 위임하는 전용 래퍼 메서드가 필요한 경우 이 예제를 사용하세요.


1. 
소스 PDF 및 출력 경로를 사용하여 기존 JSON 추출 도우미를 호출합니다.

1. 
직렬화 코드를 복제하지 않고 동일한 추출 논리를 재사용합니다.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
