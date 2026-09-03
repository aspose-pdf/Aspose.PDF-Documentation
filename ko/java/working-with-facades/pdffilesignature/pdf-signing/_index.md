---
title: PDF 문서에 서명
linktitle: PDF 문서에 서명
type: docs
weight: 10
url: /java/pdf-signing/
description: PdfFileSignature 파사드를 사용하여 Java에서 PDF 문서에 서명하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java의 디지털 서명으로 PDF 문서에 서명
Abstract: Java용 Aspose.PDF를 사용하여 PDF 문서에 서명하는 방법을 알아보세요. Java 예제 세트는 구성된 인증서 경로 및 비밀번호를 사용한 서명과 이유, 연락처 정보, 위치 및 권한과 같은 서명 메타데이터가 포함된 명시적 PKCS7 서명 개체를 사용한 서명을 다룹니다.
---
## PDF 문서에 서명



PDF에 눈에 보이는 디지털 서명을 적용해야 하는 경우 `PdfFileSignature`을 사용하세요.


### 
단계


1. 
`PdfFileSignature` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
`setCertificate`을 통해 또는 `PKCS7` 객체를 생성하여 인증서를 로드합니다.
3. 대상 페이지, 가시성 설정, 서명 사각형 및 서명 데이터를 사용하여 `sign`으로 전화하세요.

4. 
서명된 PDF를 저장하고 Facade 객체를 닫습니다.


### 
자바 예제

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
