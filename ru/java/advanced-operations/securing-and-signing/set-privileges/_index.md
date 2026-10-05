---
title: Шифрование и расшифровка PDF-файлов в Java
linktitle: Шифрование и расшифровка PDF-файла
type: docs
weight: 70
url: /ru/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Узнайте, как установить привилегии PDF, зашифровать файлы, расшифровать защищённые PDF и изменить пароли в Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установите разрешения PDF и управляйте шифрованием в Java
Abstract: В этой статье объясняется, как защищать PDF-файлы с помощью Aspose.PDF for Java. Рассматриваются шифрование документов с паролями пользователя и владельца, применение ограничений разрешений, расшифровка файлов, изменение паролей и настройка привилегий с использованием или без использования методов, безопасных от исключений.
---
Aspose.PDF for Java предоставляет операции безопасности PDF через фасад `PdfFileSecurity`.

## Шифрование PDF с паролями пользователя и владельца

1. Создайте фасад [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) и привяжите к нему исходный PDF-документ.
1. Настройте свойства [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) и [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/), необходимые для примера.
1. Сохраните обновлённый PDF‑документ через [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Шифрование PDF с использованием конкретного алгоритма

`encryptPdfWithEncryptionAlgorithm` использует `KeySize.x256` вместе с `Algorithm.AES`, чтобы применить более сильные параметры шифрования.

## Расшифровка защищённого PDF

1. Создайте фасад [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) и привяжите к нему исходный PDF-документ.
1. Расшифруйте защищённый документ с паролем владельца.
1. Сохраните обновлённый PDF‑документ через [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

Набор примеров также включает `tryDecryptPdfWithoutException`, который возвращает `false` вместо выбрасывания исключения при неудачной расшифровке.

## Изменение паролей и сброс безопасности

Класс `PdfFileSecurityExamples` демонстрирует:

- `changeUserAndOwnerPassword` — замену обоих паролей.
- `changePasswordAndResetSecurity` — изменение паролей и повторное применение разрешений за один шаг.
- `tryChangePasswordWithoutException` — смену пароля без выбрасывания исключений.

## Установка привилегий документа

Чтобы ограничить действия, такие как печать и копирование:

1. Создайте фасад [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) и привяжите к нему исходный PDF-документ.
1. Установите требуемые параметры разрешений или шифрования [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Установите свойства, необходимые для примера.
1. Сохраните обновлённый PDF‑документ через [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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


