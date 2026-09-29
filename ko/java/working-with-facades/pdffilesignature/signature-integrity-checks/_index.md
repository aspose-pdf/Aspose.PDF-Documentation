---
title: 서명 무결성 검사
linktitle: 서명 무결성 검사
type: docs
weight: 70
url: /ko/java/signature-integrity-checks/
description: PdfFileSignature 파사드를 사용하여 Java에서 서명 적용 범위와 무결성을 검증하는 방법을 알아보세요.
lastmod: "2026-09-24"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 서명 적용 범위 및 무결성 검증
Abstract: Aspose.PDF for Java를 사용하여 서명 무결성을 검사하는 방법을 알아보세요. 현재 Java 예제 세트는 `verifySignature`를 사용하여 선택한 서명을 검증하고 `coversWholeDocument`를 사용하여 서명이 전체 PDF를 보호하는지 여부를 결정합니다.
---
## 서명 무결성 확인

이 문서는 `PdfFileSignatureExamples.java`에서 공개한 것과 동일한 확인 작업 흐름에 매핑됩니다.

### 단계

1. 서명된 PDF를 `PdfFileSignature`로 바인딩하세요.
2. 문서에서 서명 이름을 선택하세요.
3. 서명 내용을 확인하려면 `verifySignature`를 호출하세요.
4. 문서 전체 적용 범위를 확인하려면 `coversWholeDocument`를 호출하세요.
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
