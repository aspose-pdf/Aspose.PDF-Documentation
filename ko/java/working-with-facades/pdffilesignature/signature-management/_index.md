---
title: 서명 관리
linktitle: 서명 관리
type: docs
weight: 80
url: /java/signature-management/
description: PdfFileSignature 파사드를 사용하여 Java에서 기존 PDF 서명을 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 서명 제거
Abstract: Java용 Aspose.PDF를 사용하여 서명된 PDF에서 서명을 제거하는 방법을 알아보세요. 현재 Java 예제 세트에서는 이름으로 기존 서명을 제거하고 업데이트된 문서를 저장하는 방법을 다룹니다. 연관된 서명 필드를 정리하기 위한 별도의 샘플은 포함되어 있지 않습니다.
---
## 
서명 제거



문서에서 기존 디지털 서명을 제거해야 하는 경우 이 작업 흐름을 사용하십시오.


### 
단계


1. 
`PdfFileSignature` 인스턴스를 생성하고 서명된 PDF를 바인딩합니다.

2. 
서명 컬렉션을 읽고 서명 이름을 선택하세요.

3. 
그 이름으로 `removeSignature`으로 전화하세요.

4. 
업데이트된 파일을 저장하고 Facade 객체를 닫습니다.


### 
자바 예


```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```


현재 Java 샘플 세트에는 서명 삭제 후 관련 서명 필드를 제거하는 별도의 방법이 포함되어 있지 않습니다.
