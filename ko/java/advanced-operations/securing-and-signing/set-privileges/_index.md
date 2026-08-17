---
title: Java에서 PDF 파일 암호화 및 해독
linktitle: PDF 파일 암호화 및 해독
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: PDF 권한을 설정하고, 파일을 암호화하고, 보호된 PDF를 해독하고, Java에서 비밀번호를 변경하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 권한 설정 및 Java 암호화 관리
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 보호하는 방법을 설명합니다. 사용자 및 소유자 비밀번호로 문서 암호화, 권한 제한 적용, 파일 암호 해독, 비밀번호 변경, 예외 안전 방법 유무에 관계없이 권한 설정 등을 다룹니다.
---

Java용 Aspose.PDF는 `PdfFileSecurity` 외관을 통해 PDF 보안 작업을 노출합니다.


## 
사용자 및 소유자 비밀번호로 PDF 암호화


1. 
[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 파사드를 생성하고 소스 PDF 문서에 바인딩합니다.

1. 
예제에 필요한 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 및 [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) 속성을 구성합니다.

1. 
업데이트된 PDF 문서를 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/)를 통해 저장하세요.


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
```

## 
특정 알고리즘으로 PDF 암호화



`encryptPdfWithEncryptionAlgorithm`은 `Algorithm.AES`과 함께 `KeySize.x256`을 사용하여 더 강력한 암호화 설정을 적용합니다.


## 
보호된 PDF 암호 해독


1. 
[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 파사드를 생성하고 소스 PDF 문서에 바인딩합니다.

1. 
소유자 비밀번호로 보호된 문서의 암호를 해독합니다.

1. 
업데이트된 PDF 문서를 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/)를 통해 저장하세요.


```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```


예제 세트에는 암호 해독이 실패할 때 발생하는 대신 `false`을 반환하는 `tryDecryptPdfWithoutException`도 포함되어 있습니다.


## 
비밀번호 변경 및 보안 재설정



`PdfFileSecurityExamples` 클래스는 다음을 보여줍니다.


- 
`changeUserAndOwnerPassword` 두 비밀번호를 모두 교체하세요.

- 
`changePasswordAndResetSecurity`을 사용하면 한 단계로 비밀번호를 변경하고 권한을 다시 적용할 수 있습니다.

- 
`tryChangePasswordWithoutException`은 비밀번호 변경이 발생하지 않는 흐름입니다.


## 
문서 권한 설정



인쇄, 복사 등의 작업을 제한하려면:


1. 
[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 파사드를 생성하고 소스 PDF 문서에 바인딩합니다.

1. 
필수 [문서권한](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 권한이나 암호화 옵션을 설정하세요.

1. 
예제에 필요한 속성을 설정합니다.

1. 
업데이트된 PDF 문서를 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/)를 통해 저장하세요.

```java
public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
