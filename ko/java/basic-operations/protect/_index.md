---
title: Java에서 PDF 파일 보호
linktitle: PDF 파일 암호화 및 해독
type: docs
weight: 70
url: /java/protect-pdf-file/
description: PDF 파일을 암호화하고, 보호된 문서를 해독하고, 비밀번호를 변경하고, Java에서 비밀번호 보호를 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 권한 설정 및 Java 암호화 관리
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 PDF 파일을 보호하는 방법을 설명합니다. 사용자 및 소유자 비밀번호 적용, 문서 권한 설정, PDF 파일 암호화 및 해독, 비밀번호 변경, 암호화된 문서에 대한 후보 비밀번호 확인 등을 다룹니다.
---
Aspose.PDF for Java는 비밀번호와 권한으로 PDF 파일을 보호하기 위한 여러 API를 제공합니다.


## 
Java로 PDF 문서 보호



`ProtectDocumentExamples.java`의 예는 다음 방법을 보여줍니다.


1. 
사용자 및 소유자 비밀번호를 사용하여 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에 암호화를 적용합니다.

1. 
[문서권한](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/)으로 권한을 제한하세요.
1. 보호된 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에 대해 [암호알고리즘](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/)을 선택하세요.

1. 
보호된 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)의 암호를 해독하세요.

1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)의 기존 비밀번호를 변경하세요.

1. 
[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) 및 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 사용하여 후보 비밀번호를 테스트하세요.


## 
제한된 권한으로 PDF 암호화

```java
public static void encryptPassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
        documentPrivilege.setAllowScreenReaders(true);

        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                documentPrivilege,
                CryptoAlgorithm.AESx128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## PDF 파일 암호화


```java
public static void encryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                DocumentPrivilege.getAllowAll(),
                CryptoAlgorithm.RC4x128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## 
보호된 PDF 암호 해독


```java
public static void decryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), USER_PASSWORD);
    try {
        document.decrypt();
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## 
비밀번호 변경


```java
public static void changePassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), OWNER_PASSWORD);
    try {
        document.changePasswords(OWNER_PASSWORD, "newuser", "newowner");
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## 
목록에서 올바른 비밀번호를 확인하세요

```java
public static void determineCorrectPasswordFromList(Path inputFile) {
    try (PdfFileInfo info = new PdfFileInfo(inputFile.toString())) {
        System.out.println("File is password protected: " + info.isEncrypted());
    }
    String[] passwords = {"test", "test1", "test2", "test3", USER_PASSWORD};
    for (String password : passwords) {
        try {
            Document document = new Document(inputFile.toString(), password);
            try {
                int pageCount = document.getPages().size();
                if (pageCount > 0) {
                    System.out.println("Password '" + password + "' is correct. Pages: " + pageCount);
                }
            } finally {
                document.close();
            }
        } catch (InvalidPasswordException ex) {
            System.out.println("Wrong password: " + password);
        }
    }
}
```
