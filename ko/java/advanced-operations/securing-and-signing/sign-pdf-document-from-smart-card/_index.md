---
title: Java에서 스마트 카드로 PDF 문서 서명
linktitle: 스마트 카드를 사용한 PDF 서명
type: docs
weight: 30
url: /ko/java/sign-pdf-document-from-smart-card/
description: Aspose.PDF에서 인증서 기반 PDF 서명에 대한 현재 Java 예제 적용 범위를 검토하세요.
lastmod: "2026-09-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 현재 Java 예제 세트의 인증서 기반 PDF 서명 적용 범위
Abstract: 이 페이지에서는 Java 문서 소스 트리에서 사용할 수 있는 서명 예제의 현재 범위를 설명합니다. 저장소에는 PFX 또는 PKCS7 자격 증명이 포함된 인증서 기반 PDF 서명 예제가 포함되어 있지만 현재 Java용 전용 스마트 카드 인증서 저장소 예제는 포함되어 있지 않습니다.
---
현재 Java 저장소에는 `facades/pdffilesignature` 아래에 전용 소스 지원 스마트 카드 서명 예제가 포함되어 있지 않지만 다음 작업 흐름은 로컬 인증서 저장소에서 선택한 인증서로 PDF에 서명하기 위한 일반적인 API 패턴을 보여줍니다.

## 스마트 카드에서 PDF 문서에 서명

1. 원본 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 여세요.
1. [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드를 생성하고 소스 PDF 문서를 바인딩하세요.
1. 로컬 인증서를 검색하고 필수 [`ExternalSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/)를 생성하세요.
1. 시각적 시그니처 모양과 대상 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 구성하세요.
1. [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)를 통해 PDF 문서에 서명을 적용하세요.
1. 업데이트된 PDF 문서를 저장하세요.
1. `bindPdf(...)`를 사용하여 로드된 문서를 [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 파사드에 바인딩하세요.
1. `getLocalCertificate()`를 호출하여 스마트 카드 자격 증명을 나타내는 로컬 인증서를 검색하세요.
1. 인증서가 발견되었는지 확인하세요. 그렇지 않은 경우 변경되지 않은 출력 파일을 저장하고 워크플로를 중지하세요.
1. 선택한 인증서에서 [`ExternalSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/)를 생성하세요.
1. `setSignatureAppearance(...)`으로 시각적 시그니처 외관 이미지를 설정하세요.
1. 대상 페이지, 사유, 연락처, 위치, 가시성 플래그, 서명[`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), 외부 서명 개체를 가지고 `sign(...)`를 호출하세요.
1. 서명된 PDF를 출력 경로에 저장하세요.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
