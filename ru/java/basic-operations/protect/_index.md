---
title: Защитить PDF-файлы в Java
linktitle: Шифровать и расшифровать PDF-файл
type: docs
weight: 70
url: /ru/java/protect-pdf-file/
description: Узнайте, как шифровать PDF-файлы, дешифровать защищённые документы, менять пароли и проверять защиту паролем в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить разрешения PDF и управлять шифрованием в Java
Abstract: В этой статье объясняется, как защищать PDF‑файлы в Java с помощью Aspose.PDF. Описывается применение пользовательских и владельческих паролей, установка привилегий документа, шифрование и дешифрование PDF‑файлов, изменение паролей и проверка кандидатных паролей для зашифрованных документов.
---
Aspose.PDF for Java предоставляет несколько API для защиты PDF‑файлов паролями и разрешениями.

## Защита PDF‑документов в Java

Примеры в `ProtectDocumentExamples.java` демонстрировать, как:

1. Применить шифрование к [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с паролями пользователя и владельца.
1. Ограничить разрешения с помощью [ПривилегияДокумента](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Выберите [КриптоАлгоритм](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) для защищенных [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Расшифровать защищённый [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Изменить существующие пароли в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Тестировать варианты паролей с [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) и [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Зашифровать PDF с ограниченными привилегиями

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

## Зашифровать PDF-файл

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

## Расшифровать защищённый PDF

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

## Изменить пароли

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

## Определите правильный пароль из списка

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

