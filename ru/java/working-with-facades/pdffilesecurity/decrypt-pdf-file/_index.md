---
title: Расшифровать PDF-файл
linktitle: Расшифровать PDF-файл
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Узнайте, как расшифровать PDF-файл на Java с помощью фасада PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалите ограничения безопасности PDF с помощью Java
Abstract: Узнайте, как расшифровать PDF-файл с помощью Aspose.PDF для Java. Набор примеров Java включает в себя прямую расшифровку пароля владельца и рабочий процесс расшифровки в стиле try, который позволяет обрабатывать сбои, не вызывая исключения.
---
## Расшифровать PDF-файл

Используйте этот рабочий процесс, если у вас есть пароль владельца и вам необходимо снять защиту с PDF-файла.

### Шаги

1. Создайте экземпляр `PdfFileSecurity`.
2. Свяжите зашифрованный PDF-файл с помощью `bindPdf`.
3. Позвоните `decryptFile` или `tryDecryptFile`, указав пароль владельца.
4. Сохраните вывод, если расшифровка прошла успешно.
5. Закройте объект безопасности.

### Примеры Java

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
