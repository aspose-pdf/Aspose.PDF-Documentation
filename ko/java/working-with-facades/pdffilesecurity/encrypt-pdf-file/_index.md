---
title: PDF 파일 암호화
linktitle: PDF 파일 암호화
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: PdfFileSecurity 파사드를 사용하여 PDF를 암호화하고 Java에서 권한을 구성하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 파일을 암호화하고 Java에서 사용자 권한을 정의합니다.
Abstract: Java용 Aspose.PDF를 사용하여 PDF를 암호화하는 방법을 알아보세요. Java 예제 세트는 제한된 권한을 사용한 비밀번호 기반 암호화, 권한 중심 암호화 및 256비트 키 크기를 사용한 AES 기반 암호화를 다룹니다.
---
## 
PDF 파일 암호화



비밀번호와 권한 규칙으로 PDF를 보호해야 하는 경우 `PdfFileSecurity`을 사용하세요.


### 
단계


1. 
`PdfFileSecurity` 인스턴스를 생성합니다.

2. 
`bindPdf`으로 소스 PDF를 바인딩합니다.

3. 
허용된 작업과 일치하는 `DocumentPrivilege` 개체를 빌드합니다.

4. 
필요한 키 크기와 알고리즘에 대해 적절한 `encryptFile` 오버로드를 호출하세요.

5. 
보안 파일을 저장하고 개체를 닫습니다.


### 
자바 예제

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
