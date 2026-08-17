---
title: Java에서 PDF를 Excel로 변환
linktitle: PDF를 엑셀로 변환
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: XML 스프레드시트 2003, XLSX, XLSM, CSV 및 ODS 출력을 포함하여 Aspose.PDF를 사용하여 Java에서 PDF 파일을 Excel로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF를 Excel로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 Excel 호환 형식으로 변환하는 방법을 설명합니다. 여기에는 빈 열 삽입 옵션과 워크시트 수 최소화 옵션과 함께 XML 스프레드시트 2003, XLSX, XLSM, CSV 및 ODS 출력이 포함됩니다.
---

Aspose.PDF for Java는 PDF 콘텐츠를 다양한 레이아웃 옵션을 사용하여 여러 스프레드시트 형식으로 내보낼 수 있습니다. [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 사용하여 대상 통합 문서 형식을 선택하고 페이지 콘텐츠가 워크시트 및 열에 매핑되는 방식을 제어하세요.


## 
PDF를 Excel 2003 XML로 변환



PDF 컨텐츠를 Excel 2003 XML 스프레드시트 형식으로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만들고 형식을 `XMLSpreadSheet2003`으로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하면 로드된 PDF가 Excel 2003 XML 스키마에 직렬화됩니다.

1. 
변환된 출력 파일을 저장합니다.


```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 XLSX로 변환



PDF 콘텐츠를 Excel 2007+ XLSX 형식으로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만들고 형식을 `XLSX`으로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하여 PDF 레이아웃을 Office Open XML 통합 문서로 내보냅니다.

1. 
출력 스프레드시트 파일을 저장합니다.


```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
열 제어를 사용하여 PDF를 XLSX로 변환



PDF에서 Excel로 변환하는 동안 열 처리를 조정해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`XLSX` 출력을 위한 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만듭니다.

1. 
PDF에서 생성된 워크시트 레이아웃을 개선하기 위해 추가 선행 열이 필요한 경우 `setInsertBlankColumnAtFirst(true)`을 활성화합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화해서 변환된 XLSX 파일을 작성하세요.


```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 단일 Excel 워크시트로 변환



모든 PDF 페이지를 하나의 워크시트로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`XLSX` 내보내기를 위해 [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만듭니다.

1. 
`setMinimizeTheNumberOfWorksheets(true)`을 활성화하면 여러 PDF 페이지가 더 적은 수의 워크시트로 통합됩니다.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하고 XLSX 출력 파일을 저장합니다.


```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 XLSM으로 변환



PDF 출력을 매크로 지원 Excel 통합 문서로 저장해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만들고 형식을 `XLSM`으로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF 콘텐츠가 매크로 지원 통합 문서 컨테이너로 내보내집니다.

1. 
XLSM 파일을 저장합니다.


```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 CSV로 변환



PDF 표 형식 콘텐츠를 CSV로 내보내야 하는 경우 이 예를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만들고 형식을 `CSV`으로 설정합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF 콘텐츠가 쉼표로 구분된 텍스트 출력으로 병합됩니다.

1. 
생성된 CSV 파일을 저장합니다.


```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 ODS로 변환



PDF 컨텐츠를 OpenDocument 스프레드시트 형식으로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)을 만들고 형식을 `ODS`으로 설정합니다.

1. 
PDF를 OpenDocument 스프레드시트 형식으로 내보내려면 `document.save(outputFile.toString(), saveOptions)`으로 전화하세요.

1. 
변환된 ODS 파일을 저장합니다.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
