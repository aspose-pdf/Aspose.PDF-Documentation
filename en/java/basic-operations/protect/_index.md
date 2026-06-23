---
title: Protect PDF Files in Java
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 70
url: /java/protect-pdf-file/
description: Learn how to encrypt PDF files, decrypt protected documents, change passwords, and inspect password protection in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set PDF permissions and manage encryption in Java
Abstract: This article explains how to protect PDF files in Java using Aspose.PDF. It covers applying user and owner passwords, setting document privileges, encrypting and decrypting PDF files, changing passwords, and checking candidate passwords for encrypted documents.
---
Aspose.PDF for Java provides several APIs for securing PDF files with passwords and permissions.

## Protect PDF documents in Java

The examples in `ProtectDocumentExamples.java` demonstrate how to:

1. Apply encryption to a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) with user and owner passwords.
1. Restrict permissions with [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Choose a [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) for the protected [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Decrypt a protected [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Change existing passwords on the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Test candidate passwords with [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) and [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Encrypt a PDF with restricted privileges

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

## Encrypt a PDF file

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

## Decrypt a protected PDF

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

## Change passwords

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

## Determine the correct password from a list

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
