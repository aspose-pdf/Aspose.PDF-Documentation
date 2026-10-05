---
title: "Java での PDF ファイルの保護"
linktitle: "PDF ファイルの暗号化と復号化"
type: docs
weight: 70
url: /ja/java/protect-pdf-file/
description: "Java で PDF ファイルを暗号化し、保護されたドキュメントを復号化し、パスワードを変更し、パスワード保護を検査する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF 権限の設定と暗号化の管理"
Abstract: "この記事では、Java で Aspose.PDF を使用して PDF ファイルを保護する方法について説明します。ユーザーと所有者のパスワードの適用、文書権限の設定、PDF ファイルの暗号化と復号化、パスワードの変更、暗号化された文書の候補パスワードのチェックについて取り上げます。"
---
Aspose.PDF for Java は、パスワードと権限で PDF ファイルを保護するための複数の API を提供します。

## Java での PDF 文書の保護

例は `ProtectDocumentExamples.java` に示されており、以下の方法を説明しています。

1. ユーザーパスワードと所有者パスワードを指定して、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に暗号化を適用してください。
1. [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) を使用して権限を制限してください。
1. 保護された [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のために [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) を選択してください。
1. 保護された [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を復号化してください。
1. 既存のパスワードを [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で変更してください。
1. 候補パスワードを [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) および [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) でテストしてください。

## 制限された権限で PDF の暗号化

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

## PDF ファイルの暗号化

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

## 保護された PDF の復号化

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

## リストから正しいパスワードの決定

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
