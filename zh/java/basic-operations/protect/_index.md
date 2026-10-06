---
title: 在 Java 中保护 PDF 文件
linktitle: 加密和解密 PDF 文件
type: docs
weight: 70
url: /zh/java/protect-pdf-file/
description: 学习如何在 Java 中加密 PDF 文件、解密受保护的文档、更改密码以及检查密码保护。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中设置 PDF 权限并管理加密
Abstract: 本文阐述了如何在 Java 中使用 Aspose.PDF 保护 PDF 文件。内容包括应用用户密码和所有者密码、设置文档权限、加密和解密 PDF 文件、修改密码，以及检查加密文档的候选密码。
---
Aspose.PDF for Java 提供了多种 API，用于通过密码和权限保护 PDF 文件。

## 在 Java 中保护 PDF 文档

示例在 `ProtectDocumentExamples.java` 演示如何：

1. 对...进行加密 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 使用用户密码和所有者密码。
1. 使用...限制权限 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/)。
1. 选择一个 [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) 用于受保护的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 解密受保护的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 更改现有密码 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用...测试候选密码 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) 和 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

## 使用受限权限加密 PDF

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

## 加密 PDF 文件

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

## 解密受保护的 PDF

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

## 更改密码

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

## 从列表中确定正确的密码

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
