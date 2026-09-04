---
title: Шифрование и расшифровка PDF-файлов в Java
linktitle: Шифрование и расшифровка PDF-файла
type: docs
weight: 70
url: /ru/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Узнайте, как установить привилегии PDF, зашифровать файлы, расшифровать защищённые PDF и изменить пароли в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установите разрешения PDF и управляйте шифрованием в Java
Abstract: В этой статье объясняется, как защищать PDF-файлы с помощью Aspose.PDF for Java. Рассматриваются шифрование документов с паролями пользователя и владельца, применение ограничений разрешений, расшифровка файлов, изменение паролей и настройка привилегий с использованием или без использования методов, безопасных от исключений.
---
Aspose.PDF for Java предоставляет операции безопасности PDF через `PdfFileSecurity` фасад.

## Зашифруйте PDF с паролями пользователя и владельца

1. Создайте и привязать [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) обертка исходного PDF-документа.
1. Настройте [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) и [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) свойства, необходимые для примера.
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

## Зашифруйте PDF с использованием конкретного алгоритма

`encryptPdfWithEncryptionAlgorithm` использует `KeySize.x256` вместе с `Algorithm.AES` применить более сильные параметры шифрования.

## Расшифруйте защищённый PDF

1. Создайте и привязать [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) обертка исходного PDF-документа.
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

## Измените пароли и сбросить безопасность

The `PdfFileSecurityExamples` класс демонстрирует:

- `changeUserAndOwnerPassword` заменить оба пароля.
- `changePasswordAndResetSecurity` изменить пароли и повторно применить привилегии за один шаг.
- `tryChangePasswordWithoutException` для потока смены пароля без выбрасывания исключений.

## Установите привилегии документа

Чтобы ограничить действия, такие как печать и копирование:

1. Создайте и привязать [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) обертка исходного PDF-документа.
1. Установите требуемое [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) параметры разрешений или шифрования.
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


