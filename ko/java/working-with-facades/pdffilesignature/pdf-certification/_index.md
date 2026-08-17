---
title: PDF 인증
linktitle: PDF 인증
type: docs
weight: 30
url: /java/pdf-certification/
description: PdfFileSignature 및 DocMDPSignature를 사용하여 Java에서 PDF 문서를 인증하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 DocMDP 권한으로 PDF 문서 인증
Abstract: Java용 Aspose.PDF를 사용하여 PDF 문서를 인증하는 방법을 알아보세요. Java 예제에서는 DocMDPSignature 및 DocMDPAccessPermissions와 함께 PdfFileSignature를 사용하여 양식 작성 및 서명을 위한 문서를 인증하는 동시에 다른 종류의 수정을 제한합니다.
---
## 
PDF 문서 인증



문서를 신뢰해야 하지만 서명 후 정의된 변경 클래스를 허용해야 하는 경우 인증을 사용합니다.


### 
단계


1. 
`PdfFileSignature` 인스턴스를 생성하고 소스 PDF를 바인딩합니다.

2. 
인증서와 인증서 비밀번호를 사용하여 `PKCS7` 서명 개체를 빌드합니다.

3. 
필수 `DocMDPAccessPermissions` 값을 사용하여 해당 서명을 `DocMDPSignature`로 래핑합니다.

4. 
대상 페이지, 서명 메타데이터, 표시되는 직사각형 및 MDP 서명을 사용하여 `certify`을 호출하세요.

5. 
인증된 PDF를 저장하고 Facade 객체를 닫습니다.


### 
자바 예

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
