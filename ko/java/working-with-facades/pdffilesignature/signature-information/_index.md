---
title: 서명 정보
linktitle: 서명 정보
type: docs
weight: 60
url: /java/signature-information/
description: PdfFileSignature를 사용하여 Java로 서명된 PDF에서 서명 이름과 서명자 세부 정보를 읽는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java로 PDF 문서에서 서명 세부 정보 읽기
Abstract: Java용 Aspose.PDF를 사용하여 서명 메타데이터를 검사하는 방법을 알아보세요. Java 예제에서는 사용 가능한 첫 번째 서명 이름을 읽은 다음 서명된 PDF에서 서명자, 날짜, 이유 및 위치를 검색합니다.
---
## 서명 정보 얻기



PDF에 서명한 사람과 저장된 서명 메타데이터를 검사해야 할 때 이 작업 과정을 사용하십시오.


### 
단계


1. 
`PdfFileSignature` 인스턴스를 생성하고 서명된 PDF를 바인딩합니다.

2. 
서명 컬렉션을 읽고 서명 이름을 선택하세요.
3. 서명자 이름, 날짜, 이유 및 위치에 대해 서명 정보 접근자에게 전화하십시오.

4. 
완료되면 Facade 객체를 닫습니다.


### 
자바 예

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
