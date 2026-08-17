---
title: PDF 파일 암호 해독
linktitle: PDF 파일 암호 해독
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: PdfFileSecurity 파사드를 사용하여 Java에서 PDF를 해독하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java로 PDF 보안 제한 제거
Abstract: Java용 Aspose.PDF를 사용하여 PDF를 해독하는 방법을 알아보세요. Java 예제 세트에는 직접 소유자 비밀번호 복호화와 예외를 발생시키지 않고 오류를 처리할 수 있는 try-style 복호화 워크플로가 포함되어 있습니다.
---
## 
PDF 파일 암호 해독



소유자 암호가 있고 PDF에서 보안을 제거해야 하는 경우 이 작업 과정을 사용하십시오.


### 
단계


1. 
`PdfFileSecurity` 인스턴스를 생성합니다.

2. 
암호화된 PDF를 `bindPdf`으로 바인딩합니다.

3. 
소유자 비밀번호로 `decryptFile` 또는 `tryDecryptFile`으로 전화하세요.

4. 
암호 해독이 성공하면 출력을 저장합니다.

5. 
보안 개체를 닫습니다.


### 
자바 예제

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
