---
title: Java의 PDF에서 서명 정보 추출
linktitle: 서명에서 세부정보 추출
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Java의 PDF 파일에서 인증서 및 디지털 서명 세부 정보를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java로 서명된 PDF에서 서명 세부 정보 및 인증서 데이터 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 디지털 서명을 검사하는 방법을 설명합니다. 서명자 세부 정보를 읽고, 서명을 확인하고, 서명이 문서 전체에 적용되는지 확인하고, 내장된 서명 인증서를 추출하고, 기존 서명을 제거하는 방법을 알아보세요.
---
PDF 문서에 이미 존재하는 서명을 검사하고 관리하려면 `PdfFileSignature`을 사용하세요.


## 
서명 정보 읽기


1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩합니다.

1. 
문서 서명 이름에 액세스하고 예제에 필요한 서명 검사 흐름을 구성합니다.

1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드에서 서명 정보를 읽고 확인하세요.
1. 반환된 값을 읽거나 다음 처리 단계를 계속하세요.


```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## 
서명 확인


1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩합니다.

1. 
문서 서명 이름에 액세스하고 예시에 필요한 확인 흐름을 구성합니다.

1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드에서 서명 정보를 읽고 확인하세요.

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## 서명 인증서 추출


1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩합니다.

1. 
인증서 추출에 필요한 문서 서명 이름에 접근합니다.

1. 
추출된 출력을 작성하거나 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드에서 반환된 값을 검사합니다.

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```
