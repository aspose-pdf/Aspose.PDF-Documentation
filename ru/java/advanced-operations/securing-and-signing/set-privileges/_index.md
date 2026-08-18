---
title: Шифрование и расшифровка PDF-файлов в Java
linktitle: Зашифровать и расшифровать PDF-файл
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Узнайте, как устанавливать права доступа к PDF, шифровать файлы, расшифровывать защищенные PDF-файлы и менять пароли в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установите разрешения PDF и управляйте шифрованием в Java
Abstract: В этой статье объясняется, как защитить файлы PDF с помощью Aspose.PDF для Java. Он охватывает шифрование документов с помощью паролей пользователя и владельца, применение ограничений разрешений, расшифровку файлов, изменение паролей и установку привилегий с использованием методов защиты от исключений или без них.
---
Aspose.PDF для Java предоставляет операции безопасности PDF через фасад `PdfFileSecurity`.

## Зашифруйте PDF-файл с помощью паролей пользователя и владельца.

1. Создайте и привяжите фасад [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) к исходному PDF-документу.
1. Настройте свойства [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) и [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/), необходимые для примера.
1. Сохраните обновленный PDF-документ через [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Зашифруйте PDF-файл с помощью определенного алгоритма

`encryptPdfWithEncryptionAlgorithm` использует `KeySize.x256` вместе с `Algorithm.AES` для применения более надежных настроек шифрования.

## Расшифровать защищенный PDF-файл

1. Создайте и привяжите фасад [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) к исходному PDF-документу.
1. Расшифруйте защищенный документ с помощью пароля владельца.
1. Сохраните обновленный PDF-документ через [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

Набор примеров также включает `tryDecryptPdfWithoutException`, который возвращает `false` вместо выдачи в случае сбоя расшифровки.

## Сменить пароли и сбросить безопасность

Класс `PdfFileSecurityExamples` демонстрирует:

- `changeUserAndOwnerPassword` для замены обоих паролей.
- `changePasswordAndResetSecurity`, чтобы сменить пароли и повторно применить привилегии за один шаг.
- `tryChangePasswordWithoutException` для потока смены пароля без выдачи.

## Установите права доступа к документу

Чтобы ограничить такие действия, как печать и копирование:

1. Создайте и привяжите фасад [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) к исходному PDF-документу.
1. Установите необходимые разрешения [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) или параметры шифрования.
1. Установите свойства, необходимые для примера.
1. Сохраните обновленный PDF-документ через [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
