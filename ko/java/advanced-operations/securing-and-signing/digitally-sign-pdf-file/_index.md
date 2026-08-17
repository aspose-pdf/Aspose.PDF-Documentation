---
title: Java에서 디지털 서명 추가 또는 PDF에 디지털 서명
linktitle: PDF에 디지털 서명
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Aspose.PDF를 사용하여 Java에서 PDF 문서에 디지털 서명하고 인증하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 디지털 서명
Abstract: 이 가이드에서는 Java용 Aspose.PDF를 사용하여 PDF 문서에 디지털 서명하는 방법을 설명합니다. 인증서 객체로 서명하고, 기본 인증서 매개변수로 서명하고, 허용된 서명 후 변경 사항을 제어하기 위해 DocMDP 서명으로 문서를 인증하는 방법을 다룹니다.
---

Java용 Aspose.PDF는 `PdfFileSignature`을 통해 여러 서명 흐름을 지원합니다.


## 
인증서 개체로 PDF에 서명


1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩합니다.

1. 
[PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) 서명 개체를 생성하고 서명 옵션을 구성합니다.

1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)를 통해 PDF 문서에 서명을 적용합니다.

1. 
업데이트된 PDF 문서를 저장합니다.


```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```


이 접근 방식은 `PKCS7` 서명 개체를 먼저 작성한 다음 이를 페이지 1에 적용합니다.


## 
기본 인증서 매개변수를 사용하여 PDF에 서명


1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩합니다.

1. 
서명 예시에 필요한 인증서 매개변수를 구성합니다.

1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)를 통해 PDF 문서에 서명을 적용합니다.

1. 
업데이트된 PDF 문서를 저장합니다.


```java
public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

## 
DocMDP로 PDF 인증



인증 수준 제한이 필요한 경우 문서 수정 감지 및 방지 서명을 사용하세요.


1. 
[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩합니다.

1. 
[DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) 개체를 생성하고 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) 서명 옵션을 구성합니다.

1. 
인증 서명을 적용하고 업데이트된 PDF 문서를 저장하세요.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
