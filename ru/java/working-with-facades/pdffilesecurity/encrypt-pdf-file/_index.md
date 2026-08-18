---
title: Зашифровать PDF-файл
linktitle: Зашифровать PDF-файл
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: Узнайте, как зашифровать PDF-файл и настроить разрешения в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Шифрование PDF-файлов и определение разрешений пользователей в Java
Abstract: Узнайте, как зашифровать PDF-файл с помощью Aspose.PDF для Java. Набор примеров Java охватывает шифрование на основе пароля с ограниченными привилегиями, шифрование с ориентацией на разрешения и шифрование на основе AES с размером ключа 256 бит.
---
## Зашифровать PDF-файл

Используйте `PdfFileSecurity`, если вам нужно защитить PDF-файл с помощью паролей и правил привилегий.

### Шаги

1. Создайте экземпляр `PdfFileSecurity`.
2. Свяжите исходный PDF-файл с помощью `bindPdf`.
3. Создайте объект `DocumentPrivilege`, соответствующий разрешенным действиям.
4. Вызовите соответствующую перегрузку `encryptFile` для нужного размера ключа и алгоритма.
5. Сохраните защищенный файл и закройте объект.

### Примеры Java

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

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
