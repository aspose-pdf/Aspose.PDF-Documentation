---
title: 서명 추출
linktitle: 서명 추출
type: docs
weight: 50
url: /java/signature-extraction/
description: PdfFileSignature를 사용하여 Java로 서명된 PDF에서 서명 인증서를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java의 PDF에서 서명 인증서 추출
Abstract: Aspose.PDF for Java를 사용하여 PDF 서명과 관련된 인증서를 추출하는 방법을 알아보세요. 현재 Java 예제 세트에는 출력 스트림에 대한 인증서 추출이 포함되어 있지만 별도의 서명 이미지 추출 샘플은 포함되어 있지 않습니다.
---
## 서명 인증서 추출



기존 서명과 연결된 인증서를 저장해야 하는 경우 이 워크플로를 사용하세요.


### 
단계


1. 
`PdfFileSignature` 인스턴스를 생성하고 서명된 PDF를 바인딩합니다.

2. 
검사할 서명 이름을 선택하세요.
3. 인증서 스트림을 열려면 `extractCertificate`으로 전화하세요.

4. 
인증서 바이트를 출력 파일에 복사합니다.

5. 
스트림 리소스와 Facade 객체를 닫습니다.


### 
자바 예


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


현재 `PdfFileSignatureExamples.java` 클래스에는 렌더링된 서명 이미지를 추출하기 위한 전용 Java 샘플이 포함되어 있지 않습니다.
