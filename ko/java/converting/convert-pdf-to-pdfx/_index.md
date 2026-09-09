---
title: Java에서 PDF를 PDF/A, PDF/E 및 PDF/X로 변환
linktitle: PDF를 PDF/A, PDF/E 및 PDF/X로 변환
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: 보관, 엔지니어링, 접근성 및 인쇄 워크플로를 위해 Aspose.PDF를 사용하여 Java에서 PDF 파일을 PDF/A, PDF/E 및 PDF/X로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF를 PDF/x 형식으로 변환하는 방법
Abstract: 이 문서에서는 Java용 Aspose.PDF를 사용하여 PDF 문서의 유효성을 검사하고 PDF/A, PDF/E 및 PDF/X 형식으로 변환하는 방법을 설명합니다. 로그 생성, PDF/A-3의 첨부 파일 보존, 누락된 글꼴 대체, 자동 태그 지정, ICC 프로필 구성 및 출력 의도 설정을 다룹니다.
---
Java용 Aspose.PDF는 표준 PDF 파일을 검증하고 보관 및 교환 지향 PDF 표준으로 변환할 수 있습니다.


## 
PDF를 PDF/A로 변환



표준 PDF를 PDF/A 호환 보관 문서로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` 및 [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`로 `document.convert(...)`에 전화하세요.
1. 변환 중에 규정 준수 문제가 기록되도록 유효성 검사 로그를 사이드카 XML 파일에 기록합니다.

1. 
검증된 PDF/A 출력을 저장합니다.


```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## 
PDF를 PDF/E로 변환



PDF를 엔지니어링 중심의 PDF/E 표준으로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1`에 대한 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/)과 원하는 로그 파일 경로를 만듭니다.
1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
`document.convert(options)`을 호출하면 준비된 옵션 개체를 사용하여 규정 준수 변환이 실행됩니다.

1. 
결과 규격 PDF 파일을 저장합니다.


```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## 
PDF를 PDF/X로 변환



PDF를 인쇄용 PDF/X 표준으로 변환해야 하는 경우 이 예를 사용하십시오.

1. [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4`에 대한 [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/)과 원하는 로그 파일 경로를 만듭니다.

1. 
인쇄 대상 색상 프로필이 변환 설정에 포함되도록 `FOGRA39`과 같은 [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/)을 구성합니다.

1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 열고 `document.convert(options)`으로 전화하세요.

1. 
변환된 PDF/X 출력을 저장합니다.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
