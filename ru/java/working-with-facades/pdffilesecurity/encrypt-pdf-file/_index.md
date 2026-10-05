---
title: Шифрование PDF-файла
linktitle: Шифрование PDF-файла
type: docs
weight: 30
url: /ru/java/encrypt-pdf-file/
description: Узнайте, как зашифровать PDF и настроить разрешения в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-09-17"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Зашифровать PDF-файлы и определить пользовательские разрешения в Java
Abstract: Узнайте, как зашифровать PDF с помощью Aspose.PDF for Java. Набор примеров Java охватывает шифрование на основе пароля с ограниченными привилегиями, шифрование, ориентированное на разрешения, и шифрование AES с размером ключа 256 бит.
---
## Шифрование PDF-файла

Используйте `PdfFileSecurity`, когда вам нужно защитить PDF паролями и правилами привилегий.

### Шаги

1. Создайте экземпляр `PdfFileSecurity`.
2. Привяжите исходный PDF с помощью `bindPdf`.
3. Создайте объект `DocumentPrivilege`, соответствующий разрешённым действиям.
4. Вызовите соответствующую перегрузку `encryptFile` для нужного размера ключа и алгоритма.
5. Сохраните защищённый файл и закройте объект.

### Примеры на Java

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


