---
title: Защитите PDF-файлы в Java
linktitle: Зашифровать и расшифровать PDF-файл
type: docs
weight: 70
url: /java/protect-pdf-file/
description: Узнайте, как шифровать PDF-файлы, расшифровывать защищенные документы, менять пароли и проверять защиту паролей в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установите разрешения PDF и управляйте шифрованием в Java
Abstract: В этой статье объясняется, как защитить файлы PDF в Java с помощью Aspose.PDF. Он охватывает применение паролей пользователей и владельцев, настройку прав доступа к документам, шифрование и расшифровку PDF-файлов, изменение паролей и проверку потенциальных паролей для зашифрованных документов.
---
Aspose.PDF для Java предоставляет несколько API для защиты файлов PDF с помощью паролей и разрешений.

## Защитите PDF-документы в Java

Примеры в `ProtectDocumentExamples.java` демонстрируют, как:

1. Примените шифрование к [Документу](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с паролями пользователя и владельца.
1. Ограничьте разрешения с помощью [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Выберите [Криптоалгоритм](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) для защищенного [Документа](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Расшифруйте защищенный [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Измените существующие пароли в [Документе](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте пароли-кандидаты с помощью [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) и [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Зашифруйте PDF-файл с ограниченными привилегиями

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

## Расшифровать защищенный PDF-файл

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

## Сменить пароли

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
