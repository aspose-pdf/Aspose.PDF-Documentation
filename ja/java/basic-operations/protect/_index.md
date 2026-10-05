---
title: "Java での PDFファイルの保護"
linktitle: PDFファイルの暗号化と復号化
type: docs
weight: 70
url: /ja/java/protect-pdf-file/
description: JavaでPDFファイルを暗号化し、保護されたドキュメントを復号化し、パスワードを変更し、パスワード保護を検査する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFの権限を設定し、暗号化を管理する
Abstract: この記事では、JavaでAspose.PDFを使用してPDFファイルを保護する方法について説明します。ユーザーと所有者のパスワードの適用、文書権限の設定、PDFファイルの暗号化と復号化、パスワードの変更、暗号化された文書の候補パスワードのチェックについて取り上げます。
---
Aspose.PDF for Java は、パスワードと権限でPDFファイルを保護するための複数の API を提供します。

## Java での PDF文書の保護

例は `ProtectDocumentExamples.java` やり方を示す:

1. 暗号化を適用する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ユーザーパスワードと所有者パスワードで。
1. で権限を制限する [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. 選択してください [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) 保護されたもののために [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 保護されたものを復号化する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 既存のパスワードを変更する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 候補パスワードを使用してテストする [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) そして [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## 制限された権限でPDFの暗号化

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

## PDFファイルの暗号化

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

## 保護されたPDFの復号化

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

## パスワードの変更

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

## リストから正しいパスワードを決定する

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
