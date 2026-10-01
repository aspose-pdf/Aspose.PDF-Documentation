---
title: 서명 확인
linktitle: 서명 확인
type: docs
weight: 90
url: /ko/java/signature-verification/
description: PdfFileSignature 파사드를 사용하여 Java에서 PDF 서명을 확인하는 방법을 알아보세요.
lastmod: "2026-09-24"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 서명 확인
Abstract: Aspose.PDF for Java를 사용하여 PDF 서명을 확인하는 방법을 알아보세요. Java 예제에서는 사용 가능한 첫 번째 서명을 선택하고 서명의 유효성을 검사한 다음 서명이 전체 문서에 적용되는지 확인합니다.
---
## PDF 서명 확인

기존 서명된 PDF에 대한 빠른 유효성 검사가 필요한 경우 이 작업 과정을 사용하세요.

### 단계

1. `PdfFileSignature` 인스턴스를 생성하고 서명된 PDF를 바인딩하세요.
2. 검사하려는 서명 이름을 선택하세요.
3. 서명을 확인하려면 `verifySignature`를 호출하세요.
4. 적용 범위를 확인하려면 `coversWholeDocument`를 호출하세요.
5. Facade 개체를 닫으세요.

### Java 예제```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
